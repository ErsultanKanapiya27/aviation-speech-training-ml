import yaml
import re


def load_config(path="configs/scenario.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


# очистка текста
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


# сравнение фраз
def phrase_match(text, phrase, threshold=0.6):
    text_words = text.split()
    phrase_words = phrase.split()

    if not phrase_words:
        return False

    matched = sum(1 for w in phrase_words if w in text_words)
    score = matched / len(phrase_words)

    return score >= threshold


# поиск позиции шага (для проверки порядка)
def find_step_positions(text, steps):
    positions = []

    for step in steps:
        pos = -1
        for phrase in step["phrases"]:
            if phrase_match(text, phrase):
                pos = text.find(phrase.split()[0])  # приблизительная позиция
                break
        positions.append(pos)

    return positions


def score_text(text, config):
    text = clean_text(text)

    steps = config["steps"]
    score = 100
    errors = []

    positions = find_step_positions(text, steps)

    # Проверка пропусков
    for i, step in enumerate(steps):
        found = any(phrase_match(text, phrase) for phrase in step["phrases"])
        if not found:
            penalty = config["scoring"]["missing_penalty"] * 100
            score -= penalty
            errors.append(f"Missing step: {step['name']}")

    # Проверка порядка
    if config.get("order_strict", False):
        last_pos = -1
        for i, pos in enumerate(positions):
            if pos != -1:
                if pos < last_pos:
                    penalty = config["scoring"]["order_penalty"] * 100
                    score -= penalty
                    errors.append(f"Wrong order: {steps[i]['name']}")
                last_pos = pos

    return max(round(score, 2), 0), errors
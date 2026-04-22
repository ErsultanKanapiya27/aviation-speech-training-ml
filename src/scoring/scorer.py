import yaml


def load_config(path="configs/scenario.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def find_step_positions(text, steps):
    positions = []

    for step in steps:
        pos = -1
        for phrase in step["phrases"]:
            idx = text.find(phrase)
            if idx != -1:
                pos = idx
                break
        positions.append(pos)

    return positions


def score_text(text, config):
    steps = config["steps"]
    score = 100
    errors = []

    positions = find_step_positions(text, steps)

    # Проверка пропусков
    for i, pos in enumerate(positions):
        if pos == -1:
            score -= config["scoring"]["missing_penalty"] * 100
            errors.append(f"Missing step: {steps[i]['name']}")

    # Проверка порядка
    if config.get("order_strict", False):
        last_pos = -1
        for i, pos in enumerate(positions):
            if pos != -1:
                if pos < last_pos:
                    score -= config["scoring"]["order_penalty"] * 100
                    errors.append(f"Wrong order: {steps[i]['name']}")
                last_pos = pos

    return max(score, 0), errors
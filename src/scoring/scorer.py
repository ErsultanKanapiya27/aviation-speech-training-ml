import yaml


def load_config(path="configs/scenario.yaml"):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def score_text(text, config):
    steps = config["steps"]
    score = 100
    errors = []

    for step in steps:
        found = any(phrase in text for phrase in step["phrases"])
        if not found:
            score -= config["scoring"]["missing_penalty"] * 100
            errors.append(f"Missing step: {step['name']}")

    return max(score, 0), errors
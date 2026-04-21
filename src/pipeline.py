import argparse
from scoring.scorer import load_config, score_text
from utils.logger import log


def fake_asr(audio_path):
    return "cleared for takeoff runway 27"


def normalize(text):
    return text.lower().strip()


def main(audio, scenario):
    log(f"[INFO] Processing: {audio}")

    config = load_config()

    # ASR
    text = fake_asr(audio)
    log(f"[ASR] Raw: {text}")

    # Normalize
    text = normalize(text)
    log(f"[NORM] {text}")

    # Score
    score, errors = score_text(text, config)

    log(f"[RESULT] Score: {score}")
    log(f"[RESULT] Errors: {errors}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True)
    parser.add_argument("--scenario", required=True)

    args = parser.parse_args()
    main(args.audio, args.scenario)
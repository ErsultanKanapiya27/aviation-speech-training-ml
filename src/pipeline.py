import argparse

from asr.whisper_asr import WhisperASR
from scoring.scorer import load_config, score_text
from utils.logger import log, Timer
from metrics.cer import cer
import re

def normalize(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


def main(audio, scenario):
    total_timer = Timer()

    log("INFO", f"Processing file: {audio}")

    config = load_config()

    # ASR
    asr_timer = Timer()
    asr = WhisperASR()
    text = asr.transcribe(audio)
    log("ASR", f"Text: {text}")
    log("ASR", f"Time: {asr_timer.stop()} sec")

    if not text:
        log("ERROR", "Empty transcription")
        return

    # Normalize
    text = normalize(text)
    log("NORM", text)

    # Score
    score, errors = score_text(text, config)

    # Fake reference (для демонстрации метрики)
    reference = "cleared for takeoff runway 27"
    error_rate = cer(reference, text)

    log("RESULT", f"Score: {score}")
    log("RESULT", f"Errors: {errors}")
    log("METRIC", f"CER: {round(error_rate, 3)}")

    log("TOTAL", f"Pipeline time: {total_timer.stop()} sec")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True)
    parser.add_argument("--scenario", required=True)

    args = parser.parse_args()
    main(args.audio, args.scenario)
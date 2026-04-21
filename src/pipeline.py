import argparse

def fake_asr(audio_path):
    return "cleared for takeoff runway 27"

def normalize(text):
    return text.lower()

def score(text):
    if "cleared for takeoff" in text:
        return 80
    return 40

def main(audio, scenario):
    print("Processing:", audio)

    text = fake_asr(audio)
    text = normalize(text)
    result = score(text)

    print("Recognized:", text)
    print("Score:", result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", required=True)
    parser.add_argument("--scenario", required=True)

    args = parser.parse_args()
    main(args.audio, args.scenario)

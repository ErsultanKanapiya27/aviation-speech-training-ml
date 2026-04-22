# Aviation Speech Training ML

## Description

Pipeline for analyzing aviation phraseology using speech recognition and rule-based scoring.

## Run

pip install -r requirements.txt

python src/pipeline.py --audio data/test.wav --scenario atc_clearance

## Stack

- Python 3.10+
- Whisper (planned)
- YAML configs

## Status

Baseline pipeline implemented (ASR stub + scoring).

## Scoring Logic

The system evaluates recognized speech against a predefined scenario:

- Each step contains allowed phrase variations
- Missing steps reduce the score
- Errors are explicitly reported

Example output:

[RESULT] Score: 70
[RESULT] Errors: ['Missing step: greeting']

<img width="1112" height="189" alt="image" src="https://github.com/user-attachments/assets/96f203c3-2086-4b02-8aab-fe71bb744c2e" />

<img width="1111" height="188" alt="image" src="https://github.com/user-attachments/assets/3ea9e557-6fef-4e0e-b831-68840914b460" />

<img width="1113" height="194" alt="image" src="https://github.com/user-attachments/assets/57b6a086-9323-4a6f-b855-48520053132b" />

<img width="1115" height="190" alt="image" src="https://github.com/user-attachments/assets/45c2ea68-f60d-4c55-9a0b-1af348134caa" />

## Future Work

- Improve ASR accuracy and experiment with different models
- Add more aviation scenarios (taxiing, landing, emergency)
- Implement advanced metrics (WER, CER)
- Add real-time microphone input
- Develop web interface for interactive training

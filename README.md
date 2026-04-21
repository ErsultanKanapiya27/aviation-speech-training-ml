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

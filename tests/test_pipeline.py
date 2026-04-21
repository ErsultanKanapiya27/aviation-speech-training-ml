from src.scoring.scorer import load_config, score_text


def test_correct_phrase():
    config = load_config()
    text = "cleared for takeoff runway 27"

    score, errors = score_text(text, config)

    assert score > 50
    assert len(errors) == 0


def test_missing_step():
    config = load_config()
    text = "runway 27"

    score, errors = score_text(text, config)

    assert score < 100
    assert len(errors) > 0
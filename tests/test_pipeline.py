from src.scoring.scorer import load_config, score_text


def test_order_violation():
    config = load_config()
    text = "runway 27 cleared for takeoff"

    score, errors = score_text(text, config)

    assert score < 100
    assert any("Wrong order" in e for e in errors)
def cer(reference, hypothesis):
    if not reference:
        return 1.0

    distance = sum(1 for a, b in zip(reference, hypothesis) if a != b)
    distance += abs(len(reference) - len(hypothesis))

    return distance / len(reference)
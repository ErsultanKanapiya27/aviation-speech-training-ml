import time


class Timer:
    def __init__(self):
        self.start = time.time()

    def stop(self):
        return round(time.time() - self.start, 3)


def log(stage, message):
    print(f"[{stage}] {message}")
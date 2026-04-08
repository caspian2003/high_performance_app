import time

class Monitor:
    def __init__(self):
        self.start = time.time()

    def report(self):
        end = time.time()
        print(f"Execution Time: {end - self.start:.2f} seconds")
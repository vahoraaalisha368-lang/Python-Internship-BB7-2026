import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        print(f"Time taken: {self.end - self.start:.4f} seconds")
        return False  

with Timer():
    total = 0
    for i in range(1000000):
        total += i
    print("Loop done, total:", total)
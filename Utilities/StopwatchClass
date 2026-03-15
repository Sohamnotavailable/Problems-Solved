"""
Simple stopwatch measuring elapsed time in milliseconds.
Methods:
- start(): reset start time to current time.
- stop(): store current time as end time.
- getElapsedTime(): return (end - start) in milliseconds
.
The constructor should set start time to the current time.
"""
import time

class StopWatch:

    def __init__(self):
        self.start_time = time.time()
        self.end_time = self.start_time

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def getElapsedTime(self):
        return (self.end_time - self.start_time) * 1000

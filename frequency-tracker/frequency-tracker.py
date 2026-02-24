class FrequencyTracker:

    def __init__(self):
        self.counter = Counter()
        self.freq = Counter()


    def add(self, number: int) -> None:
        self.freq[self.counter[number]] -= 1
        self.counter[number] += 1
        self.freq[self.counter[number]] += 1

    def deleteOne(self, number: int) -> None:
        if self.counter[number] > 0:
            self.freq[self.counter[number]] -= 1
            self.counter[number] -= 1
            self.freq[self.counter[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0

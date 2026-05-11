from typing import List
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxFreq = max(freq.values())
        maxCount = sum(1 for val in freq.values() if val == maxFreq)

        return max(len(tasks), (maxFreq - 1) * (n + 1) + maxCount)

import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        cooldown = []
        taskTally = {}

        # Count task frequencies
        for task in tasks:
            taskTally[task] = taskTally.get(task, 0) + 1

        # Use negative frequency to simulate a max-heap
        for task, amount in taskTally.items():
            heapq.heappush(maxHeap, [-amount, task, 0])  # [neg_count, task, cooldown]

        cycles = 0

        while maxHeap or cooldown:
            task = None

            # Run the highest priority task if available
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task[0] += 1  # since it's negative, adding moves toward 0 (i.e., less remaining)

            # Decrease cooldown for all tasks
            newCooldown = []
            for ctask in cooldown:
                ctask[2] -= 1
                if ctask[2] == 0:
                    heapq.heappush(maxHeap, ctask)
                else:
                    newCooldown.append(ctask)
            cooldown = newCooldown

            # If the task still has remaining count, cooldown it
            if task and task[0] != 0:
                task[2] = n
                cooldown.append(task)

            cycles += 1

        return cycles

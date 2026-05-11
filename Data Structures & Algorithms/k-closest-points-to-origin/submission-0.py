from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if not points:
            return []

        # Compute distances and pair with points
        distance_pairs = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            distance_pairs.append((dist, [x, y]))

        # Sort by distance
        distance_pairs.sort(key=lambda pair: pair[0])

        # Extract the first k points
        return [pair[1] for pair in distance_pairs[:k]]


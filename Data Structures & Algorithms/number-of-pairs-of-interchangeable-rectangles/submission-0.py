class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        counts = {}
        answer = 0
        for width, height in rectangles:
            a, b = width, height
            while b:
                a, b = b, a % b
            key = (width // a, height // a)
            answer += counts.get(key, 0)
            counts[key] = counts.get(key, 0) + 1
        return answer


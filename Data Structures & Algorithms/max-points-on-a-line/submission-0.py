class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        from math import gcd
        answer = 1
        for i, (x,y) in enumerate(points):
            counts = {}
            for xx,yy in points[i+1:]:
                dx,dy = xx-x,yy-y
                g = gcd(dx,dy)
                dx,dy = dx//g,dy//g
                if dx<0 or (dx==0 and dy<0): dx,dy=-dx,-dy
                key=(dx,dy)
                counts[key]=counts.get(key,0)+1
                answer=max(answer,counts[key]+1)
        return answer


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departures = {start for start, end in paths}
        for start, end in paths:
            if end not in departures: return end
        return ""


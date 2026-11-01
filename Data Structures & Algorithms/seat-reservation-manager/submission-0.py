class SeatManager:
    def __init__(self,n:int):self.next=1;self.free=[]
    def reserve(self)->int:
        if self.free:return heapq.heappop(self.free)
        seat=self.next;self.next+=1;return seat
    def unreserve(self,seatNumber:int)->None:heapq.heappush(self.free,seatNumber)

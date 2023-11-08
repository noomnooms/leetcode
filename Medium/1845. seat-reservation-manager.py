# 1845. Seat Reservation Manager https://leetcode.com/problems/seat-reservation-manager/
# Runtime: 466 ms
# Memory Usage: 41.88 MB
class SeatManager(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.counter = 0
        self.heap = []

    def reserve(self):
        """
        :rtype: int
        """
        if len(self.heap) == 0:
            self.counter += 1
            return self.counter
        else: return heapq.heappop(self.heap)
        

    def unreserve(self, seatNumber):
        """
        :type seatNumber: int
        :rtype: None
        """
        if seatNumber == self.counter:
            self.counter -= 1
        else:
            heapq.heappush(self.heap, seatNumber)
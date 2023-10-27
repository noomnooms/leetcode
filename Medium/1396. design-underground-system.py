# 1396. Design Underground System https://leetcode.com/problems/design-underground-system/
# Runtime: 458 ms
# Memory Usage: 26.42 MB
import statistics as st


class UndergroundSystem:

    def __init__(self):
        self.travel_list = {}
        self.travelling = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        try:
            self.travel_list[stationName].append([id, None, t])
        except:
            self.travel_list[stationName] = [[id, None, t]]
        self.travelling[id] = stationName

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start = self.travelling[id]
        for i in self.travel_list[start]:
            if i[0] == id and i[1] == None:
                i[1] = stationName
                i[2] = t - i[2]
                break
        del self.travelling[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        avg = []
        for i in self.travel_list[startStation]:
            if i[1] == endStation:
                avg.append(i[2])

        return st.mean(avg)

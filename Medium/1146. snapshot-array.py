# 1146. Snapshot Array https://leetcode.com/problems/snapshot-array/
# Runtime: 729 ms
# Memory Usage: 46.44 MB

class SnapshotArray(object):
    def __init__(self, length):
        """
        :type length: int
        """
        self.snap_id = 0
        self.arr = [[[self.snap_id, 0]] for i in range(length)]

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.arr[index][-1][0] == self.snap_id:
            self.arr[index][-1][1] = val
        else:
            self.arr[index].append([self.snap_id, val])

    def snap(self):
        """
        :rtype: int
        """
        self.snap_id += 1
        return self.snap_id-1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        # ans = self.arr[index][-1][1]
        # for i in range(len(self.arr[index])-1, -1, -1):
        #     if self.arr[index][i][0]<=snap_id: break
        #     ans =  self.arr[index][i-1][1]
        # return ans
        i = bisect.bisect(self.arr[index], [snap_id+1])-1
        return self.arr[index][i][1]

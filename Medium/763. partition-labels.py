# 763. Partition Labels https://leetcode.com/problems/partition-labels/
# Runtime: 40 ms
# Memory Usage: 16.13 MB
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        log = {}
        for i in range(len(s)):
            try: log[s[i]].append(i)
            except: log[s[i]] = [i]
        
        order = list(log.keys())
        ans = [[log[order[0]][0], log[order[0]][-1]]]
        for i in order:
            if i == order[0]: continue
            curr_substr = ans[-1]
            curr_char = log[i]

            if curr_char[0]<curr_substr[-1] or curr_char[-1]<curr_substr[-1]:
                curr_substr[-1] = max(curr_substr[-1], curr_char[-1])
            else:
                ans.append([curr_char[0], curr_char[-1]])
        return [i[-1]-i[0]+1 for i in ans]
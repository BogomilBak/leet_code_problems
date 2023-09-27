class Solution(object):
    def uniqueOccurrences(self, arr):
        result = {}

        for x in set(arr):
            if arr.count(x) in result:
                return False

            result[arr.count(x)] = True

        return True

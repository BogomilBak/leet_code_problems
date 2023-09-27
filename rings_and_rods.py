class Solution(object):
    def countPoints(self, rings):
        result = 0
        hash = {}

        for i in range(len(rings)):
            if not rings[i].isdigit():
                continue

            if rings[i] not in hash:
                hash[rings[i]] = set()

            hash[rings[i]].add(rings[i - 1])

        for ring, colour in hash.items():
            if len(colour) == 3:
                result += 1

        return result

test = Solution()
a = "B0B6G0R6R0R6G9"
print(test.countPoints(a))



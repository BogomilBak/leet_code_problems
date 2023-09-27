class Solution(object):
    def sortPeople(self, names, heights):
        list_a = []

        for i in range(len(names)):
            list_a.append([heights[i], names[i]])

        result_sorted = sorted(list_a, key=lambda x: x[0], reverse=True)

        result = []

        for _, name in result_sorted:
            result.append(name)

        return result



test = Solution()
a = ["Alice","Bob","Bob"]
b = [155,185,150]
print(test.sortPeople(a, b))

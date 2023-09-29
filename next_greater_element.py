class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = []

        for element in nums1:
            index = nums2.index(element)
            value = element
            while index < len(nums2) - 1:
                if nums2[index + 1] > element:
                    value = nums2[index + 1]
                    break
                index += 1
            if value > element:
                result.append(value)
            else:
                result.append(-1)

        return result


test = Solution()
a = [4,1,2]
b = [1,3,4,2]
print(test.nextGreaterElement(a, b))

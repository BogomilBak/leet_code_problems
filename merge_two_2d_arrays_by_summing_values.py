class Solution(object):
    def mergeArrays(self, nums1, nums2):
        hash_map = {}
        i = 0

        while i < min(len(nums1), len(nums2)):
            if nums1[i][0] not in hash_map:
                hash_map[nums1[i][0]] = 0
            hash_map[nums1[i][0]] += nums1[i][1]

            if nums2[i][0] not in hash_map:
                hash_map[nums2[i][0]] = 0

            hash_map[nums2[i][0]] += nums2[i][1]

            i += 1

        longer = nums1 if len(nums1) > len(nums2) else nums2

        while i < len(longer):
            if longer[i][0] not in hash_map:
                hash_map[longer[i][0]] = 0
            hash_map[longer[i][0]] += longer[i][1]

            i += 1

        hash_map_sorted = sorted(hash_map.items(), key=lambda x: x[0])

        return list(hash_map_sorted)

test = Solution()
a = [[2,4],[3,6],[5,5]]
b = [[1,3],[4,3]]
print(test.mergeArrays(a, b))



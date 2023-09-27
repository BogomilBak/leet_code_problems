class Solution(object):
    def countBalls(self, lowLimit, highLimit):
        boxes = {}

        for ball in range(lowLimit, highLimit + 1):
            box_number = self.helper(ball)
            if box_number in boxes:
                boxes[box_number] += 1
            else:
                boxes[box_number] = 1

        ordered_boxes = sorted(boxes.items(), key=lambda x: x[-1], reverse=True)

        for key, value in ordered_boxes:
            return value

    def helper(self, value):
        nums = 0
        while value > 9:
            nums += value % 10
            value = value // 10

        nums += value

        return nums

test = Solution()
a = 1
b = 10
print(test.countBalls(a, b))
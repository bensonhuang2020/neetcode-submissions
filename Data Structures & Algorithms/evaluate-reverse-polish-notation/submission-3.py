class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        nums = []
        for x in tokens:
            if x in operators:
                second_num = int(nums.pop())
                first_num = int(nums.pop())
                match x:
                    case "+":
                        nums.append(first_num + second_num)
                    case "-":
                        nums.append(first_num - second_num)
                    case "*":
                        nums.append(first_num * second_num)
                    case "/":
                        nums.append(int(first_num / second_num))
            else:
                nums.append(int(x))
        return nums[0]
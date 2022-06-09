class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for ele in range(len(numbers)//2  +1):
            if target-numbers[ele] in numbers[ele+1::]:
                a=numbers[ele+1::].index(target-numbers[ele])
                return [ele+1,a+2+ele]
            elif target-numbers[len(numbers)-1-ele] in numbers[:len(numbers)-1-ele:]:
                b=numbers.index(target-numbers[len(numbers)-1-ele])
                return [b+1,len(numbers)-ele]
            
        
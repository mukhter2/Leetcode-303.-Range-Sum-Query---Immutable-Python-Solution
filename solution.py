class NumArray:
    finalList=[]
    def listReturn(self,nums):
        lstfin=[]
        for x in range(0,len(nums)):
            if x==0:
                lstfin.append(nums[0])
            else:
                lstfin.append(lstfin[x-1]+nums[x])
        return lstfin
    def __init__(self, nums: List[int]):
        global finalList
        finalList=self.listReturn(nums)
    def sumRange(self, left: int, right: int) -> int:
        if left==0:
            return finalList[right]
        else:
            return finalList[right]-finalList[left-1]


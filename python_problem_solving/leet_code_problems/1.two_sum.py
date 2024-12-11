def main():

    l=input("Enter a list eg. 1,2,3,... :\t").split(",")
    int_l=[int(n) for n in l]
    target=int(input("Target=\t"))
    first=Solution()
    print(first.twoSum(int_l,target))
   
# NOTE : This is the second solution  (Best One)
class Solution:
    def twoSum(self, nums:list[int], target:int)->list[int]:
        seen={}
        for i,num in enumerate(nums):
            if target - num in seen:
                return(seen[target-num],i)
            elif num not in seen:
                seen[num]=i
    
# NOTE : This is the first solution   
# class Solution:
#     def twoSum(self, nums:list[int], target:int)->list[int]:
#         for i in range(len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if nums[i]+nums[j]==target:
#                     return [i,j]
                
            
            


if __name__=="__main__":
    main()
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack_s = []
        output = 0
        for idx, item in enumerate(s):
            
            if(idx == 0):
                stack_s.append(item)
                output = len(stack_s)
                print(f'{idx} -  {item} - {"".join(stack_s)} ')
                continue
            elif(len(stack_s) > 1 and item in stack_s):
                
                print(f'Output is : {output}')
                stack_s.append(item)
                index_of_same_char = stack_s.index(item)
                stack_s = stack_s[index_of_same_char+1::]
                if(output < len(stack_s)):
                    output = len(stack_s)
                    print(f'maxstack: {"".join(stack_s)}  ')
                
            elif(item not in stack_s):
                stack_s.append(item)
                if(output < len(stack_s)):
                    output = len(stack_s)
            print(f'{idx} -  {item} - {"".join(stack_s)}  ')
        return output
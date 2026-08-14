class Solution:
    def solve(self,index,subset,digits,result,char_map):
        if index>=len(digits):
            result.append("".join(subset))
            return
        for ch in char_map[int(digits[index])]:
            subset.append(ch)
            self.solve(index+1,subset,digits,result,char_map)
            subset.pop()
    def letterCombinations(self, digits: str) -> List[str]:
        char_map =["", "", "abc", "def", "ghi", "jkl",
                    "mno", "pqrs", "tuv", "wxyz"]
        result=[]
        self.solve(0,[],digits,result,char_map)
        return result
        
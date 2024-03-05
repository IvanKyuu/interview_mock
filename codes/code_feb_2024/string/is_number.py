class Solution:
    def isNumber(self, s: str) -> bool:
        lst = [s]
        if "e" in lst[0] or "E" in lst[0]:
            if s.count("e") + s.count("E") > 1:
                return False
            lst = list(s.replace("e", " ").replace("E", " ").split())
        if len(lst) == 2 and not self.is_integer(lst[1]):
            return False
        else:
            lst = []
        return self.is_decimal(lst[0]) or self.is_integer(lst[0])

    def is_decimal(self, s:str)->bool:
        if len(s) == 0 or (len(s) == 1 and not s.isdigit()):
            return False
        if s[0] in '+-':
            s = s[1:]
        if s[-1] == '.' and s[:-1].isdigit():
            return True
        elif s[0] == '.' and s[1:].isdigit():
            return True
        elif '.' in s:
            nums = s.split('.')
            if len(nums) != 2 or not nums[0].isdigit() or not nums[1].isdigit():
                return False
        return True

    def is_integer(self, s:str):
        if len(s) == 0:
            return False
        if s[0] in '+-':
            s = s[1:]
        return s.isdigit()

s = Solution()
print(s.isNumber("95a54eE53"))
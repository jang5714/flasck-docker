class Palindrome(object):
    def str_to_list(self, payload: str) -> [] :
        return [i for i in payload if i.isalnum()]

    def isPalindrome(self, ls: []) -> bool:
        return {"RESULT": False for i in ls if ls.pop(0) != ls.pop()}

class Reverse_String():

    def str_to_list(self, payload: str) -> []:
        strs = []
        for char in payload:
            if char.isalnum():
                strs.append(char.lower())
        return strs

    def reverse_str_list (self, ls: []) -> []:
        return ls[::-1]

    def list_to_str(self, ls: []) -> str:
        strs = "".join(ls)
        return strs


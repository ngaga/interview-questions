def reverseParentheses(s : str) -> str:
    # returns reversed and next index
    def rec(input : str, i : int) -> tuple: 
        res = ""
        while i < len(input):
            if input[i] == "(":
                tmp, i = rec(input, i + 1)
                res += tmp[::-1]
            elif input[i] == ")":
                return res, i + 1
            else:
                res += input[i]
                i += 1
        return res, i
        
    r, _ = rec(s, 0)
    return r


s = "(abcd)"
s = "(u(love)i)"
s = "l(kcu)y"
s = "(((serpac)(xua)(eiar)))"
s = "(ed(et(oc))el)"
print("Result: "+ reverseParentheses(s))

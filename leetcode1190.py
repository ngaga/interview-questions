def reverseParentheses(s : str) -> str:  
  stack = []
  for c in s:
    print(c)
    if c == ')':
      tmp = []
      while stack and stack[-1] != '(':
        tmp.append(stack.pop())
        print(tmp)
      # remove '('
      stack.pop()
      stack.extend(tmp)
    else:
      stack.append(c)
  return ''.join(stack)


s = "(abcd)"
s = "(u(love)i)"
s = "(ed(et(oc))el)"
s = "(((serpac)(xua)(eiar)))"
s = "l(kcu)y"
print("Result: "+ reverseParentheses(s))

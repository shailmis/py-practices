def is_paren(s):
    if "()" in s:
        return is_paren(s.replace('()',''))
    else:
        return not bool(s)

in_list = [
    "()",
    "(())",
    "()(",
    "{}",
    "["]
for i in in_list:
    print(is_paren(i))



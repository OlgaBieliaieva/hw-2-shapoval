from collections import deque

def is_palindrome(s):
    d = deque()
    s = ''.join(filter(str.isalnum, s)).lower()
    for char in s:
        d.append(char)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

print(is_palindrome("Level"))
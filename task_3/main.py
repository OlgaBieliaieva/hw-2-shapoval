def is_symmetric(expression):
    stack = []
    matching_pairs = {')': '(', '}': '{', ']': '['}
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != matching_pairs[char]:
                return "Несиметрично"
    return "Симетрично" if not stack else "Несиметрично"


print(is_symmetric("( ){[ 1 ]( 1 + 3 )( ){ }}"))  
print(is_symmetric("( 23 ( 2 - 3);"))  
print(is_symmetric("( 11 }"))  

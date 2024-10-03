def is_palindrome(text):
    if not isinstance(text, str):
        return False
    
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True


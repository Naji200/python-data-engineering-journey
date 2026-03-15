def reverse_string(s):
    return s[::-1]
print(reverse_string("Hello, World!"))  # !dlroW ,olleH

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello, World!"))  # 3
def is_palindrome(s):
    cleaned = ''.join(s.split()).lower()
    return cleaned == cleaned[::-1]
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Hellonaji"))  # False
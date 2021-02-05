def palindrome(w, idx):
    if idx >= len(w)/2:
        return f'{w} is a palindrome'

    elif w[idx] == w[len(w)-1-idx]:
        return palindrome(w, idx+1)
    else:
        return f'{w} is not a palindrome'


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
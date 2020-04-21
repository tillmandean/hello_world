def palindrome(word):
    """Boolean method checking to see if word is palindrome"""
    if(len(word) == 0):
        print("Enter a word please.")
        return False
    head = 0
    tail = len(word) - 1
    if(tail == 0):
        return True
    elif(word[head] == word[tail]):
        if(head+1 == tail):
            return True
        else:
            return palindrome(word[head+1:tail])
    else:
        return False

print(palindrome("racecar"))
print(palindrome("tillman"))
print(palindrome("abba"))
print(palindrome("a"))
print(palindrome("ab"))

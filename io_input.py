def reverse(text):
    return text[::-1]

def is_palindrome(text):
    print 'Reversed text : ', reverse(text)
    return text==reverse(text)

somthing = raw_input("Enter text : ")

if is_palindrome(somthing):
    print "It is a palindrome"
else:
    print "It is NOT a palindrome"
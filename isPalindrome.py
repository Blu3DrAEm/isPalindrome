# isPalindrome
# version 1.2
# josh anderson 10/15/2020

list = []
while True:
        palindrome = input('Enter a word to see if it is a palindrome: ')
        isPalindrome = palindrome.find(palindrome[::-1])==0
        if isPalindrome == True:
                list.append(palindrome)
                print(isPalindrome, list)
        else:
                print('That word is not a palindrome. Try again')

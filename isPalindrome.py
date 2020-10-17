# ispalindrome
# checks to see if a word is a palindrome
# Josh Anderson 10/15/2020
# current version 1.3 (10/17/2020)

list = []
score = 0

print('Enter 5 palindromes to win!')
while True:
	palindrome = input('Enter a word to see if it is a palindrome: ')
	isPalindrome = palindrome.find(palindrome[::-1])==0
	if isPalindrome == True:
		list.append(palindrome)
		score = score + 1
		print(isPalindrome, list)
	else:
		print('That word is not a palindrome. Try again!')

	if score == 5:
		print('You win!')
		exit()

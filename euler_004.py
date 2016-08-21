def palindrome_number(n):
	current_palindrome = 1
	for i in range(10**(n-1),10**(n),1):
		for j in range(10**(n-1),10**(n),1):
			value = i*j
			check_drome = str(value)
			if len(check_drome) % 2 == 0:
				start = check_drome[0:len(check_drome)/2]
				end = check_drome[len(check_drome)/2:len(check_drome)+1][::-1]
				if start == end and value > current_palindrome:
					current_palindrome = value
			else:
				start = check_drome[0:len(check_drome)/2]
				end = check_drome[len(check_drome)/2 + 1:len(check_drome)+1][::-1]
				if start == end and value > current_palindrome:
					current_palindrome = value

	return current_palindrome

if __name__ == "__main__":
	print palindrome_number(3)

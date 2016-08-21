def even_sums():
	counter = 1
	base = 1
	summ = 0
	while counter < 4000000:
		counter = counter + base
		if counter % 2 == 0 and counter < 4000000:
			summ += counter
		base = counter - base
	return summ

if __name__ == "__main__":
	print even_sums()




def print_square(size):
	# For each row in square
	for i in range(size):
		# For each brick in row
		for j in range(size-i):
			# Print brick
			print("#",end="")
		print()  
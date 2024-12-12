# from first.py import print_square
def main():
	print_row(3)


def print_square(size):
	# For each row in square
	for i in range(size):
		# For each brick in row
		for j in range(i+1):
			# Print brick
			print("#",end="")
		print()

def print_row(width):
	print("?"* width)
	print_square(3)











main()
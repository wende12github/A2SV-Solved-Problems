import sys


def main() -> None:
	input_data = list(map(int, sys.stdin.read().strip().split()))
	if not input_data:
		return

	n = input_data[0]
	coords = input_data[1:1 + n]

	coords.sort()
	median = coords[(n - 1) // 2]
	print(median)


if __name__ == "__main__":
	main()


def split_and_join(line):
    line = line.split(" ")
    st = "-".join(line)
    return st

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

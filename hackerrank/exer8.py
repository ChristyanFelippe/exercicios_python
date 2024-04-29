

def split_and_join(line):
    replaced = line.replace(" ", "-")
    return replaced

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
file1 = open('cities.txt')

for line in file1:
    # remove the \n at the end of the line
    line = line.strip()
    print(line)


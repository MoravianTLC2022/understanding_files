#Opens the file to both read and write
file1 = open('cities.txt', 'r+')
print('These are your current cities: ' + '\n')
print(file1.read())

new_city = input("Add a city to the file: ")
file1.write('\n' + new_city)
file1.close()

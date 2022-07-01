#Opens the file to both amend and read
file1 = open('cities.txt', 'a+')
print('These are your current cities: ' + '\n')
#Ensures regardless of the device that the text file will be found
file1.seek(0)
print(file1.read())

new_city = input("Add a city to the file: ")
file1.write('\n' + new_city)
file1.close()

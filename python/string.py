myString = 'hamza'
ew = myString.endswith("za")

print(ew)
print('hamza'.zfill(3))


index = 'hamzaahmad ahmad'.find('ahmad')
print(index)

str1 = 'hamzaahmad ahmad'.replace('ahmad', 'khan')
print(str1)


name  = input('DEnter Your Name: ')
print(f'Good Afternoon {name} Sir') # F-String
print('Good Afternoon ' + name +  ' Sir') # Concatenation
print('Good Afternoon',name,'Sir')
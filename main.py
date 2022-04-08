"""
name= input("Hello what\'s is your name?")
birth_year = input("What is your birth year,"+name + "?")
age = (2022 - int(birth_year))
print("Wow, " +name+ "! You look no older than " + str(age-10) + "!")

"""

# "Hello what's your name?" input: Roie
# " What is your birth year, Roie?" input: 1992
# " Wow! you look no older then 19!"

"""
Example 1:
input1 = "Roie"
input2 = "Dobbie"

output:
"Hello,Roie, Your password ****** , is 6 letters long"

Example 2:
input1 = "Nina"
input2 = "Slava"

output:
"Hello,Nina, Your password ***** , is 5 letters long"



"""
"""
username = input("Choose a username")
password = input("what is your password?")
passLen = len(password)
secret = "*" * passLen
print("Hello," +username+ " ,your password " +secret+ " ,is " +str(passLen)+ " letters long")
"""
"""
username = input("Choose a username")
password = input("what is your password?")
passLen = len(password)
secret = "*" * passLen

print(f"Hello, {username}, your password {secret} is {str(passLen)} letters long")
"basket = ["Banana", "Apples", "Oranges", "Blueberries"];
basket.insert(0, 'Apples')
print(basket.count('Apples'))
print(basket)
"print(basket.clear()) "



""
#"print(basket.clear())
#"my_list = [1,2,3,4,5,5]
#my_set = set(my_list)
#print(my_set)

"""
"""is_magician = False
is_expert = True
if is_magician and is_expert:
    print('you are an experted magician')
if is_magician and not is_expert:
    print('at least you are getting there')
if not is_magician:
    print('you need magic powers') """
"""
is_magician = True
is_expert = True
if is_magician:
    if is_expert:
        print('you are an experted magician')
    else:
        print('at least you are getting there')
else:S
    print('you need magic powers')
"""
"""
my_list = [1,2,3,4,5]
counter = 0
for item in my_list:
    counter = counter + item

print(counter)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of 50 is {i}')
        
 i = 0
while i < 50:
    print(i)
    i += 1  
    
    picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
for image in picture:
  for pixel in image:
    if (pixel):
      print('*', end ="")
    else:
      print(' ', end ="")
  print('')     
"""
"""
some_list = ['a', 'b','c','b','d','m','n','n']
duplicates =[]
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
print(duplicates)

"""
"""
my_list = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for item in my_list:
    list_sum = list_sum + item
print(f"my list sum is {list_sum}")
"""
"""
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# Option 1
for line in picture:
    for cell in line:
        if cell == 1:
            print('*',end='')
        elif cell == 0:
            print(' ',end='')
        else:
            print("fuck u")
    print()
"""
"""
# Option 2

#how to access each number in the matrix (iterate over matrix)
#code that cinditions so o = ' ' and 1 = '*'
# how to properly print in the shape wanted
"""
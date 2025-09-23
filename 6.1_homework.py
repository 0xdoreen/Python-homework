# 6.1 使用一个字典来存储一个人的信息，包括 名，姓，年龄和居住城市。该字典应该包括 键 first_name last_name age和city。请编写一个程序,在屏幕上打印该字典的每个值。

person = {
	'first_name': 'John',           
	'last_name': 'Doe',
	'age': 30,      
	'city': 'New York'
}
print(person['first_name'])    
print(person['last_name'])
print(person['age'])
print(person['city'])



# 6.2 喜欢的数 1 使用一个字典来存储一些人喜欢的数。请相处5个人的名字，并将这些名字 用作字典的键。
# 再想出每个人喜欢的一个数，并将这些数作为值存储在字典中。打印每个人的名字和喜欢的数。
# 为了让这个程序更有趣，通过询问朋友确保数据是真实的。

# favorite_numbers 表示字典名，后面使用 {} 来创建字典
# for name, number in favorite_numbers.items() 用于遍历字典中的每个键值对
# f"{name}'s favorite number is {number}." 是格式化字符串，用于输出每个人的名字和喜欢的数
# .items() 方法返回字典中的所有键值对，便于遍历
# for name,number 在定义新的变量，把上面的名字，数字分别赋值给 name,number


favorite_numbers = {
    'Alice': 7,    
    'Bob': 42,
    'Charlie': 3,       
    'Diana': 8,
    'Ethan': 15     
}
for name, number in favorite_numbers.items():
    print (f"{name}'s favorite number is {number}.")         

# 6.3 词汇表 1 想出5个与编程相关的术语，并将这些术语及其含义存储在一个字典中。以整洁的格式打印每个术语及其含义。
# 词汇表 2 修改程序，使其从字典中打印每个术语及其含义。将5个编程术语添加到词汇表中，并确保程序仍然能够正确地打印词汇表中的所有术语。    
vocabulary = {
    'variable': 'A named location used to store data in memory.',
    'function': 'A block of code that performs a specific task and can be reused.',
    'loop': 'A control structure that repeats a block of code as long as a specified condition is true.',
    'list': 'An ordered collection of items that can be of different types.',
    'dictionary': 'A collection of key-value pairs, where each key is unique and maps to a value.'
}
for term, definition in vocabulary.items():
    print(f"{term}: {definition}\n")        

# 6.4 现在你知道了如何遍历字典，请你整理练习 6.3 编写的代码，将其中的一系列函数调用 print() 替换为一个遍历字典中键和值的循环。
# 确保该循环正确无误后，再添加5个编程术语及其含义。当你再次运行这个程序时，这些新术语及其含义也包含在输出中。

vocabulary = {
    'variable': 'A named location used to store data in memory.',
    'function': 'A block of code that performs a specific task and can be reused.',
    'loop': 'A control structure that repeats a block of code as long as a specified condition is true.',
    'list': 'An ordered collection of items that can be of different types.',
    'dictionary': 'A collection of key-value pairs, where each key is unique and maps to a value.',
    'tuple': 'An immutable ordered collection of items.',
    'set': 'An unordered collection of unique items.',
    'class': 'A blueprint for creating objects (a particular data structure).',
    'object': 'An instance of a class.',
    'module': 'A file containing Python definitions and statements.'
}

for term, definition in vocabulary.items():
    print(f"{term}: {definition}\n")


# 6.5 河流。创建一个字典，在其中储存三条河流及其流经的国家。例如，一个简直对可能是'尼罗河': '埃及'。使用循环为每条河流打印一条消息，例如“尼罗河流经埃及”。
# 使用循环将该字典中的每条河流名称打印出来。再使用循环将该字典中的每个国家名称打印出来。

rivers = {
    '尼罗河': '埃及',
    '长江': '中国',
    '亚马逊河': '巴西'
}

# 遍历字典，打印“河流流经国家”
for river, country in rivers.items():
    print(f"{river}流经{country}。")    

#再使用循环将该字典中的每个国家名称打印出来
for country in rivers.values():
    print(country)  

# 6.6 调查 在 6.3.1 节编写的程序中 执行一下操作
# 创建一个应该会接受调查人的名单，其中有些人已经在字典中，而其他人不在字典中。
# 遍历这个名单，对于已参加调查的人，打印一条消息表示感谢；对于还未参与调查的人，打印一条邀请参加调查的消息。

favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'rust',
    'phil': 'python',
}

# 创建应该接受调查的名单
people = ['jen', 'sarah', 'edward', 'phil', 'alice', 'bob']

for person in people:
    if person in favorite_languages:
        print(f"感谢你参加调查，{person.title()}！")
    else:
        print(f"{person.title()}，欢迎来参加我们的编程语言调查！")    
       
# 6.7 人们 在为练习 6.1 编写的程序中，再创建两个表示人的字典，然后江浙三个字典都存储在一个名为 people的列表中。遍历这个列表，为其中的每个人打印其信息。 
person1 = {
    'first_name': 'John',           
    'last_name': 'Doe',
    'age': 30,      
    'city': 'New York'
}       
person2 = {
    'first_name': 'Jane',           
    'last_name': 'Smith',
    'age': 25,      
    'city': 'Los Angeles'
}
person3 = {
    'first_name': 'Alice',              
    'last_name': 'Johnson',
    'age': 28,
    'city': 'Chicago'       
}
people = [person1, person2, person3]
for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")      


# 6.8 宠物。创建多个表示宠物的字典，并将这些字典存储在一个名为 pets的列表中。每个字典都应包含宠物的类型及其主人的名字。遍历这个列表，并将宠物的信息打印出来。
pet1 = {            
    'type': 'dog',           
    'owner': 'Alice'
}   
pet2 = {            
    'type': 'cat',  
    'owner': 'Bob'  
}
pet3 = {
    'type': 'parrot',  
    'owner': 'Charlie'  
}
pets = [pet1, pet2, pet3]
for pet in pets:
    print(f"Pet Type: {pet['type']}")
    print(f"Owner: {pet['owner']}\n")
print()

# 6.9 喜欢的地方。创建一个名为 favorite_places的字典。在这个字典中，将三个人的名字用作键，并存储他们喜欢的地方。
# 对于每个人，至少存储两个喜欢的地方。遍历这个字典，并将每个人的名字及其喜欢的地方打印出来。
favorite_places = {
    'Alice': ['Paris', 'New York'],
    'Bob': ['Tokyo', 'Sydney'],
    'Charlie': ['London', 'Rome']
}
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are:")
    for place in places:
        print(f"- {place}")
# print() 打印空行
    print()

# 6.10 喜欢的数字。修改为练习 6.2 编写的程序，使每个人可以有多个喜欢的数字。至少为其中一个人指定三个喜欢的数字。打印每个人的名字及其喜欢的数字。
favorite_numbers = {
    'Alice': [7, 14, 21],    
    'Bob': [42, 56],
    'Charlie': [3, 6, 9],       
    'Diana': [8, 16],
    'Ethan': [15, 30]     
}   
for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
    print()

# 6.11 城市。创建一个名为 cities的字典，其中包含三个城市作为键。对于每个城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 遍历这个字典，并将每个城市及其信息打印出来。
cities = {
    'New York': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'Known as the "Big Apple".'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Famous for its cherry blossoms.'
    },
    'Paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Home to the Eiffel Tower.'
    }
}       
for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}\n")

# 6.12 扩展 6.11 中编写的程序，在每个城市的字典中添加一个名为 landmarks的键，并将一些著名的地标存储在该键中。遍历这个字典，并将每个城市及其信息打印出来，包括地标。
cities = {  
    'New York': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'Known as the "Big Apple".',
        'landmarks': ['Statue of Liberty', 'Central Park', 'Times Square']
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '14 million',
        'fact': 'Famous for its cherry blossoms.',
        'landmarks': ['Tokyo Tower', 'Shibuya Crossing', 'Meiji Shrine']
    },
    'Paris': {
        'country': 'France',
        'population': '2.1 million',
        'fact': 'Home to the Eiffel Tower.',
        'landmarks': ['Eiffel Tower', 'Louvre Museum', 'Notre-Dame Cathedral']
    }
}       
for city, info in cities.items():
    print(f"City: {city}")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
    print("Landmarks:")
    for landmark in info['landmarks']:
        print(f"- {landmark}")
    print()     






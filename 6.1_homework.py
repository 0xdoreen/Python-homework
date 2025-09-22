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




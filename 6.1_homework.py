# 使用一个字典来存储一个人的信息，包括 名，姓，年龄和居住城市。该字典应该包括 键 first_name last_name age和city。请编写一个程序,在屏幕上打印该字典的每个值。

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


# 创建一个字典，包含三个人的名字作为键，以及他们喜欢的编程语言作为值。为每个人选择一种不同的编程语言，并将其存储在字典中。然后，遍历该字典，并打印每个人的名字和他们喜欢的编程语言。
favorite_languages = {
    'Alice': 'Python',
    'Bob': 'JavaScript',
    'Charlie': 'Java'
}   
for name, language in favorite_languages.items():
    print(f"{name}'s favorite programming language is {language}.") 



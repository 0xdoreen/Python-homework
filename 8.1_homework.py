#8.1
def display_message():
    print("本章的主题是什么？")

display_message()

#8.2
def favorite_book(title):
    print(f"我最喜欢的书是《{title}》。")
favorite_book("One of my favorite books is Alice in Wonderland")

#8.3
def make_shirt(size, text):
    print(f"这件T恤的尺寸是{size}，上面的文字是：'{text}'") 
make_shirt("L", "Hello World")
make_shirt(size="M", text="Python is awesome")  

#8.4
def make_shirt(size="L", text="I love Python"):
    print(f"这件T恤的尺寸是{size}，上面的文字是：'{text}'")     
make_shirt()
make_shirt(size="M")    
make_shirt(size="S", text="Coding is fun")
make_shirt(text="Custom text")
#8.5
def describe_city(city, country="China"):
    print(f"{city} is in {country}.")       
describe_city("Beijing")
describe_city("Shanghai")
describe_city("New York", "USA")

#8.3.1 例子
def get_formatted_name(first_name,last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()    
musician = get_formatted_name("jimi", "hendrix")
print(musician)

"""
return 的作用：

return 用于把函数的结果“返回”给调用者。
当你调用 get_formatted_name("jimi", "hendrix") 时，函数内部会执行：
拼接字符串得到 "jimi hendrix"
用 .title() 方法变成 "Jimi Hendrix"
return 把这个结果返回出去
于是 musician 变量就得到了 "Jimi Hendrix" 这个值。
总结：
return 就是把函数处理后的结果传递出来，方便后续使用。
return 是把函数的结果返回到函数调用的地方。

在你的代码里：
这里调用了 get_formatted_name 函数，return 返回的值就赋给了变量 musician。
所以 "Jimi Hendrix" 这个字符串被“返回”到 musician 变量里，后面你可以用 print(musician) 输出它。

总结：
return 把结果传递给函数调用的位置（比如变量、表达式等）。·


#8.6 
def city_country(city, country):
    full_name = f"{city}, {country}"
    return f"{city}, {country}"

while True:
    print("请输入城市和国家（输入 'q' 退出）：")
    city = input("城市：")
    if city.lower() == 'q':
        break
    country = input("国家：")
    if country.lower() == 'q':
        break
    formatted_name = city_country(city, country)
    print(f"格式化的名称是：{formatted_name}")

#8.7
def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album    
album1 = make_album("Taylor Swift", "1989")
album2 = make_album("Adele", "25", tracks=11)
album3 = make_album("Ed Sheeran", "Divide", tracks=12)
print(album1)
print(album2)
print(album3)   

#8.8
def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album        
while True:
    print("请输入歌手和专辑名称（输入 'q' 退出）：")
    artist = input("歌手：")
    if artist.lower() == 'q':
        break
    title = input("专辑名称：")
    if title.lower() == 'q':
        break
    album = make_album(artist, title)
    print(f"创建的专辑信息：{album}")   
"""
#8.9
def show_messages(messages):
    for message in messages:
        print(message)  
messages = ["Hello, world!", "Python is great.", "Let's learn functions."]
show_messages(messages) 

#8.10
def show_messages(messages):
    for message in messages:
        print(message)  
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"正在发送消息: {current_message}")
        sent_messages.append(current_message)
messages = ["Hello, world!", "Python is great.", "Let's learn functions."]
sent_messages = []
send_messages(messages[:], sent_messages)  # 传递 messages 的副本
print("\n所有消息都已发送。")
print("已发送的消息：")
show_messages(sent_messages)

"""
当然可以！
如果你不希望函数修改原列表，可以在调用函数时传递列表的副本（用 [:]），这样函数操作的是副本，原列表不会被改变。

下面是一个简单例子：

def remove_first_item(my_list):
    # 删除列表第一个元素
    my_list.pop(0)
    print("函数内部处理后的列表：", my_list)

numbers = [1, 2, 3, 4]
remove_first_item(numbers[:])  # 传递副本，不影响原列表
print("原列表：", numbers)

输出结果：

函数内部处理后的列表： [2, 3, 4]
原列表： [1, 2, 3, 4]


这样，原列表 numbers 保持不变。
"""

#8.11
def show_messages(messages):
    for message in messages:
        print(message)  
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"正在发送消息: {current_message}")
        sent_messages.append(current_message)
messages = ["Hello, world!", "Python is great.", "Let's learn functions."]
sent_messages = []
send_messages(messages[:], sent_messages)  # 传递 messages 的副本
print("\n所有消息都已发送。")
print("已发送的消息：")
show_messages(sent_messages)


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

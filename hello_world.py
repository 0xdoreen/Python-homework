print(5+3)
print(9-1)
print(2*4)
print(16/2)
print(2**3)
print(10 % 3)
print(15 // 4)          
message = "Hello, World!"
print(message)
print(message.lower())  
# 3.1 作业
names = ["Alice", "Bob", "Charlie"]
print(names[0])  # Alice
print(names[1])  # Bob
print(names[2])  # Charlie
print(names[-1])        # Charlie   
print(names[-2])        # Bob
print(names[-3])        # Alice
print(names[1:3])      # ['Bob', 'Charlie']
print(names[0:2])           # ['Alice', 'Bob']
print(names[1:])      # ['Bob', 'Charlie']
print(names[:2])       # ['Alice', 'Bob']       
print(names[1:3])      # ['Bob', 'Charlie']
print(names[0:3])      # ['Alice', 'Bob', 'Charlie']
print(names[0:])  # ['Alice', 'Bob', 'Charlie']
print(names[:])  # ['Alice', 'Bob', 'Charlie']
print(names[-2:])  # ['Bob', 'Charlie']
print(names[-3:])   # ['Alice', 'Bob', 'Charlie']
print(names[-2:-1])  # ['Bob']
print(names[-3:-1]) # ['Alice', 'Bob']          
print(names[-3:-2])  # ['Alice']
print(names[-1:-2])  # []
print(names[-1:-3])  # []
print(names[-3:-4])  # []
print(names[-4:-1])  # []
print(names[-4:])  # []
message = f"Hello, {names[0]} and {names[1]}!"
print(message)  
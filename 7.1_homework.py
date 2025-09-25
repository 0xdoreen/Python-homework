"""
# 7.1 汽车租赁 编写一个程序，询问用户要租赁什么样的汽车。根据用户的回答打印一条消息，“Let me see if I can find you a Subaru”
car = input("你想租赁什么样的汽车？")
print(f"Let me see if I can find you a {car}.") 

# 7.2 餐馆订位 编写一个程序，询问用户有多少人用餐。如果用餐人数超过8人，打印一条消息，说明没有空桌；否则指出有空位。
num = int(input("你有多少人用餐？")) # int() 用于类型转换，把字符串变成整数。
if num > 8:
    print("对不起，没有空桌。")     
else:
    print("有空位。请跟我来。23")   

# 7.3  10 的整数倍 让用户输入一个数，并指出这个数是否是 10 的整数倍。
num = int(input("请输入一个数："))
if num % 10 == 0:   
    print(f"{num} 是 10 的整数倍。")
else:
    print(f"{num} 不是 10 的整数倍。")      

#7.4 比萨配料，编写一个循环，提示用户输入一系列比萨配料，直到用户输入 'quit'为止。每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。
prompt = "请输入一种比萨配料（输入 'quit' 结束）：" 
while True:
    topping = input(prompt)
    if topping.lower() == 'quit':  # 使用 lower() 方法忽略大小写
        break
    print(f"好的，我们会在您的比萨AA中添加 {topping}。")

# 7.5 电影票 有家电影院根据观众的年龄收取不同的票价：不到 3岁的关注免费，3~12岁的观众（包含3岁）票价为 10 美元，超过 12岁的观众票价为 15 美元。
# 编写一个循环，询问用户的年龄，并指出其票价。每次运行这个程序时，都应允许用户输入不同的年龄值，直到用户输入 'quit' 为止。

while True:
    age = input("请输入您的年龄（输入 'quit' 结束）：")
    if age.lower() == 'quit':  # 使用 lower() 方法忽略大小写
        break
    age = int(age)  # 将输入的年龄转换为整数
    if age < 3:
        price = 0
    elif 3 <= age <= 12:
        price = 10
    else:
        price = 15
    print(f"您好，您的票价是 {price} 美元。")
"""

#后面不再打印题目内容，只写题目编号。因为 VS code 会自动补全所有的代码。
#加油吧，少年！

#7.6 使用第一种方式 在 While 循环中使用条件测试来结束循环 完成 7.4
prompt = "请输入一种比萨配料（输入 'quit' 结束）：" 
topping = ""  # 初始化变量  
while topping.lower() != 'quit':  # 使用条件测试来结束循环
    topping = input(prompt)
    if topping.lower() != 'quit':  # 避免在输入 'quit' 时打印消息
        print(f"好的，我们会在您的比萨中添加 {topping}。")  

        


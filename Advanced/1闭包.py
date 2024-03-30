# 定义双层嵌套函数 内部函数可以使用外部变量的值
# 使用闭包实现ATM nonlocal关键字在内层函数修改外部变量
def account_create(init_money=0):
    def ATM(num,deposit=True): # 默认为存款
        nonlocal init_money
        if deposit:
            init_money+=num
            print(f"存款{num}")
            print(f"当前余额是{init_money}")
        else:
            if num>init_money:
                print("余额不足")
            else:
                init_money-=num
                print(f"取款{num}")
                print(f"当前余额是{init_money}")

    return ATM
my_count=account_create(200)
my_count(100)
my_count(10,False)
my_count(100)


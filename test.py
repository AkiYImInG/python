import random #载入模块 随机
Qiu = random.randint(0,10) #给Qiu赋值0-10随机整数
print('----猜个数？----')
#想要使用变量需要先赋值才能使用
az=input("这个数是？：")
za=int(az)
time=0
if za==Qiu:  
        print("答对啦！")
        print("摩拉+4（并没有")
else:
        time=time+1
        print("啊这，这也能错的嘛")
        if za>Qiu: 
            print('大了')
        else:    
            print('小了')

while (za !=Qiu) and (time<3):  #while 条件为True执行的操作 ，za不等于4时为True就继续循环直到错误（False）
    
    az=input("再给你一次机会，这数是？：") #给变量az赋值 可以输入？
    za=int(az) #int（int只能检测整数）检测玩家在az输入的整数 并赋予za

    if za==Qiu:  #if 条件为True执行的操作 ，如果za等于4 就触发if下面两行打印
        print("答对啦！")
        print("摩拉+4（并没有")

    else:      #else 条件为False执行的操作 ， 不等于4就触发下面一行打印
        time=time+1
        print("啊这，这也能错的嘛")
        if za>Qiu: #如果触发上面的else就继续if，检测数字大于玩家输入的就反应
            print('大了')
        else:    #不大于4就反应
            print('小了')
while (za !=Qiu) and (time<4):  #while 条件为True执行的操作 ，za不等于4时为True就继续循环直到错误（False）
    
    az=input("最后一次机会，这数是？？？？：") #给变量az赋值 可以输入？
    za=int(az) #int（int只能检测整数）检测玩家在az输入的整数 并赋予za

    if za==Qiu:  #if 条件为True执行的操作 ，如果za等于4 就触发if下面两行打印
        print("答对啦！")
        print("摩拉+4（并没有")

    else:      #else 条件为False执行的操作 ， 不等于4就触发下面一行打印
        time=time+1
        print("啊这，这也能错的嘛")
        if za>Qiu: #如果触发上面的else就继续if，检测数字大于玩家输入的就反应
            print('大了')
        else:    #不大于4就反应
            print('小了')
if time==4:
    print('你是真的菜')
print("你原神今天没签到")

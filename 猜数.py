import random #载入模块 随机
游戏=0
while 游戏==0: #‘游戏’为0时一直循环以下代码
                Qiu = random.randint(0,10) #给Qiu赋值0-10随机整数（可自由更改数字
                print('----猜个数？----')
                #想要使用变量需要先赋值才能使用
                输入=input("这个数是？：")    #输入数字
                数字=int(输入)                #检测“输入”的数字
                time=0                        #计数器 从零开始
                if 数字==Qiu:  
                        print("答对啦！")
                        print("您就是欧皇？")
                else:
                        time=time+1
                        if 数字>Qiu: 
                            print('大了,谁第一次猜的中啊，又不是欧皇对吧')
                        else:    
                            print('小了,谁第一次猜的中啊，又不是欧皇对吧')

                while (数字  !=Qiu) and (time<2):  #while 条件为True执行的操作 ，‘数字’不等于‘Qiu’时为True就继续循环直到错误（False）
                    
                    输入=input("给你一次机会，这数是？：") #给变量‘输入’赋值 使其可以存储字符
                    数字=int(输入) #int（int只能检测整数）检测玩家在‘输入’输入的整数 并赋予给‘数字’

                    if 数字==Qiu:  #if 条件为True执行的操作 ，如果‘数字’等于‘Qiu’ 就触发if下面两行打印
                        print("答对啦！")
                        print("牛啊")

                    else:      #else 条件为False执行的操作 ， 不等于‘Qiu’触发下面一行打印
                        time=time+1
                        if 数字>Qiu: #如果触发上面的else就继续if，检测数字大于玩家输入的就反应
                            print('错了，数大了')
                        else:    #不大于‘Qiu’就反应
                            print('错了，数小了')

                while (数字  !=Qiu) and (time<3):  #while 条件为True执行的操作 ，‘数字’不等于‘Qiu’时为True就继续循环直到错误（False）
                    
                    输入=input("再给你一次机会，这数是？：") #给变量‘输入’赋值 使其可以存储字符
                    数字=int(输入) #int（int只能检测整数）检测玩家在‘输入’输入的整数 并赋予给‘数字’

                    if 数字==Qiu:  #if 条件为True执行的操作 ，如果‘数字’等于‘Qiu’ 就触发if下面两行打印
                        print("答对啦！")

                    else:      #else 条件为False执行的操作 ， 不等于‘Qiu’触发下面一行打印
                        time=time+1
                        if 数字>Qiu: #如果触发上面的else就继续if，检测数字大于玩家输入的就反应
                            print('又错了，数大了')
                        else:    #不大于‘Qiu’就反应
                            print('又错了，数小了')
                while (数字 !=Qiu) and (time<4):  #while 条件为True执行的操作 ，‘数字’不等于‘Qiu’时为True就继续循环直到错误（False）
                    
                    输入=input("最后一次机会，这数是？？？？：") #给变量‘输入’赋值 使其可以存储字符
                    数字=int(输入) #int（int只能检测整数）检测玩家在‘输入’输入的整数 并赋予给‘数字’

                    if 数字==Qiu:  #if 条件为True执行的操作 ，如果‘数字’等于‘Qiu’ 就触发if下面两行打印
                        print("答对啦！")
                        print("极限呀")

                    else:      #else 条件为False执行的操作 ， 不等于‘Qiu’就触发下面一行打印
                        print("啊这，数字是",Qiu,"这还能错的嘛")
                        time=time+1 #增加计数器
                        #time==4 #计数器 每次错误时计数器+1，当达到4时触发下面的打印（可自由更改数字{该条已抛弃}
                        print('你是真的菜')

        
                继续=input("再玩一次？0（继续）/1（不玩了）：")
                游戏=int(继续)
                if 游戏==1:
                    print("游戏结束")

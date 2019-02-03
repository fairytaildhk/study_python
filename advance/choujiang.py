# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 17:36
# @Author  : huangkaiding

# 抽奖  面向对象版本
import tkinter
import time
import threading


class choujiang:
    # 初始化魔术方法
    def __init__(self):
        # 准备好界面
        self.root = tkinter.Tk()
        self.root.title('谁去拿饭票')
        self.root.minsize(500, 500)
        # 声明一个是否按下开始的变量
        self.isloop = False
        self.newloop = False
        # 调用设置界面的方法
        self.setwindow()
        self.root.mainloop()

    # 界面布局方法
    def setwindow(self):
        # 开始停止按钮
        self.btn_start = tkinter.Button(self.root, text='start/stop', command=self.newtask)
        self.btn_start.place(x=200, y=125, width=100, height=50)

        self.btn1 = tkinter.Button(self.root, text='luka', bg='red')
        self.btn1.place(x=20, y=20, width=100, height=50)

        self.btn2 = tkinter.Button(self.root, text='zhangqi', bg='white')
        self.btn2.place(x=140, y=20, width=100, height=50)

        self.btn3 = tkinter.Button(self.root, text='zhangbincheng', bg='white')
        self.btn3.place(x=260, y=20, width=100, height=50)

        self.btn4 = tkinter.Button(self.root, text='chenzhulei', bg='white')
        self.btn4.place(x=380, y=20, width=100, height=50)


        # # 将所有选项组成列表
        self.girlfrends = [self.btn1, self.btn2, self.btn3, self.btn4, ]

    def rounds(self):
        # 判断是否开始循环
        if self.isloop == True:
            return

        # 初始化计数  变量
        i = 0
        # 死循环
        while True:
            if self.newloop == True:
                self.newloop = False
                return

            # 延时操作
            time.sleep(0.1)
            # 将所有的组件背景变为白色
            for x in self.girlfrends:
                x['bg'] = 'white'

            # 将当前数值对应的组件变色
            self.girlfrends[i]['bg'] = 'red'
            # 变量+1
            i += 1
            # 如果i大于最大索引直接归零
            if i >= len(self.girlfrends):
                i = 0

    # 建立一个新线程的函数
    def newtask(self):
        if self.isloop == False:
            # 建立线程
            t = threading.Thread(target=self.rounds)
            # 开启线程运行
            t.start()
            # 设置循环开始标志
            self.isloop = True
        elif self.isloop == True:
            self.isloop = False
            self.newloop = True

if __name__ == '__main__':
    choujiang().setwindow()
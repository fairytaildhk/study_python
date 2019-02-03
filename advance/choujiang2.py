# -*- coding: utf-8 -*-
# @Time    : 2019/1/24 17:38
# @Author  : huangkaiding
import tkinter
import tkinter.messagebox

#导入线性模块
import threading
#导入时间模块
import time
class LuckAward:


    #初始化对象
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('水果幸运大转盘')
        self.root.minsize(600, 600)
        self.root['bg'] = 'cyan'

        #设置布局
        self.pack_labels()
        # 将所有标签组件组成一个列表
        self.label_lists = [self.label11, self.label12, self.label13, self.label14, self.label24, self.label34, self.label44, self.label43, self.label42, self.label41,self.label31, self.label21]
        #初始化开始循环状态的值
        self.isrotate = False
        #是否终止转盘的值
        self.stop_run_sign = False
        #设置初始化列表索引值
        self.i = 0

        self.root.mainloop()
    #设置抽奖程序布局
    def pack_labels(self):
        #设置图片
        self.bm1 = tkinter.PhotoImage(file='./image/apple.png')
        self.bm2 = tkinter.PhotoImage(file='./image/buluo.png')
        self.bm3 = tkinter.PhotoImage(file='./image/putao.png')
        self.bm4 = tkinter.PhotoImage(file='./image/xigua.png')
        self.bm5 = tkinter.PhotoImage(file='./image/yingtao.png')
        self.bm6 = tkinter.PhotoImage(file='./image/mitao.png')
        self.bm7 = tkinter.PhotoImage(file='./image/caomei.png')
        self.bm8 = tkinter.PhotoImage(file='./image/shiliu.png')
        self.bm9 = tkinter.PhotoImage(file='./image/xiangjiao.png')
        self.bm10 = tkinter.PhotoImage(file='./image/chengzi.png')
        self.bm11 = tkinter.PhotoImage(file='./image/mangguo.png')
        self.bm12 = tkinter.PhotoImage(file='./image/mugua.png')

        self.label11 = tkinter.Label(self.root,text='苹果', bg='white',image = self.bm1)
        self.label11.place(relx=0.08, rely=0.08, relwidth=0.15, relheight=0.15)

        self.label12 = tkinter.Label(self.root,text='菠萝', bg='white',image = self.bm2)
        self.label12.place(relx=0.31, rely=0.08, relwidth=0.15, relheight=0.15)

        self.label13 = tkinter.Label(self.root,text='葡萄', bg='white',image = self.bm3)
        self.label13.place(relx=0.54, rely=0.08, relwidth=0.15, relheight=0.15)

        self.label14 = tkinter.Label(self.root,text='西瓜', bg='white',image = self.bm4)
        self.label14.place(relx=0.77, rely=0.08, relwidth=0.15, relheight=0.15)

        self.label21 = tkinter.Label(self.root,text='樱桃', bg='white',image = self.bm5)
        self.label21.place(relx=0.08, rely=0.31, relwidth=0.15, relheight=0.15)

        self.label24 = tkinter.Label(self.root,text='蜜桃', bg='white',image = self.bm6)
        self.label24.place(relx=0.77, rely=0.31, relwidth=0.15, relheight=0.15)

        self.label31 = tkinter.Label(self.root,text='草莓', bg='white',image = self.bm7)
        self.label31.place(relx=0.08, rely=0.54, relwidth=0.15, relheight=0.15)

        self.label34 = tkinter.Label(self.root,text='石榴', bg='white',image = self.bm8)
        self.label34.place(relx=0.77, rely=0.54, relwidth=0.15, relheight=0.15)

        self.label41 = tkinter.Label(self.root,text='香蕉', bg='white',image = self.bm9)
        self.label41.place(relx=0.08, rely=0.77, relwidth=0.15, relheight=0.15)

        self.label42 = tkinter.Label(self.root,text='橙子', bg='white',image = self.bm10)
        self.label42.place(relx=0.31, rely=0.77, relwidth=0.15, relheight=0.15)

        self.label43 = tkinter.Label(self.root,text='芒果', bg='white',image = self.bm11)
        self.label43.place(relx=0.54, rely=0.77, relwidth=0.15, relheight=0.15)

        self.label44 = tkinter.Label(self.root,text='木瓜', bg='white',image = self.bm12)
        self.label44.place(relx=0.77, rely=0.77, relwidth=0.15, relheight=0.15)

        #摆放开始/停止按钮组件
        self.btn1 = tkinter.Button(self.root,text='Start', bg='green', font=('黑体', 20), command=self.new_threading)
        self.btn1.place(relx=0.26, rely=0.40, relwidth=0.2, relheight=0.15)

        self.btn2 = tkinter.Button(self.root,text='Stop', bg='red', font=('黑体', 20), command=self.stop)
        self.btn2.place(relx=0.54, rely=0.40, relwidth=0.2, relheight=0.15)

    def start_run(self):

        #判断循环是否开始
        if self.isrotate == True:#已经开始，则不再进行新的循环
            return
        # while 循环遍历label_lists列表,依次将label变为红色
        while True:
            #判断循环开始或是停止
            if self.stop_run_sign:#若是按下停止按钮，退出当前函数
                return
            try:
                # 设置时间间隔
                time.sleep(0.05)
                # 将所有组件变成白色的
                for label in self.label_lists:
                    label['bg'] = 'white'
                # 将当前数值对应的组件变色
                self.label_lists[self.i]['bg'] = 'red'
                # 变量+1
                self.i += 1
                # 如果i大于最大索引，将i值设置为0
                if self.i == len(self.label_lists):
                    self.i = 0
            except:
                print('程序错误，请重新尝试')


    #新建一个线程的函数
    def new_threading(self):
        #设置转盘停止状态的值为False
        self.stop_run_sign = False
        # 建立新线程
        new = threading.Thread(target=self.start_run)
        # 开始运行新的线程
        new.start()
        # 设置循环开始的值
        self.isrotate = True

    #新建一个停止转盘的方法
    def stop(self):
        #设置停止转盘的值
        self.stop_run_sign = True
        #判断循环开始的状态值
        if self.isrotate == False:
            #弹出‘未开始点击结束’的提示信息
            result = tkinter.messagebox.askokcancel(title = '提示框',message = '您还没有开始抽奖,是否开始抽奖?')
            if result == True:
                self.new_threading()
            else:
                tkinter.messagebox.showinfo(title='提示框', message='您已取消抽奖,欢迎下次使用！')
        #已开始抽奖，按下结束键
        else:
            tkinter.messagebox.showinfo(title='提示信息', message='恭喜您，您抽中了：' + self.label_lists[self.i]['text'])
            # 设置循环状态的值
            self.isrotate = False



if __name__ == '__main__':
    LuckAward().start_run()
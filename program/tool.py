from tkinter import *
import hashlib
import time
import json
import urllib.parse

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name


    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("文本处理工具_v1.0")           #窗口名
        #self.init_window_name.geometry('320x160+10+10')                         #290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+10+10')
        #self.init_window_name["bg"] = "pink"                                    #窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        #self.init_window_name.attributes("-alpha",0.9)                          #虚化，值越小虚化程度越高
        #标签
        self.init_data_label = Label(self.init_window_name, text="待处理数据")
        self.init_data_label.grid(row=0, column=0)
        self.result_data_label = Label(self.init_window_name, text="输出结果")
        self.result_data_label.grid(row=0, column=12)
        self.log_label = Label(self.init_window_name, text="日志")
        self.log_label.grid(row=12, column=0)
        #文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  #原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=65, height=49)  #处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        #按钮
        self.str_trans_to_md5_button = Button(self.init_window_name, text="字符串转MD5", bg="lightblue", width=15,command=self.str_trans_to_md5)  # 调用内部方法  加()为直接调用
        self.str_trans_to_md5_button.grid(row=1, column=11)
        self.str_trans_to_md5_button2 = Button(self.init_window_name, text="Json格式化", bg="lightblue", width=15,command=self.json_format) 
        self.str_trans_to_md5_button2.grid(row=2, column=11)
        self.str_trans_to_md5_button3 = Button(self.init_window_name, text="Json转字符串", bg="lightblue", width=15,command=self.json_inverse_format)  
        self.str_trans_to_md5_button3.grid(row=3, column=11)
        self.str_trans_to_md5_button4 = Button(self.init_window_name, text="urlencode编码", bg="lightblue", width=15,command=self.urlencode)
        self.str_trans_to_md5_button4.grid(row=4, column=11)
        self.str_trans_to_md5_button4 = Button(self.init_window_name, text="urldecode解码", bg="lightblue", width=15,command=self.urldecode)
        self.str_trans_to_md5_button4.grid(row=5, column=11)
        


    #功能函数
    def str_trans_to_md5(self):
        src = self.init_data_Text.get(1.0,END).strip().replace("\n","").encode()
        #print("src =",src)
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                #print(myMd5_Digest)
                #输出到界面
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,myMd5_Digest)
                self.write_log_to_Text("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0,END)
                self.result_data_Text.insert(1.0,"字符串转MD5失败")
        else:
            self.write_log_to_Text("ERROR:str_trans_to_md5 failed")
    def json_format(self):
        try:
            self.result_data_Text.delete(1.0,END)
            ltext = self.init_data_Text.get(0.0,END)
            data = json.dumps(json.loads(ltext),sort_keys=True,indent=2)
            self.result_data_Text.insert(1.0,data)
            self.write_log_to_Text("INFO:json_format success")
        except Exception as ex:
            self.result_data_Text.delete(1.0,END)
            self.write_log_to_Text(ex.msg)
    def json_inverse_format(self):
        self.result_data_Text.delete(1.0,END)
        ltext = self.init_data_Text.get(0.0,END)
        # 无奈之举
        # data = json.dumps(ltext,ensure_ascii=False,separators=(',',':'))
        data = ltext.replace("\n", "").replace("\t", "").replace(" ", "")
        self.result_data_Text.insert(1.0,data)
        self.write_log_to_Text("INFO:json_inverse_format success")
    def urlencode(self):
        self.result_data_Text.delete(1.0,END)
        ltext = self.init_data_Text.get(0.0,END)
        data = urllib.parse.quote(ltext)
        self.result_data_Text.insert(1.0,data)
        self.write_log_to_Text("INFO:urlencode success")
    def urldecode(self):
        self.result_data_Text.delete(1.0,END)
        ltext = self.init_data_Text.get(0.0,END)
        self.result_data_Text.insert(1.0,urllib.parse.unquote(ltext))
        self.write_log_to_Text("INFO:urldecode success")
        

    #获取当前时间
    def get_current_time(self):
        current_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        return current_time


    #日志动态打印
    def write_log_to_Text(self,logmsg):
        global LOG_LINE_NUM
        current_time = self.get_current_time()
        logmsg_in = str(current_time) +" " + str(logmsg) + "\n"      #换行
        
        self.log_data_Text.tag_add("tagblue","1.0")
        self.log_data_Text.tag_config("tagblue",foreground='blue')
    
        self.log_data_Text.tag_add("tagred","1.0")
        self.log_data_Text.tag_config("tagred",foreground='red')
        if LOG_LINE_NUM <= 7:
            if logmsg and logmsg.find("success")>=0:
                self.log_data_Text.insert(END, logmsg_in, "tagblue")
            else:
                self.log_data_Text.insert(END, logmsg_in, "tagred")
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0,2.0)
            if logmsg and logmsg.find("success")>=0:
                self.log_data_Text.insert(END, logmsg_in, "tagblue")
            else:
                self.log_data_Text.insert(END, logmsg_in, "tagred")


def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示


gui_start()
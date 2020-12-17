
from MyQr import myqr  #导入库
myqr.run（
    words = 'the wind of freedom blows',  #这里可以是链接或者字符串，不能是中文
    version=5,  # 容错率大小
    level='H',  # 纠错水平（L、M、Q、H）从小到大
    picture = r'C:\\Users\\Desktop\\pic.png', #可以是gif
    colorrized = True,   #是否是彩色
    contrast=1.0,    # 图片的对比度，默认为1.0。
    brightness=1.0,  # 图片的亮度，默认为1.0。
    save_name='cepit.png',  # 控制输出文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    save_dir=r'存放的位置',# 图片存储位置
）
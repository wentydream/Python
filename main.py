import crack, scan


# 主函数
def main():
    # 退出标致
    exit_flag = 0
    # 目标编号
    target_num = -1
    while not exit_flag:

        try:
            print('WiFi万能钥匙'.center(35, '-'))

            # 调用扫描模块，返回一个排序后的wifi列表
            wifi_list = scan.wifi_scan()

            # 让用户选择要破解的wifi编号，并对用户输入的编号进行判断和异常处理
            choose_exit_flag = 0
            while not choose_exit_flag:
                try:
                    target_num = int(input('请选择你要尝试破解的wifi：'))
                    # 如果要选择的wifi编号在列表内，继续二次判断，否则重新输入
                    if target_num in range(len(wifi_list)):
                        # 二次确认
                        while not choose_exit_flag:
                            try:
                                choose = str(input(f'你选择要破解的WiFi名称是：{wifi_list[target_num][1]}，确定吗？（Y/N）'))
                                # 对用户输入进行小写处理，并判断
                                if choose.lower() == 'y':
                                    choose_exit_flag = 1
                                elif choose.lower() == 'n':
                                    break
                                # 处理用户其它字母输入
                                else:
                                    print('只能输入 Y/N 哦o(*￣︶￣*)o')
                            # 处理用户非字母输入
                            except ValueError:
                                print('只能输入 Y/N 哦o(*￣︶￣*)o')

                        # 退出破解
                        if choose_exit_flag == 1:
                            break
                        else:
                            print('请重新输入哦(*^▽^*)')
                except ValueError:
                    print('只能输入数字哦o(*￣︶￣*)o')
            # 密码破解，传入用户选择的wifi名称
            crack.wifi_password_crack(wifi_list[target_num][1])

            print('-' * 38)
            exit_flag = 1
        except Exception as e:
            print(e)
            raise e


if __name__ == '__main__':
    main()
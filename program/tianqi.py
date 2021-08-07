import requests
# 当天天气预报
rep = (requests.get('https://www.tianqiapi.com/free/day?appid=93511519&appsecret=mwIdNr9z')).json()
print('城市：%s'%rep['city'])
print('天气：%s'%rep['wea'])
print('温度：%s'%rep['tem']+'°C')
print('高温：%s'%rep['tem_day']+'°C')
print('低温：%s'%rep['tem_night']+'°C')
print('风力：%s'%rep['win_speed'])
print('风向：%s'%rep['win'])
print('风速：%s'%rep['win_meter'])
print('风力等级：%s'%rep['win_speed'])
print('空气质量：%s'%rep['air'])
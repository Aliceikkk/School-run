import requests

headers = {
    # 用户的上传token 这是属于JWT加密 分为头部荷载和签名  签名是根据头部和荷载并使用密钥进行生成的 token里面的num要和data中的num统一
    'token': '', 
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'num': '', # 用户ID
    'date': '2023-9-30 18:57:52', # 跑步时间 请严格按照这个格式来设置
    'point': '', # 未知
    'distance': '', # 跑步距离 米为单位
    'duration': '', # 跑步时间 秒为时间
    'step': '', # 步数
    'locations': '', # location也未知
    'calorie': '', # 卡路里
    'tmd': '',  # 步幅？
}

response = requests.post('http://www.changdongli.top:8060/Cs/cs', data=data, headers=headers)

print(response.text)

import requests
import re
from tqdm import tqdm
#编码方法
from urllib.parse import quote
#时间模块
import time
#调用js
import  execjs
js_code = execjs.compile(open('decrypt.js',encoding='utf-8').read())

headers = {
    'accept':'*/*',
    'accept-encoding':'gzip, deflate, br, zstd',
    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'origin':'https://jx.xmflv.cc',
    'priority':'u=1, i',
    'sec-ch-ua':'"Chromium";v="136", "Microsoft Edge";v="136", " Not.A/Brand";v="99"',
    'sec-ch-ua-mobile':'?0',
    'sec-ch-ua-platform':'"macOS"',
    'sec-fetch-dest':'empty',
    'sec-fetch-mode':'cors',
    'sec-fetch-site':'cross-site',
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
}
#视频链接
play_url = 'https://v.qq.com/x/cover/324olz7ilvo2j5f/j0041cnbbod.html'
"""获取m3u8密文"""
link = 'https://59.153.166.174:4433/xmflv.js'
now_time = int(time.time())
key = js_code.call('sign',now_time,quote(play_url))
data = {
    'wap' : '0',
    'url' : quote(play_url),
    'time' : now_time,
    'key' : key,
    'area' : 'CMNET|ZheJiang-111.1.94.202'
}

json_data = requests.post(url = link,data=data ,headers= headers).json()
# 模拟浏览器请求
Mw = json_data['url']
aes_key = json_data['aes_key']
aes_iv = json_data['aes_iv']

m3u8_url = js_code.call('decrypt',Mw,aes_key,aes_iv)
#请求网址
# m3u8_url = "https://apd-vlive.apdcdn.tc.qq.com/defaultts.tc.qq.com/izgRjWeovHmL5rMmtXf3JJTBtJSmR7MzOdpOWek-X_I1UC-Pbk97qEPuseMEupH29U6gfNwYycmpXCtX12kBhO0nZXgLujCogOfGbl_u8-DBB_tl7xR4Ie8oeTBII0OG4DtFK7QpWvdasIgjzUn4yg2kxZjO8ZqTf06Zrh7CKFHrO0bn5nSi7g/gzc_1000102_0b53veaauaaa4yabg7bhcrrmbkodbkxqadsa.f323013.ts.m3u8?ver=4"

# 发送请求
response = requests.get(url=m3u8_url, headers=headers)

m3u8 = response.text

ts_list = re.findall(',\n(.*?)\n#', m3u8)
ts_name = '/'.join(m3u8_url.split('/')[:-1])+ '/'
print(ts_name)
for t in tqdm(ts_list):
    if '.ts' in t:
        ts_url = ts_name + t
        response = requests.get(url=ts_url, headers=headers)
        with open('1.mp4','ab') as f:
            f.write(response.content)
    else:
        response = requests.get(url=t, headers=headers).content
        ts_png = response.find(b'\x47')
        with open('1.mp4','ab') as f:
            f.write(response[ts_png:])
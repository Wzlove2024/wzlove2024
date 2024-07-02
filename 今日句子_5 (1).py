#小程序 今日句子 抓token 变量名jrzj @分割
import requests 
import json 
import time
import random
import os
from urllib.parse import quote
requests.packages.urllib3.disable_warnings()
class yuanshe:
    def __init__(self,cookie):
        self.cookie = cookie
        self.url = "https://api.juzi.co"
        self.header = {
    "Host": "api.juzi.co",
    "Connection": "keep-alive",
    "charset": "utf-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240301 MMWEBID/98 MicroMessenger/8.0.48.2580(0x28003036) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "token": f"{self.cookie}",
    "Referer": "https://servicewechat.com/wx3e3540cb2012ea1f/26/page-frame.html"
}
        self.header2 = {
    "Host": "api.juzi.co",
    "Connection": "keep-alive",
    "Content-Length": "140",
    "charset": "utf-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240301 MMWEBID/98 MicroMessenger/8.0.48.2580(0x28003036) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    "content-type": "application/x-www-form-urlencoded; charset=utf-8",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "token": f"{self.cookie}",
    "Referer": "https://servicewechat.com/wx3e3540cb2012ea1f/26/page-frame.html"
}
    
    def userinfo(self):
        url = f"{self.url}/member/getWalletInfo"
        r = requests.get(url,headers=self.header,timeout=10,verify=False).json()
        if r['code'] == 200:
            print(f"用户信息获取成功")
            print(f"当前余额:{r['data']['member']['money']}")
        else:
            print(f"用户信息获取失败")
            print(r)
        if float(r['data']['member']['money']) >3:
            url = "https://api.juzi.co/member/cashOut"
            data = {"price": "3"}
            r = requests.post(url, headers=self.header, data=data)
            print(f"提现结果：{r.text}")




        
    def get_hitokoto(self):
        url = random.choice(["http://v1.jinrishici.com/all.txt"])
        r = requests.get(url)
        if r.status_code == 200:
            print(r.text)
            return quote(r.text)
        else:
            print(f"请求失败,状态码:{r.status_code}")
            return self.get_hitokoto()
    def submit_hitokoto(self):
        hitokoto = self.get_hitokoto()
        url = f"{self.url}//sentence/repeatedList"
        data = f"juzi={hitokoto}"
        r = requests.post(url,headers=self.header2,data=data).json()
        if r['data']:
            print("重复")
            time.sleep(2)
            return self.submit_hitokoto()
        else:
            print("不重复")
        
        url = f"{self.url}/sentence/execWrite"
        data = f"juzi={hitokoto}&origin=true&write=&source=&tagsValue=&tagslength=&tags="
        r = requests.post(url,headers=self.header2,data=data).json()
        print(r)


    def like(self):
        url = f"{self.url}/index/tab"
        r = requests.get(url,headers=self.header,timeout=10,verify=False).json()
        for i in r['data']['recommend']:
            ii = json.loads(json.dumps(i))
            url = f"{self.url}/sentence/slike"
            data = f"sid=6666616"
            r = requests.post(url,headers=self.header2,data=data,verify=False).json()
            print(r)
            if r['code'] == 200:
                print(f"点赞成功")
                return
            else:
                print(f"点赞失败",r['msg'])
                if "每天只能点赞1次" in r['msg']:
                    print("今天已经点赞过了")
                    return
            time.sleep(random.randint(2,5))

    def main(self):
        self.userinfo()
        print("==========")
        self.submit_hitokoto()
        time.sleep(random.randint(20,40))
        print("==========")
        self.like()
        print("==========")
        self.userinfo()

if __name__ == '__main__':
    #version()
    cookie = ''
    if not cookie:
        cookie = os.getenv("jrzj")
        if not cookie:
            print("请设置环境变量:jrzj")
            exit()
    cookies = cookie.split("@")
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
     print(f"\n--------开始第{i}个账号--------")
     main = yuanshe(cookie)
     main.main()
     print(f"--------第{i}个账号执行完毕--------")
     i += 1

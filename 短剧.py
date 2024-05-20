
#   --------------------------------注释区--------------------------------
#   入口: 微信打开https://woaidjss.wetimetech.com/api/short?md5key=a5e6581d79bf335ffe1269d9c39dba62
#   抓woaidjss.wetimetech.com链接下任意包体的以下值 注意只要值
#   分别是，androidid,authorization,models,oaid,osinfo,tongdunblackbox
#   拼接成cookie 格式是 androidid#authorization#models#oaid#osinfo#tongdunblackbox
#   填入yuanshen_djss 多号@分割
#   --------------------------------一般不动区-------------------------------
#                     _ooOoo_
#                    o8888888o
#                    88" . "88
#                    (| -_- |)
#                     O\ = /O
#                 ____/`---'\____
#               .   ' \\| |// `.
#                / \\||| : |||// \
#              / _||||| -:- |||||- \
#                | | \\\ - /// | |
#              | \_| ''\---/'' | |
#               \ .-\__ `-` ___/-. /
#            ___`. .' /--.--\ `. . __
#         ."" '< `.___\_<|>_/___.' >'"".
#        | | : `- \`.;`\ _ /`;.`/ - ` : | |
#          \ \ `-. \_ __\ /__ _/ .-` / /
#  ======`-.____`-.___\_____/___.-`____.-'======
#                     `=---='
# 
#  .............................................
#           佛祖保佑             永无BUG
#           佛祖镇楼             BUG辟邪
#佛曰:  
#        写字楼里写字间，写字间里程序员；  
#        程序人员写程序，又拿程序换酒钱。  
#        酒醒只在网上坐，酒醉还来网下眠；  
#        酒醉酒醒日复日，网上网下年复年。  
#        但愿老死电脑间，不愿鞠躬老板前；  
#        奔驰宝马贵者趣，公交自行程序员。  
#        别人笑我忒疯癫，我笑自己命太贱；  
#        不见满街漂亮妹，哪个归得程序员？
#
#   --------------------------------代码区--------------------------------

import requests
import json
import random
import os
import time
import hashlib
class yuanshen():
    def __init__(self,cookie) -> None:
        if len(cookie.split("#")) != 6:
            print("cookie格式错误")
            exit()
        self.androidid = cookie.split("#")[0]
        self.authorization = cookie.split("#")[1]
        self.model = cookie.split("#")[2]
        self.oaid = cookie.split("#")[3]
        self.osinfo = cookie.split("#")[4]
        self.tongdunblackbox = cookie.split("#")[5]
        self.h = {
    "Host": "woaidjss.wetimetech.com",
    "androidid": f"{self.androidid}",
    "authorization": f"{self.authorization}",
    "channel": "yaoqing",
    "imei": "",
    "mac": "02:00:00:00:00:00",
    "models": f"{self.model}",
    "oaid": f"{self.oaid}",
    "timestamp": "",
    "v": "1.2.9",
    "sign": "",
    "tongdunblackbox": f"{self.tongdunblackbox}",
    "osversion": "Android13",
    "osinfo": f"{self.osinfo}",
    "content-type": "application/json; charset=UTF-8",
    "content-length": "18",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.7.2"
}
    
    def sign_(self,type=False,check=False):
        if type:
            str_ = f'Authorization={self.authorization}&channel=yaoqing&imei=&mac=02:00:00:00:00:00&models={self.model}&oaid={self.oaid}&timestamp={self.timestamp}&' + '{"ad_price":' + str(self.gold) + ',"ad_type":2}&key=MdKkEZoUZik6'
        elif check:
            str_ = f'Authorization={self.authorization}&channel=yaoqing&imei=&mac=02:00:00:00:00:00&models={self.model}&oaid={self.oaid}&timestamp={self.timestamp}&'+ '{}' +'&key=MdKkEZoUZik6'
        else:
            str_ = f'Authorization={self.authorization}&channel=yaoqing&imei=&mac=02:00:00:00:00:00&models={self.model}&oaid={self.oaid}&timestamp={self.timestamp}&' + '{"ad_price":' + str(self.gold) + '}&key=MdKkEZoUZik6'
        #print(str_)
        md5 = hashlib.md5()
        md5.update(str_.encode('utf-8'))
        return md5.hexdigest()

    def video_bag(self):
        self.before_ad()
        url = "https://woaidjss.wetimetech.com/v1/game/harvestSuperVideo"
        self.timestamp = int(time.time() * 1000)
        random_int = random.randrange(20, 31) * 10
        self.gold = float(random_int)
        print(f"这次我想拿[{self.gold}]金币")
        self.h["timestamp"] = f"{self.timestamp}"
        data = {
            "ad_price": self.gold
        }
        data = json.dumps(data,separators=(',', ':'))
        self.h["sign"] = self.sign_()
        r = requests.post(url, headers=self.h, data=data).json()
        #print(r)
        if r['code'] == 0:
            print(f"🎉视频红包领取成功，余额:[{r['data']['wallet_info']['money_str']}]")
            self.ad_report()
            return True
        else:
            print(f"视频红包领取失败，错误信息:[{r['msg']}]")
            return False
    
    def ad_bag(self):
        self.before_ad()
        url = "https://woaidjss.wetimetech.com/v1/game/harvestSuperVideo"
        self.timestamp = int(time.time() * 1000)
        random_int = random.randrange(28, 33) * 10
        self.gold = float(random_int)
        print(f"这次我想拿[{self.gold}]金币")
        self.h["timestamp"] = f"{self.timestamp}"
        data = {
            "ad_price": self.gold
        }
        data = json.dumps(data,separators=(',', ':'))
        self.h["sign"] = self.sign_()
        r = requests.post(url, headers=self.h, data=data).json()
        #print(r)
        if r['code'] == 0:
            print(f"🎉广告红包领取成功，余额:[{r['data']['wallet_info']['money_str']}]")
            self.ad_report()
            return True
        else:
            print(f"广告红包领取失败，错误信息:[{r['msg']}]")
            return False
        
    def ad_report(self):
        url = "https://woaidjss.wetimetech.com/v1/api/submitArpu"
        self.timestamp = int(time.time() * 1000)
        self.h["timestamp"] = f"{self.timestamp}"
        self.h["sign"] = self.sign_(type=True)
        data = {
            "ad_price": self.gold,
            "ad_type": 2
        }
        data = json.dumps(data,separators=(',', ':'))
        r =requests.post(url, headers=self.h, data=data).json()
        if r['code'] == 0:
            print(f"🔔广告上报成功")
        else:
            print(f"广告上报失败，错误信息:[{r['msg']}]")
            return
    
    def before_ad(self):
        headers ={
    "Host": "woaidjss.wetimetech.com",
    "androidid": f"{self.androidid}",
    "authorization": f"{self.authorization}",
    "channel": "yaoqing",
    "imei": "",
    "mac": "02:00:00:00:00:00",
    "models": f"{self.model}",
    "oaid": f"{self.oaid}",
    "timestamp": "",
    "v": "1.2.9",
    "sign": "",
    "tongdunblackbox": f"{self.tongdunblackbox}",
    "osversion": "Android13",
    "osinfo": f"{self.osinfo}",
    "content-length": "0",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.7.2"
}
        url = "https://woaidjss.wetimetech.com/v1/api/checkVideo"
        self.timestamp = int(time.time() * 1000)
        headers["timestamp"] = f"{self.timestamp}"
        headers["sign"] = self.sign_(check=True)
        r =requests.post(url, headers=headers).json()
        if r['code'] == 0:
            print(f"🔔check广告上报成功")
            time.sleep(random.randint(10, 25))
        else:
            print(f"check广告上报失败，错误信息:[{r['msg']}]")
            return
        
    def main(self):
        print("================视频广告开始================")
        i = 0
        while True:
            if not self.video_bag():
                break
            i +=1
            print ("-------------")
            time.sleep(random.randint(30, 45))
            if i == 3:
                break
        print("================视频广告结束================")
        time.sleep(random.randint(40, 80))
        i = 0
        print("================广告红包开始================")
        while True:
            if not self.ad_bag():
                break
            i +=1
            print ("-------------")
            time.sleep(random.randint(40, 80))
            if i == 10:
                break
        print("================广告红包结束================")
    

if __name__ == '__main__':
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_djss")
        if not cookie:
            print("⛔️请设置环境变量:yuanshen_djss")
            exit()
    cookies = cookie.split("@")#转成列表
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
        print(f"\n--------开始第{i}个账号--------")
        try:
            main = yuanshen(cookie)
            main.main()
        except Exception as e:
            print(f"出现异常,程序退出,异常信息为{e}")
            exit()
        print(f"--------第{i}个账号执行完毕--------")
        time.sleep(20)
        i += 1





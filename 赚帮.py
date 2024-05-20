#   --------------------------------注释&变量区--------------------------------
#   入口 https://app.zhuanbang.net/invite/7079
#   找请求头中NiuToken的值
#  NiuToken=**** 只要**** NiuToken=不要填 NiuToken=不要填 NiuToken=不要填
#   变量名：yuanshen_zb 多号@分割
#   --------------------------------一般不动区--------------------------------
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
import os
import time
import random
import hashlib


class yuanshen():
    def __init__(self,cookie):
        self.cookie = cookie
        self.h = {
    "Host": "app.zhuanbang.net",
    "accept": "application/json, image/webp",
    "user-agent": "Mozilla/5.0 (Linux; Android 12; M2104K10AC Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36 HuoNiuFusion/1.25.0_231652",
    "x-requested-with": "XMLHttpRequest",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://app.zhuanbang.net/assist/activity/47",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "accept-encoding": "gzip",
    "Cookie":f"NiuToken={self.cookie}"
}
    
    def sign_(self):
        d = f"{self.csrftoken}#{self.sessionId}#{self.time}"
        sha1 = hashlib.sha1()
        byte_string = d.encode('utf-8')
        sha1.update(byte_string)
        sign = sha1.hexdigest()
        #print(sign)
        return sign
        
    def video(self,key):
        i = 0
        while True:
            i += 1
            url = f"https://app.zhuanbang.net/{key}/launch?_random={int(time.time() * 1000)}&type=slide"
            #print (url)
            r = requests.get(url,headers=self.h).json()
            if r['code'] == 0:
                print(f"第[{i}]个红包获取信息成功")
                self.csrftoken = r['data']['extArgs']['csrfToken']
                self.sessionId = r['data']['extArgs']['sessionId']
                self.time = int(time.time())
                url = f"https://app.zhuanbang.net/{key}/award/grant?_t={self.time}"
                data = {
        "csrfToken": f"{self.csrftoken}",
        "deviceId": f"{self.sessionId}",
        "timestamp": f"{self.time}",
        "sign": f"{self.sign_()}"}           
                r = requests.post(url,headers=self.h,data=data).json()
                if r['code'] == 0:
                    print(f"第[{i}]个红包领取成功,获得[{r['data']['awardMoney']}]元")
                else:
                    print(f"第[{i}]个红包领取失败---[{r['msg']}]")
                    break
            else:
                print(f"第[{i}]个获取红包信息失败---[{r['msg']}]")
                break
            if i >= 21:
                break
            time.sleep(random.randint(20,48))
    def main(self):
        print("===========开始执行快手刷视频===========")
        self.video("kwai_video")
        print("===========快手刷视频执行完毕===========")
        print("===========开始执行抖音刷视频===========")
        self.video("pangle_video")
        print("===========抖音刷视频执行完毕===========")
            
        
if __name__ == '__main__':
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_zb")
        if not cookie:
            print("⛔️请设置环境变量:yuanshen_zb")
            exit()
    cookies = cookie.split("@")
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
     print(f"\n--------开始第{i}个账号--------")
     main = yuanshen(cookie)
     main.main()
     print(f"--------第{i}个账号执行完毕--------")
     i += 1
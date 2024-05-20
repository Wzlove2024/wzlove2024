
#   --------------------------------注释区--------------------------------
#   入口: http://api.wudei.com/api/v1/views/invite?inviteCode=1007307
#   app内邀请id请填1007307
#   抓authorization参
#   变量: yuanshen_wd 多号： @分割
#   玩法&注意事项：
#   No.1 下载之后先去我的右上角三条杠实名 然后开通至少vip3 成本1.5+3=4.5
#   No.2 具体收益是打赏炫舞币获得福卡（舞卡）然后开舞卡可以得现金提现到支付宝
#   N0.3 可自行决定打赏给谁，被打赏的也可以领取收益，id填脚本内生成的视频id而不是你的用户id
#   No.4 被打赏的用户必须发布有视频，不发视频就算填了id也无法打赏
useridA = "" #多号情况下 第一个用户打赏的用户视频id 不填无法运行
useridB = "" #多号情况下 除第一个用户 剩下用户打赏的用户视频id 不填无法运行
#   单号情况下只需要填useridA 不知道就随便问群友要一个吧
#   如不知道用户视频id是多少 可以先运行一遍脚本 脚本会输出用户视频id
#   推荐两号以上 不然肥水流外人田了
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
import time
import random
import os
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
import base64
import json
import uuid
def des_encrypt(text):
    base64_key = base64.b64encode(b'MjAyMjAz').decode('utf-8')
    key = base64.b64decode(base64_key)
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(text.encode('utf-8'), DES.block_size)
    encrypted_bytes = cipher.encrypt(padded_text)
    encrypted_base64 = base64.b64encode(encrypted_bytes).decode('utf-8')
    return encrypted_base64

class yuanshen():
    def __init__(self,cookie,num):
        self.num = num
        self.cookie = cookie
        self.h = {
    "Host": "api.wudei.com",
    "authorization": f"{self.cookie}",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.9.3"
}
    
    def sign(self):
        url = "https://api.wudei.com/api/v1/icecream/by/friend"
        r = requests.get(url,headers=self.h).json()
        if r['code'] == 200:
            print(f"签到A成功,获得舞币:[{r['dara']}]")
        else:
            print(f"签到A失败---[{r['msg']}]")
        time.sleep(5)
        url = "https://api.wudei.com/api/v1/user/sign"
        r = requests.post(url,headers=self.h).json()
        if r['code'] == 200:
            print(f"签到B成功,获得舞币:[{r['data']}]")
        else:
            print(f"签到B失败---[{r['msg']}]")
    
    def userinfo(self):
        url = "https://api.wudei.com/api/v1/user/asset"
        r = requests.get(url,headers=self.h).json()
        if r['code'] == 200:
            self.corn = r['data']['icecream']
            print(f"用户剩余舞b:[{self.corn}]")
        else:
            print(f"获取舞币失败---[{r['msg']}]")
        
        url = "https://api.wudei.com/api/v1/user/info?userId=&code="
        r = requests.get(url,headers=self.h).json()
        if r['code'] == 200:
            self.userid = r['data']['userId']
            print(f"用户视频ID:[{self.userid}]")
        else:
            print(f"获取视频ID失败---[{r['msg']}]")
        


    def get_card(self,userid):
        if not userid:
            print("请先填写需要打赏的用户ID")
            return
        url = f"https://api.wudei.com/api/v1/reward/{userid}?icecream={self.corn}"
        r = requests.get(url,headers=self.h).json()
        if r['code'] == 200:
            print(f"打赏[{userid}]成功,获得舞卡:[{r['data']}]")
        else:
            print(f"打赏[{userid}]打赏失败---[{r['msg']}]")
        time.sleep(random.randint(5,15))

    def withdrawl_all(self):
        url = "https://api.wudei.com/api/v1/fucard/lottery/all"
        r = requests.post(url,headers=self.h).json()
        if r['code'] == 200:
            print(f"全部舞卡抽奖成功,获得现金:[{r['data']['money']}*{r['data']['additionRate']} = {r['data']['additionMoney']}]元")
        else:
            print(f"全部舞卡抽奖失败---[{r['msg']}]")
        
    def withdraw(self):
        url = "https://api.wudei.com/api/v1/user/asset"
        r = requests.get(url,headers=self.h).json()
        if r['code'] == 200:
            money = float(r['data']['balance'])
            print(f"用户剩余余额:[{r['data']['balance']}]元")
            if money >= 5:
                self.tixian(5)
            elif money >= 1:
                self.tixian(1)
            elif money >= 0.3:
                self.tixian(0.3)
            else:
                print("余额不足,无法提现")
    
    def tixian(self,money):
        url = "https://api.wudei.com/api/v1/withdraw/2"
        rand = uuid.uuid4()
        postdata = {
    "money": f"{money}",
    "rand": f"{rand}"
}
        pj =  json.dumps(postdata,separators=(',', ':'))
        print(pj)
        data = des_encrypt(pj)
        print(data)
        r = requests.post(url,headers=self.h,data=data).json()
        if r['code'] == 200:
            print(f"提现[{money}]成功")
        else:
            print(f"提现失败---[{r['msg']}]")

                

    def main(self):
        self.sign()
        time.sleep(2)
        self.userinfo()
        if int(self.corn) != 0:
            if int(self.num) == 1:
                print(f"当前是第1个账号,对[{useridA}]进行打赏")
                self.get_card(useridA)    
            else:
                print(f"当前是第{self.num}个账号,对[{useridB}]进行打赏")
                self.get_card(useridB)
            self.withdrawl_all()
        time.sleep(2)
        self.withdraw()

        
        

    

if __name__ == '__main__':
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_wd")
        if not cookie:
            print("⛔️请设置环境变量:yuanshen_wd")
            exit()
    cookies = cookie.split("@")#转成列表
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
        print(f"\n--------开始第{i}个账号--------")
        try:
            main = yuanshen(cookie,i)
            main.main()
        except Exception as e:
            print(f"出现异常,程序退出,异常信息为{e}")
            exit()
        print(f"--------第{i}个账号执行完毕--------")
        time.sleep(20)
        i += 1

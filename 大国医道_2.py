#   --------------------------------注释区--------------------------------
#   先注册 每日0.3
#   抓getToken接口中请求体的的wx_openid
#   变量: yuanshen_dgyd 多号： @分割
#   如服务器获取的aid过期(我没起床)，可以填自己链接中的aid参数到yuanshen_aid变量
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
import json
import random
import os
from datetime import datetime
def version():
    print(requests.get("https://gitee.com/HuaJiB/yuanshen34/raw/master/toulu.txt").text)

class yuanshen():
    def __init__(self,cookie):
        self.cookie = cookie
        self.tid = "c6526356cc127852"
        self.get_aid()
        self.h_token  = {
    "Host": "flow.judaapp.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240404 MMWEBID/6484 MicroMessenger/8.0.49.2600(0x2800313B) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    "content-type": "application/json",
    "accept": "*/*",
    "origin": "https://flow.judaapp.com",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": f"https://flow.judaapp.com/api-user/v1/activity?aid={self.aid}&tid={self.tid}&code={self.cookie}&state=STATE",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}
        self.get_token()
        self.h_answer = {
    "Host": "flow.judaapp.com",
    "accept": "application/json",
    "authorization": f"Bearer {self.token}",
    "user-agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36 XWEB/1160117 MMWEBSDK/20240404 MMWEBID/6484 MicroMessenger/8.0.49.2600(0x2800313B) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64",
    "content-type": "application/json",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": f"https://flow.judaapp.com/api-user/v1/activityView?aid={self.aid}&tid={self.tid}",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}

    def get_aid(self):
        today = datetime.today().strftime("%Y-%m-%d")
        print(f"当前日期:[{today}]")
        url = "http://101.132.127.171/api/huaji/txt/aid.txt"
        r = requests.get(url).text.split(",")
        if r[1] != today:
            print("云服务器获取的aid已过期，尝试从本地环境获取")
            self.aid = os.getenv("yuanshen_aid")
            if not self.aid:
                print("本地环境获取的aid为空，退出程序")
                exit()
        else:
            self.aid = r[0]
            print(f"从云服务器获取到aid:[{self.aid}]")

    def get_token(self):
        url = "https://flow.judaapp.com/api-user/v1/getToken"
        data = {
            "wx_openid":f"{self.cookie}",
            "tid":f"{self.tid}",
        }
        r = requests.post(url,headers=self.h_token,json=data).json()
        if r['status_code'] == 200:
            self.token = r['data']['token']
            print(f"获取token成功[{self.token}]")
        else:
            print(f"获取token失败[{r['message']}]")
    
    def watch(self):
        i = 1
        all_second = 0
        while True:
            second = random.uniform(495, 505)#大约500s上报一次
            second = round(second, 2) #2位小数
            all_second =  round(all_second + second, 2)#2位小数
            print(f"上报时间---[{all_second}/{self.videotime}]")
            if all_second >= float(3599.59):
                break
            if i != 1:#如果不是第一次上报 那么就真实休眠
                time.sleep(second)
            url = "https://flow.judaapp.com/api-user/v1/activityWatchVideo"
            data = {
                "userActivityId":f"{self.userid}",
                "second":f"{all_second}",
            }
            r = requests.post(url,headers=self.h_answer,json=data).json()
            print(r)
            if r['status_code'] == 200:
                print(f"上报[{all_second}]成功")
                i += 1
            else:
                print(f"上报[{all_second}]失败")
                break

            if i == 8:
                self.watch_over()
                break
    
    def watch_over(self):
        time.sleep(5)
        url = "https://flow.judaapp.com/api-user/v1/activityWatchVideoOver"
        data = {
            "userActivityId":f"{self.userid}",
        }
        r = requests.post(url,headers=self.h_answer,json=data).json()
        if r['status_code'] == 200:
            print(f"上报完成")
        else:
            print(f"上报完成失败,[{r}]")
                
    def answer(self):
        time.sleep(random.randint(10,20))
        data = {"activity_id":self.activity_id,"answers":self.answer_list}
        data = json.dumps(data)
        print(data)
        url = "https://flow.judaapp.com/api-user/v1/receiveAwardAndWatchOver"
        r = requests.post(url,headers=self.h_answer,data=data).json()
        if r['status_code'] == 200:
            print(f"答题成功,喜提0.3r")
        else:
            print(f"答题失败,[{r}]")
        
    
    def videoinfo(self):
        self.answer_list = []
        url = f"https://flow.judaapp.com/api-user/v1/activityDetatil?ac_code={self.aid}&team_code={self.tid}&withMaterial=1"
        r = requests.get(url,headers=self.h_answer).json()
        if r['status_code'] == 200:
            self.userid = r['meta']['joinInfo']['userActivityId']
            self.videotime = r['meta']['joinInfo']['playTime']
            self.activity_id = r['data']['activity_id']
            print(f"获取userActivityIds成功[{self.userid}] /获取activity_id成功[{self.activity_id}] /本期时间[{self.videotime}]")
            k = json.loads(json.dumps(r["data"]["materialDetail"]["questions"]))
            for index, item in enumerate(k):
                question = item['question']
                answers = item['answer']
                for ans_index, answer in enumerate(answers):
                    if answer['result'] == '1':
                        print(f"题目 {index}: {question}，答案: {answer['item']}，序号: {ans_index}")
                        self.answer_list.append(f"{index}_{ans_index}")
                
            print(f"获取答案成功:{self.answer_list}")
            time.sleep(5)
    
    def main(self):
        self.videoinfo()
        self.watch()
        self.answer()

if __name__ == '__main__':
    version()
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_dgyd")
        if not cookie:
            print("⛔️请设置环境变量:yuanshen_dgyd")
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

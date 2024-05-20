#   --------------------------------注释区--------------------------------
#   入口http://103.225.198.104:5212/s/9lS3 天企.jpg
#   变量:yuanshen_tqhb 多号： @分割
#   找https://app.88888yc.com//appapi/mp.red/red_list的请求体
#   把请求体的所有数据和其他任意接口的uid和token全部填入即可
#   请求体例如：{"page":k,"city_or_nation":2,"city":"","lat":self.lat,"long":self.long,"sort_type":"1","search":""}
#   格式：请求data#token#uid
Max_account = 20 #本次运行领取红包个数
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
import time,random
import os
import json
def version():
    print(requests.get("https://gitee.com/HuaJiB/yuanshen34/raw/master/pubilc.txt").text)

class yuanshen():
    def __init__(self,cookie):
        try:
            self.j = json.loads(cookie.split("#")[0])
        except:
            print("cookie格式错误")
            exit()
        self.cookie = cookie.split("#")[1]
        self.uid  = cookie.split("#")[2]
        self.id_ = []
        self.headers = {
    "Host": "app.88888yc.com",
    "Connection": "keep-alive",
    "charset": "utf-8",
    "User-Agent": "Mozilla/5.0 (Linux; Android 13; 23054RA19C Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/122.0.6261.120 Mobile Safari/537.36 XWEB/1220053 MMWEBSDK/20240404 MMWEBID/98 MicroMessenger/8.0.49.2600(0x28003133) WeChat/arm64 Weixin NetType/5G Language/zh_CN ABI/arm64 MiniProgramEnv/android",
    "content-type": "application/json",
    "Accept-Encoding": "gzip,compress,br,deflate",
    "Referer": "https://servicewechat.com/wx6f66ee5a06451646/31/page-frame.html"
}
    def userinfo(self):
        url = "https://app.88888yc.com//appapi/mp.User/get_info"
        data = {"uid":f"{self.uid}","token":f"{self.cookie}"}
        r = requests.post(url,headers=self.headers,json=data).json()
        if r['code'] == 200:
            print(f"用户[{r['datas']['info']['nickname']}]剩余余额:[{r['datas']['info']['money']}]")
            k = 1
            while True:
                url = "https://app.88888yc.com//appapi/mp.User/get_money_record"
                data = {"uid":f"{self.uid}","token":f"{self.cookie}","page":k}
                r = requests.post(url,headers=self.headers,json=data).json()
                if r['code'] == 200 and r['datas']['list'] != []:
                    print("请求历史数据成功")
                    for i in r['datas']['list']:
                        self.id_.append(i.get('type_id'))
                    k += 1
                    time.sleep(random.randint(1,3))
                else:
                    break
            url = ""
            
        else:
            print(f"用户[{self.uid}]登录失败:[{r['datas']['msg']}]")
            exit()

    def task(self):
        j = 0
        k = 1
        n = 0
        Max_error = 5
        print(f"尝试领取:[{Max_account}]个红包")
        while True:
            url = "https://app.88888yc.com//appapi/mp.red/red_list"
            data = {"page":k,"city_or_nation":2,"city":f"{self.j['city']}","lat":self.j['lat'],"long":self.j['long'],"sort_type":"2","search":""}
            r = requests.post(url,headers=self.headers,json=data).json()
            if r['code'] == 200:
                print(f"红包列表第[{k}]页请求成功")
                for i in r['datas']['list']:
                    self.id = i.get('id')
                    if self.id not in self.id_:
                        if self.red(): 
                            j+=1
                            time.sleep(random.randint(10,65))
                        else:
                            n+=1
                            time.sleep(random.randint(1,5))  
            if n >= Max_error:
                print(f"当前账号[{self.uid}]已达到最大错误次数")
                break
            if j >= Max_account:
                print(f"当前账号[{self.uid}]已达到最大红包数")
                break                     
            k += 1
    def red(self):
        url = "https://app.88888yc.com//appapi/mp.red/red_detail"
        data = {"uid":f"{self.uid}","id":f"{self.id}","lat":f"{self.j['lat']}","long":f"{self.j['long']}"}
        r = requests.post(url,headers=self.headers,json=data).json()
        if r['code'] == 200:
            if r['datas']['info']['else_count'] == 0:
                print(f"ID[{self.id}]红包已被抢完")
                return False
        else:
            print(f"ID[{self.id}]请求失败:[{r['datas']['msg']}]")
        url = "https://app.88888yc.com//appapi/mp.Red/share_update"
        data = {"uid":f"{self.uid}","token":f"{self.cookie}","id":f"{self.id}"}
        r = requests.post(url,headers=self.headers,json=data).json()
        if r['code'] == 200:
            print(f"ID[{self.id}]分享成功:[{r['datas']['msg']}]")
            url = "https://app.88888yc.com//appapi/mp.Red/get_red2"
            data = {"uid":f"{self.uid}","token":f"{self.cookie}","type":"wx","id":f"{self.id}","topic":"red"}
            r = requests.post(url,headers=self.headers,json=data).json()
            if r['code'] == 200:
                print(f"ID[{self.id}]领取红包成功:[{r['datas']['msg']}]")
                self.id_.append(self.id)
                return True
            else:
                print(f"ID[{self.id}]领取红包失败:[{r['datas']['msg']}]")
        else:
            print(f"ID[{self.id}]分享失败:[{r['datas']['msg']}]")
            return False

    def main(self):
        self.userinfo()
        self.task()
        self.userinfo()
            

if __name__ == '__main__':
    version()
    cookie = ''
    if not cookie:
        cookie = os.getenv("yuanshen_tqhb")
        if not cookie:
            print("请设置环境变量:yuanshen_tqhb")
            exit()
    cookies = cookie.split("@")
    print(f"一共获取到{len(cookies)}个账号")
    i = 1
    for cookie in cookies:
        print(f"\n--------开始第{i}个账号--------")
        main = yuanshen(cookie)
        main.main()
        print(f"--------第{i}个账号执行完毕--------")
        time.sleep(20)
        i += 1
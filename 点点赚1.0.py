
#   --------------------------------注释&变量区--------------------------------
#   入口，微信打开： https://168740033-1257141735.cos-website.ap-nanjing.myqcloud.com/index.html?pid=16345
#   找含sx.shuxiangby.cn域名下的cookie中user_openid，uid，PHPSESSID的值
#   user_openid=**** 只要**** 其余两项也是如此
#   变量格式user_openid的值#uid的值#PHPSESSID的值
#   变量名：yuanshen_ddz 多号分割方式 [ @ 或 换行 或 新建同名变量 ]

#   检测配置：
#   在yuanshen_apptoken，yuanshen_topicid分别填入你的wxpusher的apptoken和topicid
#   注意是填的topicid而不是你的uid 不要傻乎乎把uid填上去 填了不推送文章包黑号的
#   不懂看 https://wxpusher.zjiecode.com/docs/#/ 或 百度 或 打钱

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


import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))

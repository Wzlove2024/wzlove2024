/**
 *
 * tclx
 *Author: Mist
 *Date: 2024-05-31
 * cron 0 6,8 * * *  tclx.js         
 * 微信小程序 同程旅行 ck有效期不清楚   完成浏览任务  里程换实物
 * 抓域名wx.17u.cn/下 openId&unionId&aesOpenId&aesUnionId&sectoken
 * export tclx= openId&unionId&aesOpenId&aesUnionId&sectoken 多账号换行或者#分隔
 */
// ============================================================================================================
const $ = new Env('vx同程旅行') 
const notify = $.isNode() ? require("./sendNotify") : "";
const got = require('got') //青龙发包依赖
const axios = require("axios");//axios
const env_name = 'tclx' //环境变量名字
const env = process.env[env_name] || '' //或 process.env.zippoCookie, node读取变量方法. 后面的 || 表示如果前面结果为false或者空字符串或者null或者undifined, 就取后面的值
const Notify = 1//是否通知, 1通知, 0不通知. 默认通知
const debug = 1//是否调试, 1调试, 0不调试. 默认不调试
let scriptVersionNow = "1.0.0";//脚本版本号
let msg;
let host = 'wx.17u.cn';
let hostname = 'https://' + host;
// ==================================异步顺序==============================================================================
!(async () => {
    await getNotice();  //远程通知
    await getVersion("yang7758258/ohhh154@main/zippo会员签到.js");
    await main();//主函数
    await SendMsg(msg); //发送通知

})()
    .catch((e) => $.logErr(e))
    .finally(() => $.done());
//==================================脚本入口函数main()==============================================================
async function main() {
    if (env == '') {
        //没有设置变量,直接退出
        console.log(`没有填写变量,请查看脚本说明: ${env_name}`)
        return
    }
    let user_ck = env.split('\n')//多账号分割,这里默认是换行(\n)分割,其他情况自己实现
    let index = 1 //用来给账号标记序号, 从1开始
    //循环遍历每个账号
    for (let ck of user_ck) {
        if (!ck) continue //跳过空行
        //默认用&分割多变量
        let ck_info = ck.split('&')
        let openid = ck_info[0]
        let unionid = ck_info[1] 
        let aesOpenid = ck_info[2]
        let aesUnionid = ck_info[3]
        let sectoken = ck_info[4]
        //用一个对象代表账号, 里面存放账号信息 注意别遗漏
        let user = {
            index: index,
            openid, //简写法, 效果等同于 openid: openid,
            openid, 
            unionid,
            aesOpenid,
            aesUnionid,
            sectoken,
        }
        index = index + 1 //每次用完序号+1
        //开始账号任务
        await userTask(user)
        //每个账号之间等1~5秒随机时间
        let rnd_time = Math.floor(Math.random() * 4000) + 1000
        console.log(`账号[${user.index}]随机等待${rnd_time / 1000}秒...`)
        await $.wait(rnd_time)
    }
}
// =========================================================================================================================
async function userTask(user) {
    //任务逻辑都放这里了, 与脚本入口分开, 方便分类控制并模块化
    console.log(`\n============= 账号[${user.index}]开始任务 =============`)
    debugLog(`【debug】 这是你的账号数组:\n ${user}`);
    await userinfo(user)
    // await liulan(user,id)
    // await liulan(user,id1)
    // await liulan(user,id2)
    // await liulan(user,id3)
    // await liulan(user,id4)
    // await liulan(user,id5)
    // await lingjiang(user,id)
    // await lingjiang(user,id1)
    // await lingjiang(user,id2)
    // await lingjiang(user,id3)
    // await lingjiang(user,id4)
    // await lingjiang(user,id5)
}
// =============================================================================================================================
//用户信息查询
async function userinfo(user) {
    //user: 用户参数, 里面存放ck和账户信息啥的. 进阶可以用类(class)的方法的代替, 效率更高
    //养成良好习惯, 每个方法里面都用try catch包起来, 这样出错了也不影响下一个步骤进行
    try {
        let url = {
            url: `${hostname}/wechatmypubapi/myInfo/headInfo`,
            headers: {
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'sectoken': user.sectoken,
                'Referer': 'https://servicewechat.com/wx336dcaf6a1ecf632/632/page-frame.html',
                'Accept-Language': 'zh-CN,zh;q=0.9',
            },
            body: JSON.stringify({"openId": user.openid,"unionId": user.unionid, "aesOpenId": user.aesOpenid, "aesUnionId": user.aesUnionid}),
           
        };
        //解构返回, 只需要result也可以这样:
        // const {result} = await request(urlObject);
        let result = await  httpPost(url, `账户信息查询`)
        // ?.语法: 前面的结果为null/undefined的时候不再执行后面操作, 可以简单的防止出错
        if (result?.retCode == 0) {
            //errcode==0的时候表示请求正常
            let value0 = result.content.headList[0].value;
            let value1 = result.content.headList[1].value;
            let value2 = result.content.headList[2].value;
            let value3 = result.content.headList[3].value;
            DoubleLog(`账号[${user.index}]` + `\n当前里程积分为:[${value0}]💰` + `\n红包优惠券:[${value1}]🎫` + `\n现金:[${value2}]💵` + `礼品卡:[${value3}]🎁`);
        } else {
            //打印请求错误信息
            DoubleLog(`账号[${user.index}]查询失败,可能是CK失效!`)
        }
    } catch (e) {
        //打印错误信息
        console.log(e)
    }
}
// =======================================
//存放任务taskid
const taskId = [
    "c77a1bcf5f75433f8bb41e5cb5209da7",//60秒玩转里程攻略
    "6e4d8b5f150d45959bd446fcd4e5636a",//100万本小说免费读
    "6507eaf4bbab42eea2be20314437c894",//下单赚现金，微信秒到账
    "cb184190929f4ab1a00bd4830f25ba0e",//订房10倍返里程，全额可抵
    "ff6bd56498bd4e73a75592db6a2d2094",//立减金叠加券使用，享折上折
    "0d15cd77790b42baa686a0adb7426e6e"//开黑鲸，每月领50元大额券
  ];
const id  = taskId[0]
const id1 = taskId[1]
const id2 = taskId[2]
const id3 = taskId[3]
const id4 = taskId[4]
const id5 = taskId[5]
//浏览任务接口
async function liulan(user,taskid) {
    try {
        let url = `${hostname}/wcsign/SignTask/SaveTaskAction`
        let body = {
            "openId": user.openid,
            "unionId": user.unionid,
            "taskId": taskid
        }

        let result = await axios.post(url, body, {
            headers: {
                'Content-Type': 'application/json',
                'sectoken': user.sectoken,
                'referer': 'https://servicewechat.com/wx336dcaf6a1ecf632/632/page-frame.html',
                'Accept-language': 'zh-CN,zh;q=0.9',

            }
       })
            
        //解构返回
        if (result?.rspCode == 0) {
            DoubleLog(`账号[${user.index}]` + `任务:[${result.message}]`)
        } else {
            //打印请求错误信息
            DoubleLog(`账号[${user.index}]任务失败`)
        }
    } catch (e) {
        //打印错误信息
        console.log(e)
    }
}

//领取奖励接口
async function lingjiang(user,taskid) {
    try {
        let host = 'wx.17u.cn'
        let hostname = 'https://' + host
        let url = `${hostname}/wcsign/SignTask/SaveTaskAction`
        let body = {
            "openId": user.openid,
            "unionId": user.unionid,
            "taskId": taskid
        }

        let result = await axios.post(url, body, {
            headers: {
                'Host': 'wx.17u.cn',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090a13) XWEB/9129',
                'Connection': 'keep-alive',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'sectoken': user.sectoken,
                'referer': 'https://servicewechat.com/wx336dcaf6a1ecf632/632/page-frame.html',
                'Accept-language': 'zh-CN,zh;q=0.9',

            }
       })
        if (result?.rspCode == 0) {
            DoubleLog(`账号[${user.index}]领取成功` + `获得里程💰:${result.Mileage}`)
        } if ( result?.rspCode == 3001){
            //打印请求错误信息
            DoubleLog(`账号[${user.index}]领取失败:[${result?.message}]`)
        }
    } catch (e) {
        //打印错误信息
        console.log(e)
    }
}
// =========================================================固定不动区域===================================================
// update:2024.05.31
// =========================================================发送消息=======================================================
async function SendMsg(message) {
    if (!message) return;
    if (Notify > 0) {
        if ($.isNode()) {
            var notify = require("./sendNotify");
            await notify.sendNotify($.name, message);
        } else {
            // $.msg(message);
            $.msg($.name, '', message)
        }
    } else {
        console.log(message);
    }
}

/**
=====================================================双平台log输出==========================================
 */
function DoubleLog(data) {
    if ($.isNode()) {
        if (data) {
            console.log(`${data}`);
            msg += `\n${data}`;
        }
    } else {
        console.log(`${data}`);
        msg += `\n${data}`;
    }

}
/**
* ======================================================等待 X 秒============================================
*/
function wait(n) {
    return new Promise(function (resolve) {
        setTimeout(resolve, n * 1000);
    });
}
//=======================================================get请求=============================================
async function httpGet(getUrlObject, tip, timeout = 3) {
    return new Promise((resolve) => {
        let url = getUrlObject;
        if (!tip) {
            let tmp = arguments.callee.toString();
            let re = /function\s*(\w*)/i;
            let matches = re.exec(tmp);
            tip = matches[1];
        }
        if (debug) {
            console.log(`\n 【debug】=============== 这是 ${tip} 请求 url ===============`);
            console.log(url);
        }

        $.get(
            url,
            async (err, resp, data) => {
                try {
                    if (debug) {
                        console.log(`\n\n 【debug】===============这是 ${tip} 返回data==============`);
                        console.log(data);
                        console.log(`\n 【debug】=============这是 ${tip} json解析后数据============`);
                        console.log(JSON.parse(data));
                    }
                    let result = JSON.parse(data);
                    if (result == undefined) {
                        return;
                    } else {
                        resolve(result);
                    }

                } catch (e) {
                    //console.log(err, resp);
                    console.log(`\n ${tip} 失败了!请稍后尝试!!`);
                    msg = `\n ${tip} 失败了!请稍后尝试!!`
                    console.log("服务器卡爆啦");
                } finally {
                    resolve();
                }
            },
            timeout
        );
    });
}
//====================================================post请求================================================================
async function httpPost(postUrlObject, tip, timeout = 3) {
    return new Promise((resolve) => {
        let url = postUrlObject;
        if (!tip) {
            let tmp = arguments.callee.toString();
            let re = /function\s*(\w*)/i;
            let matches = re.exec(tmp);
            tip = matches[1];
        }
        if (debug) {
            console.log(`\n 【debug】=============== 这是 ${tip} 请求 url ===============`);
            console.log(url);
        }

        $.post(
            url,
            async (err, resp, data) => {
                try {
                    if (debug) {
                        console.log(`\n\n 【debug】===============这是 ${tip} 返回data==============`);
                        console.log(data);
                        console.log(`\n 【debug】=============这是 ${tip} json解析后数据============`);
                        console.log(JSON.parse(data));
                    }
                    let result = JSON.parse(data);
                    if (result == undefined) {
                        return;
                    } else {
                        resolve(result);
                    }

                } catch (e) {
                    //console.log(err, resp);
                    console.log(`\n ${tip} 失败了!请稍后尝试!!`);
                    msg = `\n ${tip} 失败了!请稍后尝试!!`
                    console.log("服务器卡爆啦");
                } finally {
                    resolve();
                }
            },
            timeout
        );
    });
}

//===============================================网络请求httpRequest=========================================
function httpRequest(options, timeout = 1 * 1000) {
    method = options.method ? options.method.toLowerCase() : options.body ? "post" : "get";
    return new Promise(resolve => {
        setTimeout(() => {
            $[method](options, (err, resp, data) => {
                try {
                    if (err) {
                        console.log(JSON.stringify(err));
                        $.logErr(err);
                    } else {
                        try { data = JSON.parse(data); } catch (error) { }
                    }
                } catch (e) {
                    console.log(e);
                    $.logErr(e, resp);
                } finally {
                    resolve(data);
                }
            })
        }, timeout)
    })
}
//==============================================Debug模式===============================================
function debugLog(...args) {
    if (debug) {
        console.log(...args);
    }
}
//===============================================获取远程通知========================================
async function getNotice() {
    try {
        const urls = [
            "https://gitee.com/ohhhooh/jd_haoyangmao/raw/master/Notice.json",
            
        ];
        let notice = null;
        for (const url of urls) {
            const options = { url, headers: { "User-Agent": "" }, };
            const result = await httpRequest(options);
            if (result && "notice" in result) {
                notice = result.notice.replace(/\\n/g, "\n");
                break;
            }
        }
        if (notice) { $.DoubleLog(notice); }
    } catch (e) {
        console.log(e);
    }
}
//==============================================获取远程版本=================================================
function getVersion(scriptUrl, timeout = 3 * 1000) {
    return new Promise((resolve) => {
        const options = { url: `https://fastly.jsdelivr.net/gh/${scriptUrl}` };
        $.get(options, (err, resp, data) => {
            try {
                const regex = /scriptVersionNow\s*=\s*(["'`])([\d.]+)\1/;
                const match = data.match(regex);
                const scriptVersionLatest = match ? match[2] : "";
                console.log(`\n====== 当前版本：${scriptVersionNow} 📌 最新版本：${scriptVersionLatest} ======`);
            } catch (e) {
                $.logErr(e, resp);
            }
            resolve();
        }, timeout);
    });
}
//=================================青龙发包GOT===========================================================
//got的基本用法, 封装一下方便之后直接调用, 新手可以不动他直接用就行
// async function request(opt) {
//     const DEFAULT_RETRY = 3 //请求出错重试三次
//     var resp = null, count = 0
//     var fn = opt.fn || opt.url
//     opt.method = opt?.method?.toUpperCase() || 'GET'
//     while (count++ < DEFAULT_RETRY) {
//         try {
//             var err = null
//             const errcodes = ['ECONNRESET', 'EADDRINUSE', 'ENOTFOUND', 'EAI_AGAIN']
//             await got(opt).then(t => {
//                 resp = t
//             }, e => {
//                 err = e
//                 resp = e.response
//             })
//             if (err) {
//                 if (err.name == 'TimeoutError') {
//                     console.log(`[${fn}]请求超时(${err.code})，重试第${count}次`)
//                 } else if (errcodes.includes(err.code)) {
//                     console.log(`[${fn}]请求错误(${err.code})，重试第${count}次`)
//                 } else {
//                     let statusCode = resp?.statusCode || -1
//                     console.log(`[${fn}]请求错误(${err.message}), 返回[${statusCode}]`)
//                     break
//                 }
//             } else {
//                 break
//             }
//         } catch (e) {
//             console.log(`[${fn}]请求错误(${e.message})，重试第${count}次`)
//         };
//     }
//     let { statusCode = -1, headers = null, body = null } = resp
//     if (body) try { body = JSON.parse(body) } catch { };
//     return { statusCode, headers, result: body }
// }
//===============================================================================================================================================
//================================================固定API===============================================================================================
function Env(t, e) { class s { constructor(t) { this.env = t } send(t, e = "GET") { t = "string" == typeof t ? { url: t } : t; let s = this.get; return ("POST" === e && (s = this.post), new Promise((e, a) => { s.call(this, t, (t, s, r) => { t ? a(t) : e(s) }) })) } get(t) { return this.send.call(this.env, t) } post(t) { return this.send.call(this.env, t, "POST") } } return new (class { constructor(t, e) { this.userList = []; this.userIdx = 0; (this.name = t), (this.http = new s(this)), (this.data = null), (this.dataFile = "box.dat"), (this.logs = []), (this.isMute = !1), (this.isNeedRewrite = !1), (this.logSeparator = "\n"), (this.encoding = "utf-8"), (this.startTime = new Date().getTime()), Object.assign(this, e), this.log("", `🔔${this.name},开始!`) } getEnv() { return "undefined" != typeof $environment && $environment["surge-version"] ? "Surge" : "undefined" != typeof $environment && $environment["stash-version"] ? "Stash" : "undefined" != typeof module && module.exports ? "Node.js" : "undefined" != typeof $task ? "Quantumult X" : "undefined" != typeof $loon ? "Loon" : "undefined" != typeof $rocket ? "Shadowrocket" : void 0 } isNode() { return "Node.js" === this.getEnv() } isQuanX() { return "Quantumult X" === this.getEnv() } isSurge() { return "Surge" === this.getEnv() } isLoon() { return "Loon" === this.getEnv() } isShadowrocket() { return "Shadowrocket" === this.getEnv() } isStash() { return "Stash" === this.getEnv() } toObj(t, e = null) { try { return JSON.parse(t) } catch { return e } } toStr(t, e = null) { try { return JSON.stringify(t) } catch { return e } } getjson(t, e) { let s = e; const a = this.getdata(t); if (a) try { s = JSON.parse(this.getdata(t)) } catch { } return s } setjson(t, e) { try { return this.setdata(JSON.stringify(t), e) } catch { return !1 } } getScript(t) { return new Promise((e) => { this.get({ url: t }, (t, s, a) => e(a)) }) } runScript(t, e) { return new Promise((s) => { let a = this.getdata("@chavy_boxjs_userCfgs.httpapi"); a = a ? a.replace(/\n/g, "").trim() : a; let r = this.getdata("@chavy_boxjs_userCfgs.httpapi_timeout"); (r = r ? 1 * r : 20), (r = e && e.timeout ? e.timeout : r); const [i, o] = a.split("@"), n = { url: `http://${o}/v1/scripting/evaluate`, body: { script_text: t, mock_type: "cron", timeout: r }, headers: { "X-Key": i, Accept: "*/*" }, timeout: r, }; this.post(n, (t, e, a) => s(a)) }).catch((t) => this.logErr(t)) } loaddata() { if (!this.isNode()) return {}; { (this.fs = this.fs ? this.fs : require("fs")), (this.path = this.path ? this.path : require("path")); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), a = !s && this.fs.existsSync(e); if (!s && !a) return {}; { const a = s ? t : e; try { return JSON.parse(this.fs.readFileSync(a)) } catch (t) { return {} } } } } writedata() { if (this.isNode()) { (this.fs = this.fs ? this.fs : require("fs")), (this.path = this.path ? this.path : require("path")); const t = this.path.resolve(this.dataFile), e = this.path.resolve(process.cwd(), this.dataFile), s = this.fs.existsSync(t), a = !s && this.fs.existsSync(e), r = JSON.stringify(this.data); s ? this.fs.writeFileSync(t, r) : a ? this.fs.writeFileSync(e, r) : this.fs.writeFileSync(t, r) } } lodash_get(t, e, s) { const a = e.replace(/\[(\d+)\]/g, ".$1").split("."); let r = t; for (const t of a) if (((r = Object(r)[t]), void 0 === r)) return s; return r } lodash_set(t, e, s) { return Object(t) !== t ? t : (Array.isArray(e) || (e = e.toString().match(/[^.[\]]+/g) || []), (e.slice(0, -1).reduce((t, s, a) => Object(t[s]) === t[s] ? t[s] : (t[s] = Math.abs(e[a + 1]) >> 0 == +e[a + 1] ? [] : {}), t)[e[e.length - 1]] = s), t) } getdata(t) { let e = this.getval(t); if (/^@/.test(t)) { const [, s, a] = /^@(.*?)\.(.*?)$/.exec(t), r = s ? this.getval(s) : ""; if (r) try { const t = JSON.parse(r); e = t ? this.lodash_get(t, a, "") : e } catch (t) { e = "" } } return e } setdata(t, e) { let s = !1; if (/^@/.test(e)) { const [, a, r] = /^@(.*?)\.(.*?)$/.exec(e), i = this.getval(a), o = a ? ("null" === i ? null : i || "{}") : "{}"; try { const e = JSON.parse(o); this.lodash_set(e, r, t), (s = this.setval(JSON.stringify(e), a)) } catch (e) { const i = {}; this.lodash_set(i, r, t), (s = this.setval(JSON.stringify(i), a)) } } else s = this.setval(t, e); return s } getval(t) { switch (this.getEnv()) { case "Surge": case "Loon": case "Stash": case "Shadowrocket": return $persistentStore.read(t); case "Quantumult X": return $prefs.valueForKey(t); case "Node.js": return (this.data = this.loaddata()), this.data[t]; default: return (this.data && this.data[t]) || null } } setval(t, e) { switch (this.getEnv()) { case "Surge": case "Loon": case "Stash": case "Shadowrocket": return $persistentStore.write(t, e); case "Quantumult X": return $prefs.setValueForKey(t, e); case "Node.js": return ((this.data = this.loaddata()), (this.data[e] = t), this.writedata(), !0); default: return (this.data && this.data[e]) || null } } initGotEnv(t) { (this.got = this.got ? this.got : require("got")), (this.cktough = this.cktough ? this.cktough : require("tough-cookie")), (this.ckjar = this.ckjar ? this.ckjar : new this.cktough.CookieJar()), t && ((t.headers = t.headers ? t.headers : {}), void 0 === t.headers.Cookie && void 0 === t.cookieJar && (t.cookieJar = this.ckjar)) } get(t, e = () => { }) { switch ((t.headers && (delete t.headers["Content-Type"], delete t.headers["Content-Length"], delete t.headers["content-type"], delete t.headers["content-length"]), this.getEnv())) { case "Surge": case "Loon": case "Stash": case "Shadowrocket": default: this.isSurge() && this.isNeedRewrite && ((t.headers = t.headers || {}), Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient.get(t, (t, s, a) => { !t && s && ((s.body = a), (s.statusCode = s.status ? s.status : s.statusCode), (s.status = s.statusCode)), e(t, s, a) }); break; case "Quantumult X": this.isNeedRewrite && ((t.opts = t.opts || {}), Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then((t) => { const { statusCode: s, statusCode: a, headers: r, body: i, bodyBytes: o, } = t; e(null, { status: s, statusCode: a, headers: r, body: i, bodyBytes: o, }, i, o) }, (t) => e((t && t.error) || "UndefinedError")); break; case "Node.js": let s = require("iconv-lite"); this.initGotEnv(t), this.got(t).on("redirect", (t, e) => { try { if (t.headers["set-cookie"]) { const s = t.headers["set-cookie"].map(this.cktough.Cookie.parse).toString(); s && this.ckjar.setCookieSync(s, null), (e.cookieJar = this.ckjar) } } catch (t) { this.logErr(t) } }).then((t) => { const { statusCode: a, statusCode: r, headers: i, rawBody: o, } = t, n = s.decode(o, this.encoding); e(null, { status: a, statusCode: r, headers: i, rawBody: o, body: n, }, n) }, (t) => { const { message: a, response: r } = t; e(a, r, r && s.decode(r.rawBody, this.encoding)) }) } } post(t, e = () => { }) { const s = t.method ? t.method.toLocaleLowerCase() : "post"; switch ((t.body && t.headers && !t.headers["Content-Type"] && !t.headers["content-type"] && (t.headers["content-type"] = "application/x-www-form-urlencoded"), t.headers && (delete t.headers["Content-Length"], delete t.headers["content-length"]), this.getEnv())) { case "Surge": case "Loon": case "Stash": case "Shadowrocket": default: this.isSurge() && this.isNeedRewrite && ((t.headers = t.headers || {}), Object.assign(t.headers, { "X-Surge-Skip-Scripting": !1 })), $httpClient[s](t, (t, s, a) => { !t && s && ((s.body = a), (s.statusCode = s.status ? s.status : s.statusCode), (s.status = s.statusCode)), e(t, s, a) }); break; case "Quantumult X": (t.method = s), this.isNeedRewrite && ((t.opts = t.opts || {}), Object.assign(t.opts, { hints: !1 })), $task.fetch(t).then((t) => { const { statusCode: s, statusCode: a, headers: r, body: i, bodyBytes: o, } = t; e(null, { status: s, statusCode: a, headers: r, body: i, bodyBytes: o, }, i, o) }, (t) => e((t && t.error) || "UndefinedError")); break; case "Node.js": let a = require("iconv-lite"); this.initGotEnv(t); const { url: r, ...i } = t; this.got[s](r, i).then((t) => { const { statusCode: s, statusCode: r, headers: i, rawBody: o, } = t, n = a.decode(o, this.encoding); e(null, { status: s, statusCode: r, headers: i, rawBody: o, body: n }, n) }, (t) => { const { message: s, response: r } = t; e(s, r, r && a.decode(r.rawBody, this.encoding)) }) } } time(t, e = null) { const s = e ? new Date(e) : new Date(); let a = { "M+": s.getMonth() + 1, "d+": s.getDate(), "H+": s.getHours(), "m+": s.getMinutes(), "s+": s.getSeconds(), "q+": Math.floor((s.getMonth() + 3) / 3), S: s.getMilliseconds(), }; /(y+)/.test(t) && (t = t.replace(RegExp.$1, (s.getFullYear() + "").substr(4 - RegExp.$1.length))); for (let e in a) new RegExp("(" + e + ")").test(t) && (t = t.replace(RegExp.$1, 1 == RegExp.$1.length ? a[e] : ("00" + a[e]).substr(("" + a[e]).length))); return t } queryStr(t) { let e = ""; for (const s in t) { let a = t[s]; null != a && "" !== a && ("object" == typeof a && (a = JSON.stringify(a)), (e += `${s}=${a}&`)) } return (e = e.substring(0, e.length - 1)), e } msg(e = t, s = "", a = "", r) { const i = (t) => { switch (typeof t) { case void 0: return t; case "string": switch (this.getEnv()) { case "Surge": case "Stash": default: return { url: t }; case "Loon": case "Shadowrocket": return t; case "Quantumult X": return { "open-url": t }; case "Node.js": return }case "object": switch (this.getEnv()) { case "Surge": case "Stash": case "Shadowrocket": default: { let e = t.url || t.openUrl || t["open-url"]; return { url: e } } case "Loon": { let e = t.openUrl || t.url || t["open-url"], s = t.mediaUrl || t["media-url"]; return { openUrl: e, mediaUrl: s } } case "Quantumult X": { let e = t["open-url"] || t.url || t.openUrl, s = t["media-url"] || t.mediaUrl, a = t["update-pasteboard"] || t.updatePasteboard; return { "open-url": e, "media-url": s, "update-pasteboard": a, } } case "Node.js": return }default: return } }; if (!this.isMute) switch (this.getEnv()) { case "Surge": case "Loon": case "Stash": case "Shadowrocket": default: $notification.post(e, s, a, i(r)); break; case "Quantumult X": $notify(e, s, a, i(r)); break; case "Node.js": }if (!this.isMuteLog) { let t = ["", "==============📣系统通知📣==============",]; t.push(e), s && t.push(s), a && t.push(a), console.log(t.join("\n")), (this.logs = this.logs.concat(t)) } } log(...t) { t.length > 0 && (this.logs = [...this.logs, ...t]), console.log(t.join(this.logSeparator)) } logErr(t, e) { switch (this.getEnv()) { case "Surge": case "Loon": case "Stash": case "Shadowrocket": case "Quantumult X": default: this.log("", `❗️${this.name},错误!`, t); break; case "Node.js": this.log("", `❗️${this.name},错误!`, t.stack) } } wait(t) { return new Promise((e) => setTimeout(e, t)) } DoubleLog(d) { if (this.isNode()) { if (d) { console.log(`${d}`); msg += `\n ${d}` } } else { console.log(`${d}`); msg += `\n ${d}` } } async SendMsg(m) { if (!m) return; if (Notify > 0) { if (this.isNode()) { var notify = require("./sendNotify"); await notify.sendNotify(this.name, m) } else { this.msg(this.name, "", m) } } else { console.log(m) } } done(t = {}) { const e = new Date().getTime(), s = (e - this.startTime) / 1e3; switch ((this.log("", `🔔${this.name},结束!🕛${s}秒`), this.log(), this.getEnv())) { case "Surge": case "Loon": case "Stash": case "Shadowrocket": case "Quantumult X": default: $done(t); break; case "Node.js": process.exit(1) } } })(t, e) }
//Env rewrite:smallfawn Update-time:23-6-30 newAdd:DoubleLog & SendMsg
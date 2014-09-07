__author__ = 'ifcheung'
# -*- coding:gb2312 -*-
import httplib
import urllib, urllib2
import cookielib

Host=	"220.180.21.26"
loginurl = "http://220.180.21.26:8059/vbmis/devapp/IControl/IUsers?login_validator=login&userName=admin&passward=96E79218965EB72C92A549DD5A330112&tmp=1?random=0.020557932322362138"
para = {'userName':'admin',
        'password':'111111',
        'tmp':1}

postData = urllib.urlencode(para);
cookieJarInMemory = cookielib.CookieJar();
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookieJarInMemory));
urllib2.install_opener(opener);

resp1 = urllib2.urlopen(loginurl)
print cookieJarInMemory
print resp1

req = urllib2.Request(loginurl, postData); # urllib2.Request: the HTTP request will be a POST instead of a GET when the data parameter is provided.
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:26.0) Gecko/20100101 Firefox/26.0');
req.add_header('Content-Type', 'application/x-www-form-urlencoded');
req.add_header('Cache-Control', 'no-cache');
req.add_header('Accept', '*/*');
req.add_header('Connection', 'Keep-Alive');
resp = urllib2.urlopen(req);
respInfo = resp.info();
print cookieJarInMemory
print respInfo


requesturl = "http://220.180.21.26:8059/vbmis/devapp/IBudget/IPubFun?random=0.9568880549222739"

headerdata = {"X-Requested-With": "XMLHttpRequest",
              "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:26.0) Gecko/20100101 Firefox/26.0",
              "Referer": "http://220.180.21.26:8059/vbmis/page/budget/xssr_edit.jsp?state=i&mdid=BUDGET_0019&mdname=%E9%94%80%E5%94%AE%E6%94%B6%E5%85%A5%E9%A2%84%E7%AE%97",
              "Pragma": "no-cache",
              "mdid": "BUDGET_0019",
              "mapkey": "XssrInfo.insertXssr",
              "Host": "220.180.21.26:8059",
              "Content-Type": "application/json;charset=utf-8",
              "Content-Length": "7026",
              "Connection": "keep-alive",
              "Cache-Control": "no-cache",
              "Authorization": "space accessname='web', ramdom='4' , code='AFA459FFAB4F9F13C3B6AB64EE03758D'",
              "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
              "Accept-Encoding": "gzip, deflate",
              "Accept": "application/json, text/javascript, */*; q=0.01"}

postdata = {"insert": {
"com.horizon.module.budget.app.vo.XssrVO": {"yslx": "3", "month": "2", "id": "", "ysfa": "YSFA201311131622100011",
                                            "zrzx": "ORG201311080922040009", "yskm": "KJKM201311111011430167",
                                            "whrname": "赵二",
                                            "hsje": ["0", "0", "0", "0", "0", "1193283", "6879990", "3325647", "661440",
                                                     "2647008", "14002560", "13253760", "10007712"], "ysje": "0",
                                            "whsj": "2013-12-25 21:10:38", "hsfjje": "0", "fjje": "0", "qjje": "",
                                            "rowno": "", "khid": ["KH201311081119290017", "KH201311081119290017",
                                                                  "KH201311081119290017", "KH201311081119290017",
                                                                  "KH201311081119290017", "KH201311081119290017",
                                                                  "KH201311081119290017", "KH201311081119290017",
                                                                  "KH201311081119290017", "KH201311081119290017",
                                                                  "KH201311081119290017", "KH201311081119290017"],
                                            "khcode": ["C001", "C001", "C001", "C001", "C001", "C001", "C001", "C001",
                                                       "C001", "C001", "C001", "C001"],
                                            "khmc": ["A客户", "A客户", "A客户", "A客户", "A客户", "A客户", "A客户", "A客户", "A客户",
                                                     "A客户", "A客户", "A客户"],
                                            "cp": ["WL201311081423160038", "WL201311081422440037",
                                                   "WL201311081422190036", "WL201311081421230035",
                                                   "WL201311081420500034", "WL201311081420180033",
                                                   "WL201311081419410032", "WL201311081419070031",
                                                   "WL201311081417450030", "WL201311081417140029",
                                                   "WL201311081416470028", "WL201311081416040027"],
                                            "cpcode": ["ZY002", "ZY001", "WM401", "WM301", "WM203", "WM202", "WM201",
                                                       "WM105", "WM104", "WM103", "WM102", "WM101"],
                                            "cpname": ["邮政车", "厢货车", "CNG双燃料车", "微面STJ6401A", "微面STJ6400B",
                                                       "微面STJ6400B", "微面STJ6400B", "微面STJ6400A", "微面STJ6400A",
                                                       "微面STJ6400A", "微面STJ6400A", "微面STJ6400A"],
                                            "cplx": ["舒适型", "标准型", "基本型", "豪华型", "舒适型", "标准型", "基本型", "简配型 "],
                                            "cpjldw": ["辆", "辆", "辆", "辆", "辆", "辆", "辆", "辆", "辆", "辆", "辆", "辆 "],
                                            "sxid": "FZSX201312230907070015", "sxcode": "02", "sxname": "yellow",
                                            "zzsl": ["17", "17", "17", "17", "17", "17", "17", "17", "17", "17", "17",
                                                     "17"],
                                            "hsdj": ["45045", "42705", "49608", "45864", "38493", "34983", "31473",
                                                     "49608", "47268", "43758", "41418", "37908"],
                                            "dj": ["38500", "36500", "42400", "39200", "32900", "29900", "26900",
                                                   "42400", "40400", "37400", "35400", "32400"],
                                            "ysl": ["0", "0", "0", "0", "93", "590", "317", "40", "168", "960", "960",
                                                    "792"],
                                            "hsyje": ["0", "0", "0", "0", "3579849", "20639970", "9976941", "1984320",
                                                      "7941024", "42007680", "39761280", "30023136"],
                                            "yje": ["0", "0", "0", "0", "3059700", "17641000", "8527300", "1696000",
                                                    "6787200", "35904000", "33984000", "25660800"],
                                            "sl": ["0", "0", "0", "0", "31", "196.66666666", "105.66666666",
                                                   "13.33333333", "56", "320", "320", "264"],
                                            "je": ["0", "0", "0", "0", "1019900", "5880333.3333333", "2842433.3333333",
                                                   "565333.3333333", "2262400", "11968000", "11328000", "8553600"],
                                            "xssrmxVos": [{"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081423160038",
                                                           "cpcode": "ZY002", "cpname": "邮政车", "cplx": "",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "45045", "dj": "38500", "ysl": "0",
                                                           "hsyje": "0", "yje": "0", "sl": "0", "hsje": "0", "je": "0"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081422440037",
                                                           "cpcode": "ZY001", "cpname": "厢货车", "cplx": "",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "42705", "dj": "36500", "ysl": "0",
                                                           "hsyje": "0", "yje": "0", "sl": "0", "hsje": "0", "je": "0"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081422190036",
                                                           "cpcode": "WM401", "cpname": "CNG双燃料车", "cplx": "",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "49608", "dj": "42400", "ysl": "0",
                                                           "hsyje": "0", "yje": "0", "sl": "0", "hsje": "0", "je": "0"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081421230035",
                                                           "cpcode": "WM301", "cpname": "微面STJ6401A", "cplx": "",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "45864", "dj": "39200", "ysl": "0",
                                                           "hsyje": "0", "yje": "0", "sl": "0", "hsje": "0", "je": "0"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081420500034",
                                                           "cpcode": "WM203", "cpname": "微面STJ6400B", "cplx": "舒适型",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "38493", "dj": "32900", "ysl": "93",
                                                           "hsyje": "3579849", "yje": "3059700", "sl": "31",
                                                           "hsje": "1193283", "je": "1019900"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081420180033",
                                                           "cpcode": "WM202", "cpname": "微面STJ6400B", "cplx": "标准型",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "34983", "dj": "29900", "ysl": "590",
                                                           "hsyje": "20639970", "yje": "17641000", "sl": "196.66666666",
                                                           "hsje": "6879990", "je": "5880333.3333333"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081419410032",
                                                           "cpcode": "WM201", "cpname": "微面STJ6400B", "cplx": "基本型",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "31473", "dj": "26900", "ysl": "317",
                                                           "hsyje": "9976941", "yje": "8527300", "sl": "105.66666666",
                                                           "hsje": "3325647", "je": "2842433.3333333"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081419070031",
                                                           "cpcode": "WM105", "cpname": "微面STJ6400A", "cplx": "豪华型",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "49608", "dj": "42400", "ysl": "40",
                                                           "hsyje": "1984320", "yje": "1696000", "sl": "13.33333333",
                                                           "hsje": "661440", "je": "565333.3333333"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081417450030",
                                                           "cpcode": "WM104", "cpname": "微面STJ6400A", "cplx": "舒适型",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "47268", "dj": "40400", "ysl": "168",
                                                           "hsyje": "7941024", "yje": "6787200", "sl": "56",
                                                           "hsje": "2647008", "je": "2262400"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081417140029",
                                                           "cpcode": "WM103", "cpname": "微面STJ6400A", "cplx": "标准型",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "43758", "dj": "37400", "ysl": "960",
                                                           "hsyje": "42007680", "yje": "35904000", "sl": "320",
                                                           "hsje": "14002560", "je": "11968000"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081416470028",
                                                           "cpcode": "WM102", "cpname": "微面STJ6400A", "cplx": "基本型",
                                                           "cpjldw": "辆", "sxid": "", "sxcode": "", "sxname": "",
                                                           "zzsl": "17", "hsdj": "41418", "dj": "35400", "ysl": "960",
                                                           "hsyje": "39761280", "yje": "33984000", "sl": "320",
                                                           "hsje": "13253760", "je": "11328000"},
                                                          {"status": 1, "mapSels": [], "qjje": "", "rowno": "",
                                                           "khid": "KH201311081119290017", "khcode": "C001",
                                                           "khmc": "A客户", "cp": "WL201311081416040027",
                                                           "cpcode": "WM101", "cpname": "微面STJ6400A", "cplx": "简配型 ",
                                                           "cpjldw": "辆 ", "sxid": "FZSX201312230907070015",
                                                           "sxcode": "02", "sxname": "yellow", "zzsl": "17",
                                                           "hsdj": "37908", "dj": "32400", "ysl": "792",
                                                           "hsyje": "30023136", "yje": "25660800", "sl": "264",
                                                           "hsje": "10007712", "je": "8553600"}]}}}
conn = httplib.HTTPConnection("220.180.21.26", "8059")


reqdata = urllib.urlencode(postdata)
conn.request(method="POST", url=requesturl, body=reqdata, headers=headerdata)
res = conn.getresponse()
print res.msg
conn.close()
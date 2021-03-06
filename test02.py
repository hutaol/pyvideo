import requests
import os
import time
import random
import pymysql

from random import Random

def random_phonenum(numlength=32):
    num =''
    chars='1234567890'
    length=len(chars)-1
    rd=Random()
    for j in range(numlength):
        num +=chars[rd.randint(0,length)]
    return num

def getKandianUrl():
    pass


# http://kandian.qq.com/qz_kandian_ext/kandian_ext/SetVideoPlayCount?vid=t07564o2k6p&rtype=0&rcode=0&token=1499787794&uuid=0308167210877994261534329722709
# http://kandian.qq.com/qz_kandian_ext/kandian_ext/SetVideoPlayCount?vid=t07564o2k6p&rtype=0&rcode=0&token=1499787794&uuid=60809028364664461534330751413

# url = 'http://kandian.qq.com/qz_kandian_ext/kandian_ext/SetVideoPlayCount?vid=t07564o2k6p'

# refer = 'http://post.mp.qq.com/kan/video/1901479951-2485b72d09e536aj-v07561lmxld.html?_wv=2281701505&sig=7edf20f0804ba7c01e59c1b6e7a6f9ef&time=1534251166&sourcefrom=6'
# refer = 'http://post.mp.qq.com/kan/video/1901479951-7335b742b2c475aj-l0757jbak98.html?_wv=2281701505&sig=ab7b5c3dd7db610098318de2678b1f7d&time=1534339884&sourcefrom=6'
refer = 'http://post.mp.qq.com/kan/video/1901292418-2975b8e7889207aj-SyzVA.html?_wv=2281701505&sig=3de11f33d09a58a60361dd6e3cd89b64&time=1536063625&sourcefrom=6'
vid = 'SyzVA'
headers = {
    # 'Accept': 'application/json',
    # 'Accept-Encoding': 'gzip, deflate',
    # 'Accept-Language': 'zh-CN,zh;q=0.9',
    # 'Connection': 'keep-alive',
    # 'Cookie': 'pgv_pvi=1057001472; RK=FrBxn1CERL; ptcz=43adaf6cdb11ef8863c8f30c9ecca3f7d794c907342145a2a976088de7a7286a; pgv_pvid=7568353335; tvfe_boss_uuid=8cb0b948d6dd6ac4; pac_uid=1_1194332304; eas_sid=M155I3d119c7L4o1w1J3N8W6d7; ue_uk=e098cf75fb374372f79380486f251299; ue_uid=940371b6f425307d6badf1f9085d1650; LW_uid=J1P5W3K15947T557p8a7O9t6T2; LW_pid=72d6681a10f61d611fb7d9a5f94288f6; ue_ts=1531975945; ue_skey=5924dc23dac6300d4b818499c5175f24; mobileUV=1_164b18eaa0c_6b9b8; LW_sid=B1G5c3b3U7a9b030x2l6F1K4r5; AMCV_248F210755B762187F000101%40AdobeOrg=-1891778711%7CMCIDTS%7C17753%7CMCMID%7C69604585822315279883440476244192776143%7CMCAAMLH-1534402396%7C11%7CMCAAMB-1534402396%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1533804796s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17760%7CvVersion%7C2.4.0; o_cookie=810359132; pgv_si=s2447248384; ptisp=ctc; pgv_info=ssid=s4189052732; ptui_loginuin=3056371919; pt2gguin=o0810359132; uin=o0810359132; skey=@n9IoidQIf',
    'Host': 'kandian.qq.com',
    'Origin': 'http://post.mp.qq.com',
    'Referer': refer,
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

MYSQL_CONF = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'passwd': 'ht123456',
    'db': 'proxypool'
}

def getProxies():
    conn = pymysql.connect(host=MYSQL_CONF['host'],
                               user=MYSQL_CONF['user'],
                               passwd=MYSQL_CONF['passwd'],
                               db=MYSQL_CONF['db'],
                               port=MYSQL_CONF['port'],
                               charset='utf8')
    cursor = conn.cursor()
    cursor.execute('select ip,ip_port from proxypool')
    ip_list = []
    for row in cursor.fetchall():
        ip_list.append("%s:%s" % (row[0], row[1]))

    content = random.choice(ip_list)

    proxies = {
        'http': 'http://'+content,
        'https': 'https://'+content
    }
    return proxies

TIMEOUT = 10

urls = []

for i in range(1000):

    # proxies = getProxies()
    token = random_phonenum(10)
    uuid = random_phonenum(30)
    print(vid)
    url = 'http://kandian.qq.com/qz_kandian_ext/kandian_ext/SetVideoPlayCount?vid=%s&rtype=0&rcode=0&token=%s&uuid=%s' % (vid, token, uuid)
    
    print(i)
    print(url)
   
    try:
        res = requests.get(url, headers=headers, timeout=TIMEOUT)
        print(res.content)
    except Exception as e:
        print('request error')


    time.sleep(1)


# http://kandian.qq.com/qz_kandian_ext/kandian_ext/GetVideoPlayCount?puin=1466387522&vid=SyzVA&token=1608772387&uuid=392383906163423561536079957156

# Accept: application/json
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.9
# Connection: keep-alive
# Cookie: pgv_pvi=1057001472; RK=FrBxn1CERL; ptcz=43adaf6cdb11ef8863c8f30c9ecca3f7d794c907342145a2a976088de7a7286a; pgv_pvid=7568353335; tvfe_boss_uuid=8cb0b948d6dd6ac4; eas_sid=M155I3d119c7L4o1w1J3N8W6d7; ue_uk=e098cf75fb374372f79380486f251299; ue_uid=940371b6f425307d6badf1f9085d1650; LW_uid=J1P5W3K15947T557p8a7O9t6T2; LW_pid=72d6681a10f61d611fb7d9a5f94288f6; ue_ts=1531975945; ue_skey=5924dc23dac6300d4b818499c5175f24; mobileUV=1_164b18eaa0c_6b9b8; LW_sid=B1G5c3b3U7a9b030x2l6F1K4r5; AMCV_248F210755B762187F000101%40AdobeOrg=-1891778711%7CMCIDTS%7C17753%7CMCMID%7C69604585822315279883440476244192776143%7CMCAAMLH-1534402396%7C11%7CMCAAMB-1534402396%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1533804796s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-17760%7CvVersion%7C2.4.0; pac_uid=1_810359132; pgv_pvid_new=810359132_3a88ec091e; pgv_si=s4023227392; ptisp=ctc; pgv_info=ssid=s5995211425; o_cookie=810359132; ptui_loginuin=1194332304; pt2gguin=o1194332304; uin=o1194332304; skey=@CpMF0u4ju
# Host: kandian.qq.com
# Origin: http://post.mp.qq.com
# Referer: http://post.mp.qq.com/kan/video/1901292418-2975b8e7889207aj-SyzVA.html?_wv=2281701505&sig=3de11f33d09a58a60361dd6e3cd89b64&time=1536063625
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
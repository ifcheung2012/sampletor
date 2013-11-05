# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
import re

import urllib,urllib2
from BeautifulSoup import BeautifulSoup
def main():
    srcurl="http://zst.cjcp.com.cn/cjwssq/view/hong_zonghe-1-2013121-2013125-1.html"
    lottourl="http://zst.cjcp.com.cn/cjwdlt/view/dlteqzonghe-1-2013096-2013125-1.html"
    f=urllib.urlopen(srcurl)
    html=f.read()
    f2=urllib.urlopen(lottourl)
    html2=f2.read()

    # soup=BeautifulSoup(html)
    #
    # issue = soup.findAll('td',attrs={'class':'z_bg_05'})
    # redball=soup.findAll('td',attrs={'class':'WhiteBack RedFont'})
    # blueball=soup.findAll('td',attrs={'class':'WhiteBack BlueFont'})

    # for v in result:
    #     print re.compile(' ').subn(',',str(v.text))[0]

    patt = re.findall("<td class=\'z_bg_05\'>(?P<id>.*?)</td><td class=\'z_bg_05\'>(?P<issue>.*?)</td><td class=\'WhiteBack RedFont\' nowrap>(?P<redball>.*?)</td>\
<td class=\'WhiteBack BlueFont\'>(?P<blueball>.*?)</td> \
<td class=bg3><span class=z_font_orange>(?P<valsum>.*?)</span></td>\
<td class=z_bg_06><span class=z_font_green>(?P<valsumendnumber>.*?)</span></td>\
<td class=bg3><span class=z_font_orange>(?P<valavg>.*?)</span></td>\
<td class=z_bg_06><span class=z_font_green>(?P<valendsum>.*?)</span></td>\
<td class=bg3><span class=z_font_orange>(?P<valendgroup>.*?)</span></td><td class=z_bg_06><span class=z_font_green>(?P<valdistance>.*?)</span></td><td class=bg3><span class=z_font_orange>(?P<valbigdistance>.*?)</span></td>\
<td class=z_bg_06><span class=z_font_green>(?P<valrepeat>.*?)</span></td><td class=bg3><span class=z_font_orange>(?P<valconcount>.*?)</span></td><td class=z_bg_06><span class=z_font_green>(?P<valcongroups>.*?)</span></td>\
<td class=bg3><span class=z_font_orange>(?P<ratiobigsmall>.*?)</span></td><td class=z_bg_06><span class=z_font_green>(?P<ratiooddeven>.*?)</span></td><td class=bg3><span class=z_font_orange>(?P<ratio3>.*?)</span></td>\
<td class=z_bg_06><span class=z_font_green>(?P<ratio4>.*?)</span></td><td class=bg3><span class=z_font_orange>(?P<ratio5>.*?)</span></td><td class=z_bg_06><span class=z_font_green>(?P<ratio6>.*?)</span></td>\
<td class=bg3><span class=z_font_orange>(?P<valac>.*?)</span></td><td class=z_bg_06><span class=z_font_green>(?P<valconoddeven>.*?)</span></td><td class=bg3><span class=z_font_orange>(?P<valconeven>.*?)</span></td>",html,re.I)
    # match = patt.match(html)
    for i in patt:
        print i
        # print i[1],i[2]+':'+i[3]

    # lottopatt = re.findall("<td class='z_bg_05'>(?P<id>.*?)</td><td class='z_bg_05'>(?P<issue>.*?)</td><td class='WhiteBack RedFont' nowrap >(?P<redball>.*?)</td><td class='WhiteBack BlueFont'>(?P<blueball>.*?)</td>",html2,re.I)
    # for i in lottopatt:
    #     print i[2][1:]


if __name__ == '__main__':
    print 'begin!'
    main()
    print 'stop!'
    pass
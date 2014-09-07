# -*- coding: utf-8 -*-

from models import *
import re
import urllib,urllib2


def createdatabase():
    metadata.create_all()


def dropdatabase():
    metadata.drop_all()

def getdoublechromefromurl(issuefr="2003001",issueto="20150125"):
    '''
    return [('5', '2013125', ' 04 06 08 18 25 28', '16', '89', '9', '14', '39',
     '4', '24', '10', '1', '0', '0', '3:3', '1:5', '0:6', '1:1:4',
      '2:1:3', '2:3:1', '8', '0', '2'),]   #tuple list
    '''

    from BeautifulSoup import BeautifulSoup
    #srcurl="http://zst.cjcp.com.cn/cjwssq/view/hong_zonghe-1-2013121-2013125-1.html"
    srcurl="http://zst.cjcp.com.cn/cjwssq/view/hong_zonghe-1-"+issuefr+"-"+issueto+"-1.html"
    f=urllib.urlopen(srcurl)
    html=f.read()

    # soup=BeautifulSoup(html)
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

    return patt

def getsuperlotto(issuefr="2007001",issueto="20150125"):
    '''
    return [('30', '2013125', ' 04 08 14 23 28 ', '04 08'),]   #tuple list
    '''
    lottourl="http://zst.cjcp.com.cn/cjwdlt/view/dlteqzonghe-1-"+issuefr+"-"+issueto+"-1.html"
    f2=urllib.urlopen(lottourl)
    html2=f2.read()
    lottopatt = re.findall("<td class='z_bg_05'>(?P<id>.*?)</td><td class='z_bg_05'>(?P<issue>.*?)</td><td class='WhiteBack RedFont' nowrap >(?P<redball>.*?)</td><td class='WhiteBack BlueFont'>(?P<blueball>.*?)</td>",html2,re.I)
    return  lottopatt



def insertdata():
    from sqlalchemy.orm import scoped_session, sessionmaker
    import hashlib

    userlist = [
        {'name': 'jamix' + str(i), 'address': 'pukou', 'city': 'nanj', 'img': 'http://www.baidu.com/1.png',
         'info': 'info',
         'email': 'auditor@111.com', 'ip': '127.0.0.11', 'passwd': unicode(hashlib.md5(str(i)).hexdigest(), 'utf-8'), \
         'birthday': '1980-09-10', 'province': 'jiangsu', 'sex': 1, 'status': 1}
        for i in xrange(1, 10)
    ]
    rolelist = [{'name': 'diaosi', 'description': 'this is diaosi role'},
                {'name': 'normal', 'description': 'this is normal role'}, \
                {'name': 'superadmin', 'description': 'this is superadmin role'}]
    permitlist = [{'name': 'permit' + str(i), 'description': 'this is ' + str(i) + ' permit'} for i in xrange(1, 5)]
    algolist = [{'name': 'algorithm' + str(i), 'description': 'this is ' + str(i) + 'algorithm'} for i in xrange(1, 10)]
    lottanalysislist = [{'analysis':'analysis_text' + str(i)} for i in range(1,18)]
    lotterycatlist = [{'name':'superlotto'},{'name':'doublechrom'}]

    lotterydoublechromlist = [{'lottcat_id':'2','issue':x[1],'redball':x[2][1:], \
                               'redone':x[2][1:].split(' ')[0],'redtwo':x[2][1:].split(' ')[1], \
                               'redthree':x[2][1:].split(' ')[2],'redfour':x[2][1:].split(' ')[3], \
                               'redfive':x[2][1:].split(' ')[4], \
                               'redsix':x[2][1:].split(' ')[5], \
                               'blueball':x[3], \
                               } for x in getdoublechromefromurl()]

    lotterysuperlottolist = [{'lottcat_id':'1','issue':x[1],'redball':x[2][1:-1],\
                              'redone':x[2][1:].split(' ')[0],'redtwo':x[2][1:].split(' ')[1], \
                              'redthree':x[2][1:].split(' ')[2],'redfour':x[2][1:].split(' ')[3], \
                              'redfive':x[2][1:].split(' ')[4], \
                              'blueball':x[3], \
                              'blueone':x[3].split(' ')[0], \
                              'bluetwo':x[3].split(' ')[1]\
                              } for x in getsuperlotto()]
    lotteryforecastlist = [{'lottcat_id':'2','issue':'20131001','lottanalysis_id':'1','forecastdata':'01,03,06,17,23,29:16'},
                           {'lottcat_id':'2','issue':'20131001','lottanalysis_id':'2','forecastdata':'01,04,05,14,26,30:06'},
                           {'lottcat_id':'2','issue':'20131001','lottanalysis_id':'3','forecastdata':'03,03,02,16,27,28:13'},
                           {'lottcat_id':'2','issue':'20131001','lottanalysis_id':'4','forecastdata':'01,03,05,16,23,31:14'},
                           {'lottcat_id':'2','issue':'20131001','lottanalysis_id':'5','forecastdata':'02,03,05,16,26,27:11'},
                           {'lottcat_id':'2','issue':'20131003','lottanalysis_id':'6','forecastdata':'01,03,06,11,17,31:08'},
                           {'lottcat_id':'2','issue':'20131003','lottanalysis_id':'7','forecastdata':'02,05,06,13,16,31:05'},
                           {'lottcat_id':'2','issue':'20131003','lottanalysis_id':'8','forecastdata':'01,03,06,14,17,31:07'},
                           {'lottcat_id':'2','issue':'20131003','lottanalysis_id':'9','forecastdata':'02,14,16,23,27,30:09'},
                           {'lottcat_id':'2','issue':'20131005','lottanalysis_id':'10','forecastdata':'06,08,11,12,23,27:06'},
                           {'lottcat_id':'2','issue':'20131007','lottanalysis_id':'11','forecastdata':'01,05,07,11,16,20:11'},
                           {'lottcat_id':'1','issue':'20130904','lottanalysis_id':'12','forecastdata':'11,16,20,22,26:03,05'},
                           {'lottcat_id':'1','issue':'20130904','lottanalysis_id':'13','forecastdata':'16,19,20,23,26:07,12'},
                           {'lottcat_id':'1','issue':'20130904','lottanalysis_id':'14','forecastdata':'15,16,21,22,26:10,08'},
                           {'lottcat_id':'1','issue':'20130906','lottanalysis_id':'15','forecastdata':'03,08,11,12,32:03,07'},
                           {'lottcat_id':'1','issue':'20130906','lottanalysis_id':'16','forecastdata':'07,09,12,18,22:01,08'},
                           {'lottcat_id':'1','issue':'20130906','lottanalysis_id':'17','forecastdata':'01,06,11,12,32:13,18'},
                           ]
    session = scoped_session(sessionmaker(bind=engine))
    try:
        session.execute(User.__table__.insert(), userlist)
        session.execute(Algorithm.__table__.insert(), algolist)
        session.execute(Permit.__table__.insert(), permitlist)
        session.execute(Role.__table__.insert(), rolelist)
        session.execute(Lotterycat.__table__.insert(),lotterycatlist)
        session.execute(Lotterydoublechrom.__table__.insert(),lotterydoublechromlist)
        session.execute(Lotterysuperlotto.__table__.insert(),lotterysuperlottolist)
        session.execute(Lottanalysis.__table__.insert(),lottanalysislist)
        session.execute(Lotteryforecast.__table__.insert(),lotteryforecastlist)

        user = User(name='admin', passwd=unicode(hashlib.md5('admin').hexdigest(), 'utf-8'), email='admin@site.com')
        role = Role(name='admin', description='this is admin role')
        user.roles.append(role)
        session.add(user)                 # INSERT INTO administrator  user/password = admin/admin

        permit1 = session.query(Permit).filter(Permit.name == 'permit1').one()
        permit2 = session.query(Permit).filter(Permit.name == 'permit2').one()
        role1 = session.query(Role).filter(Role.name == 'diaosi').one()
        role1.permits.append(permit1)
        role2 = session.query(Role).filter(Role.name == 'normal').one()
        role2.permits.append(permit2)

        algorithm1 = session.query(Algorithm).filter(Algorithm.name == 'algorithm1').one()
        algorithm2 = session.query(Algorithm).filter(Algorithm.name == 'algorithm2').one()
        session.query(Permit).filter(Permit.name == 'permit1').one().algorithms.append(algorithm1)
        session.query(Permit).filter(Permit.name == 'permit1').one().algorithms.append(algorithm2)

        algorithm3 = session.query(Algorithm).filter(Algorithm.name == 'algorithm3').one()
        algorithm4 = session.query(Algorithm).filter(Algorithm.name == 'algorithm4').one()
        algorithm5 = session.query(Algorithm).filter(Algorithm.name == 'algorithm5').one()
        session.query(Permit).filter(Permit.name == 'permit2').one().algorithms.append(algorithm3)
        session.query(Permit).filter(Permit.name == 'permit2').one().algorithms.append(algorithm4)
        session.query(Permit).filter(Permit.name == 'permit2').one().algorithms.append(algorithm5)

        session.commit()
    except Exception as e:
        print str(e)
        session.rollback()
    finally:
        session.close()


def initialdatabase():
    dropdatabase()
    createdatabase()
    insertdata()


if __name__ == '__main__':
    initialdatabase()
    # from sqlalchemy.engine import reflection
    # print reflection.Inspector.from_engine(engine).get_table_names()

    # from sqlalchemy.orm import scoped_session, sessionmaker
    # session = scoped_session(sessionmaker(bind=engine))
    # try:
    #     # role = session.query(Role).filter(Role.name == 'admin').one()
    #     # usr = session.query(User).filter(User.name == 'jamix1').one()
    #     # usr.roles.append(role)            #when  role has exist in user_role table,it wont exec insert or update(actually do nothing on database)
    #     session.commit()
    # except Exception as e:
    #     print str(e)
    #     session.rollback()
    # finally:
    #     res = session.query(User).join(UserRole.user)
    #     print res[0].name, res[0].email
    #     session.close()


        # from sqlalchemy.engine import *
        # from sqlalchemy.sql import select,text
        # conn = engine.connect()

        # cmd = select([Algorithm])
        # res=conn.execute(cmd)


# -*- coding: utf-8 -*-
__author__ = 'ifcheung'
import unittest
import time
from models import metadata,engine
from models import User,UserRole,Role,Permit,Algorithm
from models.repository import *
from models.model import *
from sqlalchemy.orm import scoped_session, sessionmaker

import hashlib

class UserQueryTestCase(unittest.TestCase):
    def setUp(self):
        self.session = scoped_session(sessionmaker(bind=engine))
        self.model=User

    @property
    def query(self):
        return self.session.query(self.model)

    def tearDown(self):
        self.model=None
        self.session.close()

    def test_isadmin(self):
        value='admin'
        expectuser = self.session.query(User.id,User.name,User.email).filter(self.model.passwd=='21232f297a57a5a743894a0e4a801fc3').one()

        self.assertEqual(expectuser.name,value)

    # def test_removeuser(self):
    #     user=User(id=11)
    #     rep = user_repository(self.session)
    #     rep.removeuserdelrole(user)

    def test_getuserroles(self):
        user=User(id=12)
        rep = user_repository(self.session)
        self.assertEqual(len(rep.getuserroles(user)),2)

    def test_getuseralgorithm(self):
        # usr=User(id=12)

        # algos2 = self.session.query(UserRole)\
        #     .join(RolePermit.role)\
        #     .filter(UserRole.user  == usr ).count()
        # al = self.session.execute(text("select * from user where id=:param"),{"param":12})
        algos3=self.session.query(User)
        res = algos3.column_descriptions


def suite1():
    suite = unittest.TestSuite()
    # suite.addTest(UserQueryTestCase("test_isadmin"))
    # suite.addTest(UserQueryTestCase("test_getuserroles"))
    suite.addTest(UserQueryTestCase("test_getuseralgorithm"))
    return suite


##reference:http://www.cnblogs.com/hyddd/archive/2009/05/30/1492536.html
def testselenium():
    # from selenium.webdriver.firefox.webdriver import  WebDriver
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.common.exceptions import NoSuchElementException
    browser = webdriver.Ie()

    #register
    browser.get("http://221.226.175.204:6888/easportal")
    name = browser.find_element_by_name("username")
    name.send_keys("001950" )
    passwd = browser.find_element_by_name("password")
    passwd.send_keys("8888")

    time.sleep(0.2)
    try:
        browser.find_element_by_id('loginSubmit').click()
    except NoSuchElementException:
        assert 0, "can't find seleniumname"
    time.sleep(1)

    #goto index.html  but it will redirect to loginurl
    # browser.find_element_by_xpath("//a[contains(@href,'/')]").click()

    #login
    # time.sleep(1)
    # element1 = browser.find_element_by_name("name")
    # element1.send_keys("admin" )
    # passwd1 = browser.find_element_by_name("passwd")
    # passwd1.send_keys("admin" + Keys.RETURN)


    time.sleep(5)

    browser.close()
    browser.quit()



if __name__ == '__main__':
    # unittest.main(defaultTest='suite1')
    testselenium()
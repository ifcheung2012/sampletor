# -*- coding: utf-8 -*-
from  models.model import *
import hashlib


class BaseRepository(object):
    def __init__(self, db):
        self.session = db

    def load(self, Entity, id):
        return self.session.query(Entity).filter(Entity.id == id).first()

    def save(self, instance):
        try:
            self.session.add(instance)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
        finally:
            self.session.close()

    def remove(self, instance):
        try:
            self.session.delete(instance)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
        finally:
            self.session.close()

    def list(self, Entity):
        return self.session.query(Entity).all()

    '''
        relationattrname : attribute name of an instance ,type string
        relateEntities  : a list of relateEntities, type list,
        example:
        user = User(name='foo')
        func(user,'roles',[Role(name='admin'),Role(id=5)]
    '''

    def _add_or_update_relation(self, instance, relationattrname, relateEntities):
        if not hasattr(instance, relationattrname):
            return
        try:
            for relation in relateEntities:
                getattr(instance, relationattrname).append(relation)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
        finally:
            self.session.close()


class user_repository(BaseRepository):
    def searchbyname(self, name):
        return self.session.query(User).filter(User.name.like('%' + name + '%')).all()

    def getsinglebyname(self,name):
        return self.session.query(User).filter(User.name == name).first()

    def validateuser(self, username, userpasswd):
        usr = self.session.query(User).filter(User.name == username). \
            filter(User.passwd == unicode(hashlib.md5(userpasswd).hexdigest(), 'utf-8'))\
            .first()
        if usr == None:
            return
        return usr.name, len(usr.roles)


    def save(self, instance):
        instance.passwd= unicode(hashlib.md5(instance.passwd).hexdigest(), 'utf-8')
        super(user_repository,self).save(instance)
        

    def saveuseraddrole(self,user,rolenamelist):
        usr = self.session.query(User).filter(User.name == user.name).first()
        if usr:
            return None
        user.passwd= unicode(hashlib.md5(user.passwd).hexdigest(), 'utf-8')
        try:
            self.session.add(user)
            rolelist = self.session.query(Role).filter(Role.name.in_(rolenamelist))
            for role in rolelist:
                user.roles.append(role)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
        finally:
            self.session.close()
        return True

    def checkuserexists(self,user):
        usr =  self.session.query(User).filter(User.name == user.name).first()
        return usr

    def removeuserdelrole(self,user):
        try:
            user=self.session.query(User).filter(User.id==user.id).one()
            self.session.query(UserRole).filter(UserRole.user==user).delete()
            self.session.delete(user)
            self.session.commit()

        except Exception as e:
            print str(e)
            self.session.rollback()
        finally:
            self.session.close()

    def _addroles(self, user, rolenamelist):
        rlist = []
        rolenamelist = self.session.query(Role).filter(Role.name.in_(rolenamelist))
        rlist = [ role for role in rolenamelist]

        self._add_or_update_relation(user, 'roles', rlist)

    def getuserroles(self,user):
        usr = self.session.query(User).filter(User.id == user.id).one()
        return usr.roles

    def getuserpermit(self,user):
        usr = self.session.query(User).filter(User.id == user.id).one()
        roles = self.getuserroles(user)
        permitlist = []
        for r in roles:
            permit = self.session.query(RolePermit).filter(RolePermit.role == r.id)
            permitlist.append(permit)
        self.session.query(UserRole)\
            .join(RolePermit,UserRole.roles)\
            .join(PermitAlgo,RolePermit.permit)\
            .join(Algorithm,PermitAlgo.algorithm)\
            .filter(UserRole.user_id == user.id)
        return permitlist

    def getuseralgorithms(self,user):
        algolist = self.session.query(User.id,Algorithm.id,Algorithm.name) \
            .join(UserRole)\
            .join(Role)\
            .join(RolePermit) \
            .join(Permit)\
            .join(PermitAlgo) \
            .join(Algorithm) \
            .filter(User.id == user.id).all()
        return algolist


class userrole_repository(BaseRepository):
    pass


class role_repository(BaseRepository):
    pass


if __name__ == '__main__':

    pass
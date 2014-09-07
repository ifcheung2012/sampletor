# -*- coding: utf-8 -*-
#autogenerated by sqlautocode

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation
from datetime import datetime

engine = create_engine('mysql+mysqldb://root:123@localhost:3306/ifcheung', echo=True,pool_recycle = -1)
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata
metadata.bind = engine

permit_algo = Table(u'permit_algo', metadata,
                    Column(u'id', INTEGER(), primary_key=True, nullable=False),
                    Column(u'permit_id', INTEGER(), ForeignKey('permit.id'), nullable=False),
                    Column(u'algo_id', INTEGER(), ForeignKey('algorithm.id'), nullable=False),
                    Column(u'status', INTEGER(), default=0),
                    Column(u'rmv', INTEGER(), default=0),
                    Column(u'created', DateTime,default=datetime.now()),
)

role_permit = Table(u'role_permit', metadata,
                    Column(u'id', INTEGER(), primary_key=True, nullable=False),
                    Column(u'permit_id', INTEGER(), ForeignKey('permit.id'), nullable=False),
                    Column(u'role_id', INTEGER(), ForeignKey('role.id'), nullable=False),
                    Column(u'status', INTEGER(), default=0),
                    Column(u'rmv', INTEGER(), default=0),
                    Column(u'created', DateTime,default=datetime.now()),
)

user_role = Table(u'user_role', metadata,
                  Column(u'id', INTEGER(), primary_key=True, autoincrement=True, nullable=False),
                  Column(u'user_id', INTEGER(), ForeignKey('user.id'), nullable=False),
                  Column(u'role_id', INTEGER(), ForeignKey('role.id'), nullable=False),
                  Column(u'status', INTEGER(), default=0),
                  Column(u'rmv', INTEGER(), default=0),
                  Column(u'created', DateTime,default=datetime.now()),
)

class Algorithm(DeclarativeBase):
    __tablename__ = 'algorithm'

    __table_args__ = {}

    #column definitions

    id = Column(u'id', INTEGER(), primary_key=True, autoincrement=True, nullable=False)
    name = Column(u'name', VARCHAR(length=20), nullable=False)

    description = Column(u'description', VARCHAR(length=100))

    status = Column(u'status', INTEGER(), default=0)
    rmv = Column(u'rmv', INTEGER(), default=0)
    created = Column(u'created', DateTime,default=datetime.now())
    #relation definitions
    permits = relation('Permit', primaryjoin='Algorithm.id==PermitAlgo.algo_id', secondary=permit_algo,
                       secondaryjoin='PermitAlgo.permit_id==Permit.id')


class Permit(DeclarativeBase):
    __tablename__ = 'permit'

    __table_args__ = {}

    #column definitions

    id = Column(u'id', INTEGER(), primary_key=True, autoincrement=True, nullable=False)
    name = Column(u'name', VARCHAR(length=20), nullable=False)

    description = Column(u'description', VARCHAR(length=100))

    status = Column(u'status', INTEGER(), default=0)
    rmv = Column(u'rmv', INTEGER(), default=0)
    created = Column(u'created', DateTime,default=datetime.now())
    #relation definitions
    algorithms = relation('Algorithm', primaryjoin='Permit.id==PermitAlgo.permit_id', secondary=permit_algo,
                          secondaryjoin='PermitAlgo.algo_id==Algorithm.id')
    roles = relation('Role', primaryjoin='Permit.id==RolePermit.permit_id', secondary=role_permit,
                     secondaryjoin='RolePermit.role_id==Role.id')


class PermitAlgo(DeclarativeBase):
    __table__ = permit_algo

    #relation definitions
    algorithm = relation('Algorithm', primaryjoin='PermitAlgo.algo_id==Algorithm.id')
    permit = relation('Permit', primaryjoin='PermitAlgo.permit_id==Permit.id')


class Role(DeclarativeBase):
    __tablename__ = 'role'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', INTEGER(), primary_key=True, autoincrement=True, nullable=False)
    name = Column(u'name', VARCHAR(length=20), nullable=False)

    description = Column(u'description', VARCHAR(length=100))

    status = Column(u'status', INTEGER(), default=0)
    rmv = Column(u'rmv', INTEGER(), default=0)
    created = Column(u'created', DateTime,default=datetime.now())
    #relation definitions
    permits = relation('Permit', primaryjoin='Role.id==RolePermit.role_id', secondary=role_permit,
                       secondaryjoin='RolePermit.permit_id==Permit.id')
    users = relation('User', primaryjoin='Role.id==UserRole.role_id', secondary=user_role,
                     secondaryjoin='UserRole.user_id==User.id')


class RolePermit(DeclarativeBase):
    __table__ = role_permit


    #relation definitions
    permit = relation('Permit', primaryjoin='RolePermit.permit_id==Permit.id')
    role = relation('Role', primaryjoin='RolePermit.role_id==Role.id')


class User(DeclarativeBase):
    __tablename__ = 'user'

    __table_args__ = {}

    #column definitions
    id = Column(u'id', INTEGER(), primary_key=True, autoincrement=True, nullable=False)
    name = Column(u'name', VARCHAR(length=50), nullable=False)
    passwd = Column(u'passwd', VARCHAR(length=50), nullable=False)
    email = Column(u'email', VARCHAR(length=50), nullable=False)

    sex = Column(u'sex', INTEGER())
    birthday = Column(u'birthday', VARCHAR(length=50))
    img = Column(u'img', VARCHAR(length=255))
    info = Column(u'info', VARCHAR(length=500))

    province = Column(u'province', VARCHAR(length=50))
    city = Column(u'city', VARCHAR(length=50))
    address = Column(u'address', VARCHAR(length=50))

    ip = Column(u'ip', VARCHAR(length=15))
    last_ip = Column(u'last_ip', VARCHAR(length=15))

    status = Column(u'status', INTEGER(), default=0)
    rmv = Column(u'rmv', INTEGER(), default=0)

    created = Column(u'created', DateTime,default=datetime.now())

    #relation definitions
    roles = relation('Role', primaryjoin='User.id==UserRole.user_id', secondary=user_role,
                     secondaryjoin='UserRole.role_id==Role.id')


class UserRole(DeclarativeBase):
    __table__ = user_role

    #relation definitions
    user = relation('User', primaryjoin='UserRole.user_id==User.id')
    role = relation('Role', primaryjoin='UserRole.role_id==Role.id')


class Lotterycat(DeclarativeBase):
    __tablename__ = 'lottcat'

    id = Column(u'id',INTEGER(),primary_key=True,autoincrement=True,nullable=False)
    name = Column(u'name', VARCHAR(length=20), nullable=False)
    created = Column(u'created', DateTime,default=datetime.now())
    rmv = Column(u'rmv', INTEGER(), default=0)

class Lotteryforecast(DeclarativeBase):
    __tablename__ = 'lottforecast'

    id = Column(u'id',INTEGER(),primary_key=True,autoincrement=True,nullable=False)

    lottcat_id = Column(u'lottcat_id', INTEGER(), ForeignKey('lottcat.id'), nullable=False)
    lottanalysis_id = Column(u'lottanalysis_id', INTEGER(), ForeignKey('lottanalysis.id'), nullable=False)
    issue = Column(u'issue',INTEGER(),  nullable=False)
    forecastdata = Column(u'forecastdata',VARCHAR(length=20),nullable=True)
    created = Column(u'created', DateTime,default=datetime.now())
    rmv = Column(u'rmv', INTEGER(), default=0)


class Lotterydoublechrom(DeclarativeBase):
    __tablename__ = 'lotterydoublechrom'
    id = Column(u'id',INTEGER(),primary_key=True,autoincrement=True,nullable=False)
    lottcat_id = Column(u'lottcat_id', INTEGER(), ForeignKey('lottcat.id'), nullable=False)
    issue = Column(u'issue',VARCHAR(length=20),nullable=False)
    opendate = Column(u'opendate', Date,default=datetime.today())
    redball  = Column(u'redball',VARCHAR(length=20),nullable=False)
    redone   = Column(u'redone',VARCHAR(length=2),nullable=False)
    redtwo   = Column(u'redtwo',VARCHAR(length=2),nullable=False)
    redthree = Column(u'redthree',VARCHAR(length=2),nullable=False)
    redfour  = Column(u'redfour',VARCHAR(length=2),nullable=False)
    redfive  = Column(u'redfive',VARCHAR(length=2),nullable=False)
    redsix   = Column(u'redsix',VARCHAR(length=2),nullable=False)
    blueball = Column(u'blueball',VARCHAR(length=2),nullable=False)
    created = Column(u'created', DateTime,default=datetime.now())
    rmv = Column(u'rmv', INTEGER(), default=0)

class Lotterysuperlotto(DeclarativeBase):
    __tablename__ = 'lotterysuperlotto'
    id = Column(u'id',INTEGER(),primary_key=True,autoincrement=True,nullable=False)
    lottcat_id = Column(u'lottcat_id', INTEGER(), ForeignKey('lottcat.id'), nullable=False)
    issue = Column(u'issue',VARCHAR(length=20),nullable=False)
    opendate = Column(u'opendate', Date,default=datetime.today())
    redball  = Column(u'redball',VARCHAR(length=20),nullable=False)
    redone   = Column(u'redone',VARCHAR(length=2),nullable=False)
    redtwo   = Column(u'redtwo',VARCHAR(length=2),nullable=False)
    redthree = Column(u'redthree',VARCHAR(length=2),nullable=False)
    redfour  = Column(u'redfour',VARCHAR(length=2),nullable=False)
    redfive  = Column(u'redfive',VARCHAR(length=2),nullable=False)
    blueball = Column(u'blueball',VARCHAR(length=8),nullable=False)
    blueone  = Column(u'blueone',VARCHAR(length=2),nullable=False)
    bluetwo  = Column(u'bluetwo',VARCHAR(length=2),nullable=False)
    created = Column(u'created', DateTime,default=datetime.now())
    rmv = Column(u'rmv', INTEGER(), default=0)

class Lottanalysis(DeclarativeBase):
    __tablename__ = 'lottanalysis'
    id = Column(u'id',INTEGER(),primary_key=True,autoincrement=True,nullable=False)
    created = Column(u'created', DateTime,default=datetime.now())
    analysis  = Column(u'analysis',Text,nullable=False)
    rmv = Column(u'rmv', INTEGER(), default=0)









if __name__ == '__main__':
    usr = User(id=12)
    from sqlalchemy.orm.collections import InstrumentedList
    from models import metadata,engine
    from sqlalchemy.orm import scoped_session, sessionmaker
    session = scoped_session(sessionmaker(bind=engine))
    algos = session.query(User.id,Algorithm.id,Algorithm.name) \
        .join(UserRole)\
        .join(Role)\
        .join(RolePermit) \
        .join(Permit)\
        .join(PermitAlgo) \
        .join(Algorithm) \
        .filter(User.id == usr.id).all()

    print type(algos),algos
    # print getattr(usr, "roles")
    # print isinstance(usr, DeclarativeBase)
    # print type(usr) is DeclarativeBase, type(usr.roles) is InstrumentedList

# sqlalchemy.orm.collections.InstrumentedList


#encoding: utf-8

DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = '12345'
HOST ='127.0.0.1'
PORT='3306'
DATABASE='mqq'
DEBUG = True
SQLALCHEMY_DATABASE_URI="{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD,HOST
                                             ,PORT,DATABASE)


SQLALCHEMY_TRACK_MODIFICATIONS=False
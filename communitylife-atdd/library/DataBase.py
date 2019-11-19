#coding=utf-8
import pymysql
import configparser
class DataBase():
    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read("../conf/config.ini")
        self.host = conf.get("DataBase", "host")
        self.port = int(conf.get("DataBase", "port"))
        self.user = conf.get("DataBase", "user")
        self.password = conf.get("DataBase", "password")
        self.move=conf.get("DataBase","move")
        self.clean = conf.get("DataBase", "clean")
        self.broadband = conf.get("DataBase", "broadband")
    def connect_base(self,db):

        print(self.host,self.port,self.user,self.password,db)
        # if service == 1:
        #     print("连接搬家数据库")
        # elif service == 2:
        #     print("链接保洁数据库")
        #
        # elif service ==3:
        #     print("连接宽带数据库")
        #
        # else:
        #     print("输入参数值错误！1 搬家 2 保洁 3 宽带")
        try:
            print(22222)

            db = pymysql.connect(host=self.host, port=self.port,user=self.user, passwd=self.password, database=db)
            cursor = db.cursor()


        except Exception as e:
            print(e)
        else:
            print(11111)
            con=pymysql.connect(host='m10038.mars.test.mysql.ljnode.com',port=self.port,user='root',password='b0C123a6fd',database='ke_move',charset='utf8')
if __name__=="__main__":
    DataBase().connect_base(db='ke_move')

#coding=utf-8
import pymysql
import configparser
class DataBase():
    def __init__(self):
        self.conf = configparser.ConfigParser()
        self.conf.read("../conf/config.ini")
        self.host = self.conf.get("DataBase", "host")
        self.port = int(self.conf.get("DataBase", "port"))
        self.user = self.conf.get("DataBase", "user")
        self.password = self.conf.get("DataBase", "password")
        self.move=self.conf.get("DataBase","move")
        self.clean = self.conf.get("DataBase", "clean")
        self.broadband = self.conf.get("DataBase", "broadband")
    def connect_base(self,service):

        print(self.host,self.port,self.user,self.password,service)
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
            db = pymysql.connect(host=self.host, user=self.user, password=self.password, db=service)
            cursor = db.cursor()

        except Exception as e:
            print(e)
        else:
            print(11111)
            con=pymysql.connect(host='m10038.mars.test.mysql.ljnode.com',user='root',password='b0C123a6fd',db='ke_move',charset='utf8')
if __name__=="__main__":
    DataBase().connect_base(service=1)

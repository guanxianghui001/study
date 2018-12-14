#coding: utf-8
import smtplib
#添加附件
import time
from email.mime.multipart import MIMEMultipart
import configparser
from email.header import Header
# 添加邮件内容
from email.mime.text import MIMEText
def send_Mail():
    conf = configparser.ConfigParser()
    conf.read("config.ini")
    smtp= smtplib.SMTP('smtp.163.com')
    sender=conf.get("email","sender")
    receiver=conf.get("email","receiver")
    password=conf.get("email","password")
    print(sender)
    print(receiver)
    login=smtp.login(sender,password)
    print(login)
    try:
        msg=MIMEMultipart()
        text=MIMEText(mail_body,'html','utf-8')
        msg.attach(text)
        msg_file=MIMEText(mail_body,'html','utf-8')
        current_time=time.strftime('%y-%m-%d')
        msg_file['content-Type']='application/octet-stream'
        msg_file['Content-Disposition']='attachment;filename="%s测试报告 .html'%current_time
        msg['Subject']=Header('接口自动化测试报告结果','utf-8')
        msg['From']=sender
        msg['To']=','.join(receiver)
        msg.attach(msg_file)
        smtp.sendmail(sender,receiver,msg.as_string())
        smtp.quit()
    except smtplib.SMTPException as e:
        print(str(e))
send_Mail()
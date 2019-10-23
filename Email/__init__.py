import configparser
conf = configparser.ConfigParser()
conf.read(r"C:\Users\guanxianghui001\Desktop\学习\testDemo\Email\config.ini")
sender=conf.get("email","sender")
print(sender)
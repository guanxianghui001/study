#coding=utf-8
class Person(object):
    def __init__(self,name,age):
        self._name=name
        self._age=age
        #访问器 -getter方法
        @property
        def name(self):
            return self._name
        #f访问器-setter方法
        @property
        def age(self):
            return self._age
        #修改器-setter方法
        @age.setter
        def age(self,age):
            self._age=age
    def play(self):
        if self._age <= 16:
            print('%d你还小！'% self._age)
        else:
            print('%d你已经不小了！' %self._age)
def main():
    person=Person('花花',14)
    person.play()
    person.age=22
    person.play()
if __name__=='__main__':
    main()


class Student:
    pass


# 或者
class Developer(object):
    # 定义类属性
    name = 'WuXiaolong'
    site = 'http://wuxiaolong.me/'

    # 变量名两个下划线开头，定义私有属性, 这样在类外部无法直接进行访问，类的私有方法也是如此
    __sex = 0

    # 定义构造方法，对象的方法
    def __init__(self, name, site, sex):
        self.name = name
        self.site = site
        self.__sex = sex

    # 类方法
    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex


if __name__ == '__main__':
    # 实例化类
    developer = Developer('wxl', 'http://wuxiaolong.me/', 1)  # 实例变量
    print(developer.site, developer.get_sex())  # 访问类的属性和方法

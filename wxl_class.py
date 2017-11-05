class Student:
    pass


# 或者
class Developer(object):
    # 定义类属性
    name = 'WuXiaolong'
    site = 'http://wuxiaolong.me/'

    # 变量名两个下划线开头，定义私有属性, 这样在类外部无法直接进行访问，类的私有方法也是如此
    __sex = 0

    # 定义构造方法
    def __init__(self, name, site, sex):
        self.name = name
        self.site = site
        self.__sex = sex

    # 类方法
    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex


# 单继承
class AndroidCoder(Developer):
    coder_id = 1024

    # 定义构造方法
    def __init__(self, name, site, sex, coder_id):
        # 调用父类构造方法
        # Developer.__init__(self, name, site, sex) # 老办法
        super(AndroidCoder, self).__init__(name, site, sex)  # 采用新式类
        self.coder_id = coder_id

    # 重写父类的方法
    def set_sex(self, sex):
        self.__sex = sex
        print('这是个秘密')

    def get_sex(self):
        return self.__sex


class JavaCoder(object):
    java_id = 1

    # 定义构造方法
    def __init__(self, java_id):
        self.java_id = java_id
        print('来自JavaCoder')


# 多继承，B 继承 A，C 继承 B
class PythonCoder(AndroidCoder):
    # 定义构造方法
    def __init__(self, name, site, sex, coder_id):
        # 调用父类构造方法
        super(PythonCoder, self).__init__(name, site, sex, coder_id)


class FullStackCoder(AndroidCoder, JavaCoder):
    # 定义构造方法
    def __init__(self, name, site, sex, coder_id):
        # 调用父类构造方法
        super(FullStackCoder, self).__init__(name, site, sex, coder_id)
        JavaCoder.__init__(self, coder_id)  # 这里需要使用老办法


# 调用：
if __name__ == '__main__':
    pass
    # 实例化类
    developer = Developer('wxl', 'http://wuxiaolong.me/', 1)  # 实例化成变量
    print(developer.site, developer.get_sex())  # 访问类的属性和方法

    # 单继承
    androidCoder = AndroidCoder('wxl', 'http://wuxiaolong.me/', 1, 520)
    print(androidCoder.set_sex(2))

    pythonCoder = PythonCoder('wxl', 'http://wuxiaolong.me/', 1, 1024)
    print(androidCoder.get_sex())

    fullStackCoder = FullStackCoder('wxl', 'http://wuxiaolong.me/', 1, 1024)

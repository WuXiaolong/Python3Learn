# 导入模块
import wxl_class

from wxl_def import hello

developer = wxl_class.Developer('wxl', 'http://wuxiaolong.me/', 1)  # 实例变量
print(developer.site, developer.get_sex())

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

m = hello(666, 999)
print(m)

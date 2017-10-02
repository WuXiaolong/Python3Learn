try:
    name = 'wxl'
    print(int(name))
except ValueError as e:  # 所有的错误类型都继承自BaseException
    print(e)
finally:
    print('finally')

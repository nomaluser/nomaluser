while True:
    change = (input('选择你想转换的进制\n1. 八进制 2. 十六进制 3. 二进制 4.十进制\n'))
    if change == '1' or '一':
        num1 = int(input('请选择你想要转化的数字= '))
        print('转化成功，结果为{}'.format(oct(num1)))
    elif change == '2' or '二':
        num2 = int(input('请选择你想要转化的数字= '))
        print('转化成功，结果为{}'.format(hex(num2)))
    elif change == '3' or '三':
        num3 = int(input('请选择你想要转化的数字= '))
        print('转化成功，结果为{}'.format(bin(num3)))
    elif change == '4' or '四':
        num4 = int(input('请选择你想要转化的数字= '))
        print('转化成功，结果为{}'.format(int(num4)))
    else:
        print("请输入正确的代号")

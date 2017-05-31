#coding=utf-8
val = raw_input("请输入温度:")
if val[-1] in ['C','c']:
    f = 1.8 *eval(val[0:-1]) + 32
    print("converted temperature is:%.2fF"%f)
elif val[-1] in ['F','f']:
    c = (eval(val[0:-1]) -32) /1.8
    print("converted temperature is:%.2fC"%c)
else:
    print("input wrong")

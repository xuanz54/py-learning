def str_reverse(s):
    s=s[::-1]
    return s
def substr(s,x,y):
    s=s[x:y:1]
    return s

if __name__ == '__main__': # 卸载main里面的单元测试 不会被导入的程序调用
    print(str_reverse('dxz')) # zxd
    print(substr('qwerty',2,5)) # ert
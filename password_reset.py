password = 'a123456'
n = 3 #剩餘機會
while n > 0:
    pwd = input('請輸入密碼: ')
    n = n - 1
    if pwd == password:
        print('登入成功!')
        break #逃出迴圈
    else:
        print('密碼錯誤!')
        if n > 0:
            print('還有', n, '次機會')
        else:
            print('要鎖帳號了喔！')

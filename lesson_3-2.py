# Дана строка S. Нужно распечатать её подстроками длиной w. Например S=”ABCDEFGHIJKLIMNOQRSTUVWXYZ” и w=4 - выход
#
# ABCD
#
# EFGH
#
# IJKL
#
# IMNO
#
# QRST
#
# UVWX
#
# YZ
s=input('введите строку')
w=int(input('по сколько разбивать'))
i=0
while i<=len(s):
    print(s[i:i+w])
    i+=w
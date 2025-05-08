# 云影密码
a="8842101220480224404014224202480122"
s=a.split('0')
l=[]
print(s)
for i in s:
    sum=0
    for j in i:
        sum+=eval(j)
    l.append(chr(sum+64))
print(l)
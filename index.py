import re
file=open('../mbox.txt','r')
email=[]
for line in file:
    search=re.findall('\S*@+\S*',line)
    if len(search)>0:
        email.append(search)
for mail in email:
    if re.search('[<>;)]',''.join(mail)):
        fix=re.sub('[<>;)]','',''.join(mail))
        print(fix)
    else:
        print(''.join(mail))
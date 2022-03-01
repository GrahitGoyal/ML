l='hello world@ 123'
w=[]
for i in l:
    w.append(i)
y=['1','2','3','4','5','6','7','8','9','0']
countn=0
counta=0
for j in w:
    if j.isalpha():
        counta = counta+1
    elif j in y :
        countn = countn+1
    else :
        print('')
print('Alphabets :',counta)
print('digits :',countn)
    

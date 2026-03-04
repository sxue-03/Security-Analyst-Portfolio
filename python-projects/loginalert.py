count = 0 
threshold = 3 
for line in open('auth.log','r'):
    if 'Failed login' in line:
        count+=1
if count > threshold:
    print('ALERT: Too many failed logins:', count)
else:
    print('Failed logins:', count)
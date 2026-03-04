password = input("enter password:")
score=0

if len(password) >= 8:
    print("long enough")
    score +=1
else:
    print("too short")

if any(c.isupper() for c in password):
    print("has upper")
    score +=1
else:
    print("no uppercase")

if any(c.islower() for c in password):
    print("has lower")
    score +=1
else:
    print("no lowercase")

if any(c.isdigit() for c in password):
    print("has digit")
    score +=1
else:
    print("no digit")

special="!@#@$"

if any(c in special for c in password):
    print("has special")
    score +=1
else:
    print("no special")

if score<=2:
    print('weak')
elif score<=4:
    print('medium')
else:
    print('strong')
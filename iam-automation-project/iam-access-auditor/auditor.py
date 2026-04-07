import csv
import datetime 
with open('users.csv') as file:
    reader = csv.DictReader(file)
    today = datetime.date.today()
    inactive_users = []
    never_logged_in = []
    disabled_accounts = []
    admin_review = []
    total_users = 0
    for row in reader:
        
        total_users+=1
        if row['last_login'] == '':
            never_logged_in.append(row['username'])
        else:
            last_login = datetime.date.fromisoformat(row['last_login'])
            day_inactive = (today - last_login).days
            if day_inactive > 90:
                inactive_users.append(row['username'])
        if row['status'] == 'disabled':
            disabled_accounts.append(row['username'])
        if row['is_admin'] == 'True':
            admin_review.append(row['username'])
    print('===== IAM AUDIT REPORT =====')
    flagged = set(inactive_users + never_logged_in + disabled_accounts + admin_review)
    print('Total users:', total_users)
    print('Flagged accounts:', len(flagged))
    print('INACTIVE (90+ days):', inactive_users)
    print('NEVER LOGGED IN:', never_logged_in)
    print('DISABLED ACCOUNTS:', disabled_accounts)
    print('ADMIN REVIEW:', admin_review)
    
    

    



        
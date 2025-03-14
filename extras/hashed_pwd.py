'''
This is a Dummy File which is supposed to justify the values that have been stored in the "Password" field in the clinicians database.

I am Hashing the passwords and then storing them into the database, enabling security and avoiding password leaks and easy access.

Since I have Hashed the passwords directly before storing in the API code, I need to separately hash the dummy data passwords, and this is the Justification for the Same.
'''

from utils.security import hash_password, check_password


password = {"pwjoel87": "", "pwshiminh": "", "pwrishiaw": ""}

for i in password:
    hashed_pwd = hash_password(i)
    password[i] = hashed_pwd

    print(f'Hash: {hashed_pwd}, check: {check_password(hashed_pwd, i)}')

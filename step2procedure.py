# -*- coding: utf-8 -*-
import re


def valid_user(login):
    login = str(login).strip()
    if not 21 > len(login) > 0:
        return False

    if len(login) == 1 and re.search(r'^[a-z]$', login, re.IGNORECASE):
        return True

    if re.search(r'^[a-z]+([a-z0-9-.]+)?[a-z0-9]+$', login, re.IGNORECASE):
        return True

    return False

if __name__ == '__main__':

    # False
    print(valid_user('.'))
    print(valid_user('-'))
    print(valid_user(1))
    print(valid_user('ss123456789123467-.'))
    print(valid_user('ss12345678912-3.467sd'))

    # True
    print(valid_user('s'))
    print(valid_user('s1'))
    print(valid_user('ss12345678912-3.467'))
    print(valid_user('ss12345678912-3.467s'))

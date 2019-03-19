def fun(s):
    # return True if s is a valid email, else return False
    try:
        s = split('@')
        username = s[0]
        web = s[1].split('.')[0]
        extension = s[1].split('.')[1]
    except Exception as e:
        return False
    if len(extension) > 3:
        return False
    elif not web.isalnum():
        return False
    elif not username.replace('_','').replace('-','').isalnum():
        return False
    else:
        return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
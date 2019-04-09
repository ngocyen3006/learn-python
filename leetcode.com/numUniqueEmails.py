# https://leetcode.com/problems/unique-email-addresses/


def numUniqueEmails(emails):
    list_email = set()
    for email in emails:
        local, domain = email.split('@')
        local = local.replace('.', '').split('+')[0]
        list_email.add(local + '@' + domain)
    return len(list_email)


def test():
    print(numUniqueEmails(["test.email+alex@leetcode.com",
                           "test.e.mail+bob.cathy@leetcode.com",
                           "testemail+david@lee.tcode.com"]))


if __name__ == '__main__':
    test()

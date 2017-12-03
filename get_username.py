import ldap
from datetime import datetime, timedelta
from properties import *

def connect_to_ad():
    l = ldap.initialize(ldap_srv)
    l.simple_bind_s(ldap_user, ldap_pass)
    return l

# find users with last-login over 180 days
def find_users_old_login(ad):
    try:
        return ad.search_s(base, ldap.SCOPE_SUBTREE, filters, ['SamAccountName', 'lastLogonTimestamp', 'lastlogon'])
    except IndexError:
        print 'IndexError Exception'
        exit()

def convert_ad_timestamp(timestamp):
    epoch_start = datetime(year=1601, month=1, day=1)
    seconds_since_epoch = timestamp / 10 ** 7
    return epoch_start + timedelta(seconds=seconds_since_epoch)

def run():
    ad = connect_to_ad()
    response = find_users_old_login(ad)
    for line in response:
        users_attributes = line[1]
        for user_attribute in users_attributes:
            print type(user_attribute)
            # username = line[1]['sAMAccountName'][0]
            # lastlogontimestamp = long(line[1]['lastLogonTimestamp'][0])
            # lastlogon = line[1]
            # normal_logon_timestamp = convert_ad_timestamp(lastlogontimestamp)
            # normal_last_logon = convert_ad_timestamp(lastlogon)
            # print '{},{},{}'.format(username, normal_logon_timestamp, normal_last_logon)
run()

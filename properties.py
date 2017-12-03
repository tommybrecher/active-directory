# Active Directory url
ldap_srv = 'ldap://127.0.0.1'
# Active Directory Administrator Credentials
ldap_user = ''
ldap_pass = ''
# Active Directory search base
base = 'cn=users,dc=domain,dc=com'
# Find only users where lastLogonTimestamp is greater than 3 months.
filters = '(|(lastLogonTimestamp<=131323104000000000))'

import re

# regex = re.compile('test')
# wynik = regex.findall('asdfasdfasdftestasdfatestsdf')
# print(wynik)
#
# regex = re.compile('[0-9]+')
# wynik = regex.findall('asdfasdfasdfte234stasdfatestsdf')
# print(wynik)
#
# # \\d+ == [0-9]+
# regex = re.compile('\\d+')
# wynik = regex.findall('asdfasdfasdfte234stasdfatestsdf')
# print(wynik)

regex = re.compile('\d{2}-\d{3}')
wynik = regex.findall('45-12304-32112-12321-89601-45205-691')
print(wynik)

regex_mail = re.compile('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)')
# ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.][com,pl,en,org,]+)
# ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+)
# ^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]$
wynik2 = regex_mail.findall('adsffas@gmail.comfdsklfdsjkl@interia.orgdfsggfj@onet.pl')
print(wynik2)

regex_date = re.compile('\d{2}-\d{3}')
wynik3 = regex_date.findall('25 Nov 2014')
print(wynik3)
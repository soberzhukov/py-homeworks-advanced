import csv
import re
from pprint import pprint


with open('phonebook_raw.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)

table_dict = dict()
pattern_LFS = re.compile(r"^([а-яёА-ЯЁ]*).([ха-яёА-ЯЁ]*).([ха-яёА-ЯЁ]*)([,]*)")
pattern_phone = re.compile(
        r"(\+7|8)[\s]*\(*(\d{3})\)*\s*[-]*(\d{3})[-]*(\d{2})[-]*(\d{2})\s*\(*(([доб]*\.*)\s*(\d+)*\)*)")

for i in range(1, len(data)):
    text_LFS = pattern_LFS.sub(r"\1,\2,\3,", ','.join(data[i][0:3]))
    table_dict[text_LFS.split(',')[0]] = {
    'lastname' : text_LFS.split(',')[0],
    'firstname' : text_LFS.split(',')[1],
    'surname'  : '',
    'organization' : '',
    'position' : '',
    'phone' : '',
    'email' : '',
    }

for i in range(1, len(data)):
    text_LFS = pattern_LFS.sub(r"\1,\2,\3,", ','.join(data[i][0:3]))
    text_phone = pattern_phone.sub(r"+7(\2)\3-\4-\5 \7\8", data[i][5])
    if text_LFS.split(',')[2] != '':
        table_dict[text_LFS.split(',')[0]]['surname'] = text_LFS.split(',')[2]
    if data[i][3] != '':
        table_dict[text_LFS.split(',')[0]]['organization'] = data[i][3]
    if data[i][4] != '':
        table_dict[text_LFS.split(',')[0]]['position'] = data[i][4]
    if text_phone != '':
        table_dict[text_LFS.split(',')[0]]['phone'] = text_phone
    if data[i][6] != '':
        table_dict[text_LFS.split(',')[0]]['email'] = data[i][6]

contacts_list = list()

for i in table_dict.values():
    contacts_list1 = [
        i['lastname'],
        i['firstname'],
        i['surname'],
        i['organization'],
        i['position'],
        i['phone'],
        i['email']
    ]
    contacts_list.append(contacts_list1)


with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list)

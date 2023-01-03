from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    # pprint(contacts_list)

    pattern_name = r"^([\w]+)(\s)?([\w]+)?(\s)?([\w]+)?,([\w]+)?(\s)?([\w]+)?,([\w]+)?"
    result_name = re.compile(pattern_name)

    pattern_phone = r"((\+7)|8)\s?\(?([\d]{3}?)(\)|\s|-)?\s?([\d]{3}?)(\s|-)?([\d]{2}?)(\s|-)?([\d]{2}?)(\s\(?(доб\.)?\s?([\d]*)\)?)?"
    result_phone = re.compile(pattern_phone)

    contacts_list_2 = []
    for contact in contacts_list:
        contact = ','.join(contact)
        contact = result_name.sub(r"\1,\3\6,\5\8\9", contact)
        contact = result_phone.sub(r"+7(\3)\5-\7-\9 \11\12", contact)
        contact = contact.split(',')
        contacts_list_2.append(contact)
    pprint(contacts_list_2)

with open("phonebook_correct.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(contacts_list_2)
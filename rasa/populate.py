# -*- coding: utf-8 -*-
from pymongo import MongoClient
import json

client_alerts = MongoClient("mongo_alerts", 27016)
client_ru = MongoClient("mongo_ru", 27017)

alert_db = client.mongo_alerts
alert_notifiers = alert_db.notifiers

ru_db = client.mongo_ru
ru_notifiers = ru_db.users

def populateNotifiers():
    notifier_file = open('email_dos_professores.csv', 'r+')

    while True:
        line = notifier_file.readline()

        if line == "":
            break

        structure = ""
        c_indent = 0
        indent = "    "
        structure += (indent*c_indent + "{\n")
        c_indent += 1
        element = line.split(',')
        structure += (indent*c_indent + "\"name\": " + "\"" + element[0] + "\",\n")
        structure += (indent*c_indent + "\"email\": " + "\"" + element[1].split("\n")[0] + "\"\n")
        c_indent -= 1
        structure += (indent*c_indent + "}\n\n")

        alert_notifiers.insert_one(json.loads(structure))

def populateUsers():
    user_file = open('documents.json', 'r+')

    users_list = json.dumps(user_file)

    for user in users_list:
        ru_notifiers.insert_one(user)

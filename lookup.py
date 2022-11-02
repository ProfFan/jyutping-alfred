#!/usr/bin/env python3

import sqlite3
import argparse

con = sqlite3.connect("dict.db")
con.row_factory = sqlite3.Row
cur = con.cursor()

parser = argparse.ArgumentParser()
parser.add_argument('lookup')

args = parser.parse_args()
lookup: str = args.lookup

pronounciation = []

for char in lookup:
    # print(lookup)
    cur.execute("SELECT * FROM 常用字廣州話讀音表 WHERE 字 = :lookup", {'lookup': char})
    try:
        result = cur.fetchall()
        if len(result) == 1:
            pronounciation.append(result[0]["粵拼讀音"])
        else:
            allpron = [r["粵拼讀音"] for r in result]
            pronounciation.append("({})".format("|".join(allpron)))

    except:
        pronounciation.append("<unk>")

all_results = []
all_results.append(
    {"title": "'".join(pronounciation)}
)

import json
print(json.encoder.JSONEncoder(ensure_ascii=False).encode({"items": all_results}))

#!/usr/bin/env python3

import csv
import sqlite3

con = sqlite3.connect("dict.db")
cur = con.cursor()

cur.execute('DROP TABLE 常用字廣州話讀音表')
cur.execute(
    'CREATE TABLE IF NOT EXISTS 常用字廣州話讀音表(編號, 頁, 字碼, 字, 輔助檢索用異體, 異讀分類, 欄位, 義項, 讀音類型, 說明, 粵拼讀音, 粵拼聲母, 粵拼韻母, 粵拼聲調, 九聲聲調, 增補讀音, 經校訂修正, 校訂註)'
)

with open('C02_正文(按讀音列出).txt') as csvfile:
    csvfile.readline()  # skip first line
    csvfile.readline()  # skip second line
    reader = csv.DictReader(csvfile, [
        "編號", "頁", "字碼", "字", "輔助檢索用異體", "異讀分類", "欄位", "義項", "讀音類型", "說明",
        "粵拼讀音", "粵拼聲母", "粵拼韻母", "粵拼聲調", "九聲聲調", "增補讀音", "經校訂修正", "校訂註"
    ],
                            delimiter='\t')
    for row in reader:
        # print(', '.join(row))
        print(row)
        print(len(row))
        cur.execute(
            "INSERT INTO 常用字廣州話讀音表 VALUES(:編號, :頁, :字碼, :字, :輔助檢索用異體, :異讀分類, :欄位, :義項, :讀音類型, :說明, :粵拼讀音, :粵拼聲母, :粵拼韻母, :粵拼聲調, :九聲聲調, :增補讀音, :經校訂修正, :校訂註)",
            row)
    
    con.commit()
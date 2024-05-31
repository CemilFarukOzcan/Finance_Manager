import csv
import time
import gspread
#eksterinizi csv formatında indirip ismine göre düzenleyin.
MONTH = 'march'

file = f"ekstre_{MONTH}.csv"

transactions = []
toplam = 0

def hsbcFin(file):
    with open(file, mode='r',encoding="utf8") as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                date = row[3]
                name = row[5]
                amount = float(row[6])
                global toplam
                toplam += amount
                #kendi ekstrenizdeki açıklamalara göre düzenleyin
                category = 'Category'
                if name == ".....":
                      category = "....."
                if name == ".....":
                      category = "....."
                if name == ".....":
                      category = "....."
                if name == ".....":
                      category = "....."
                if name == ".....":
                      category = "....."
                if name == ".....":
                      category = '"....."'
                if name == ".....":
                      category = '"....."'
                if name == ".....":
                      category = '"....."'
                transaction = ((date,name,amount,category,toplam))
                print(transaction)
                transactions.append(transaction)
            return transactions

#sonucları google sheets e göndermek için gspread kütüphanesini kullandım.
spread = gspread.service_account()
sh = spread.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = hsbcFin(file)

for row in rows:
    wks.insert_row([row[0],row[1],row[2],row[3],row[4]],1)
    time.sleep(2)

wks.insert_row([1,2,3,4],10)
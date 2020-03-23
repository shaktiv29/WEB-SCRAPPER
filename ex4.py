import requests
import time
from bs4 import BeautifulSoup
p = 1
old = []

def seperate(x):
    print("Alert Company " + x + "crossed the 2% criteria.")
while p<= 45:
    ls = []
    res = requests.get("https://www.moneycontrol.com/stocks/marketstats/indexcomp.php?optex=NSE&opttopic=indexcomp&index=9")
    soup = BeautifulSoup(res.text,"lxml")
    table = soup.find("table", { "class" : "tbldata14 bdrtpg" })
    table_body = table.find('tbody')
    for row in table.findAll('tr'):
        yu=[]
        for col in row.findAll('td'):
            yu.append(col.text.strip())
        ls.append(yu)
    new = []
    for i in range(len(ls)):
        j = []
        for l in range(len(ls[i])):
            if l==0:
                b = "\n\n\n\n\nAdd to Watchlist\nAdd to Portfolio"
                q = ls[i][l].replace(b,"")
                j.append(q)
            else:
                j.append(ls[i][l])
        new.append(j)
    new.remove(new[0])
    if p!=1:
        for i in range(len(new)):
            oldchg = old[i][4]
            newchg = new[i][4]
            oldchg = float(oldchg)
            newchg = float(newchg)
            if abs(oldchg-newchg) > 2 :
                seperate(new[i][0])
    time.sleep(30)
    old = new
    p+=1

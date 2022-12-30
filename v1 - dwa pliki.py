import requests
import bs4
from datetime import date

i = 1
x = 1
while i<4:
    r = requests.get("https://www.euro.com.pl/telefony-komorkowe,d4,od2000do10000,strona-"+str(i)+".bhtml")
    # print(r)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    #print(soup)

    with open('name.txt', 'a', encoding='utf-8') as f:
        names = soup.select(".product-name .js-save-keyword")
        for j in names:
            if(x%2==1):
                f.write(j.text.strip())
                f.write("\n")
                x+=1
            else:
                x=1
        #print(names)
        f.close()
    with open('readme2.txt', 'a', encoding='utf-8') as f2:
        prices = soup.select(".price-normal")
        #print(prices)
        for z in prices:
            f2.write(z.text.strip())
            f2.write("\n")
        #print(prices)
        f2.close()
    i+=1

Money = []
NewMoney = []
with open('readme2.txt', 'r', encoding='utf-8') as f3:
    Money = [line.strip() for line in f3]
    j3 = len(Money)
    i3 = 0
    while(i3<j3-1):
        if (Money[i3] == Money[i3+1]):
            NewMoney.append(Money[i3])
            i3 += 2
        else:
            i3 +=1
    f3.close()
    #print (Money)
    #print (len(Money))
    #print (NewMoney)
    #print (len(NewMoney))

    z4 = 0
    with open('prices.txt', 'w', encoding='utf-8') as f4:
        while (z4<len(NewMoney)):
            f4.write(NewMoney[z4])
            f4.write("\n")
            z4 += 1
    f4.close()

    Name = []
with open('name.txt', 'r', encoding='utf-8') as f5:
    Name = [line.strip() for line in f5]
    print (Name)
f5.close()

z6 = 0
with open('end.txt', 'w', encoding='utf-8') as f6:
    while (z6<len(Name)):
        f6.write(Name[z6]+"; "+NewMoney[z6]+"; "+str(date.today())+"\n")
        z6 += 1
    f6.close() 
    

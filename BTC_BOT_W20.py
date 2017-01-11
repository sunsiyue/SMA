import urllib2
import json
import unicodedata
import time

WINDOW_SIZE = 20

count = 0
prev = 0.0
money = 10000.0
hasMoney = True
coin = 0.0
window = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
averageP = 0.0
text_file = open("BTC_W20.txt", "w")
text_file.write("BTC_W20\n\n")


while (count < 10000):
	time.sleep(1)
	count = count + 1

	response = urllib2.urlopen('http://api.chbtc.com/data/v1/ticker?currency=btc_cny')
	data = json.load(response)
	price = float(data['ticker']['buy'])
	window[count % WINDOW_SIZE] = price
	p1 = 'price at count ' + str(count) + ' is ' + str(price)
	text_file.write(p1)
	text_file.write("\n")
	print p1

	if count < WINDOW_SIZE:
		continue



	averageP = sum(window) / WINDOW_SIZE

	p2 = 'average price now is: '+ str(averageP)
	text_file.write(p2)
	text_file.write("\n")
	print p2

	if((price > averageP) and not hasMoney):
		hasMoney = not hasMoney
		money = coin * price
		coin = 0.0
		p3 = "sold coins at price: " + str(price) + " and net worth : " + str(money)
		text_file.write(p3)
		text_file.write("\n")
		print p3

	elif ((price < averageP) and hasMoney):
		hasMoney = not hasMoney
		coin = money / price
		p4 = "bought coins at price: " + str(price) + " and net worth : " + str(money)
		text_file.write(p4)
		text_file.write("\n")
		print p4
		money = 0.0

	else:
		continue


text_file.close()


	
	






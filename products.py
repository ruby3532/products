products = []
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ') # 價格寫在這裡，是因為如果他沒有輸入商品名稱，就不需要輸入價格了。
	p = []
	p.append(name)
	p.append(price)
	products.append(p)

print(products)

	# 可以有更快的寫法： p = [name , price]
	# 最精簡的寫法：products.append([name , price])

# products[0][0] # product 中第 0 格中的第 0 格。

for p in products:
	print(p[0], '的價格是', p[1])


import os # operating system 作業系統

products = [] # 不管檔案是否存在，都要執行此指令
if os.path.isfile('products.csv'):
	print('yaaa 找到檔案了')
	with open('products.csv' , 'r' , encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue # 不會跳出迴圈，會直接跳到下一回
		name, price = line.strip().split(',')
		products.append([name , price])
	print(products)

else:
	print('找不到檔案.....')


# 讀取檔案



# 讓使用者輸入
while True:
	name = input('請輸入商品名稱： ')
	if name == 'q':
		break
	price = input('請輸入商品價格： ') # 價格寫在這裡，是因為如果他沒有輸入商品名稱，就不需要輸入價格了。
	price = int(price) # 價格變整數
	p = []
	p.append(name)
	p.append(price)
	products.append(p)

print(products)

	# 可以有更快的寫法： p = [name , price]
	# 最精簡的寫法：products.append([name , price])

# products[0][0] # product 中第 0 格中的第 0 格。

# 印出所有購買記錄
for p in products:
	print(p[0], '的價格是', p[1])

# 寫入檔案
with open ('products.csv', 'w', encoding = 'utf-8') as f:   # 寫入模式，用 f 稱做 products.txt 檔
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') # 用加法合併字串open。f.write 才是真的寫入
# csv 是很常儲存數據的格式
# with 是自動 close 的功能
# 若祇是單純中文會亂碼，需要用 encoding = 'utf-8' 處理

# 字串的加和乘法
# 'abc' + '123' = 'abc123'
# 'abc'* 3 = 'abcabcabc'



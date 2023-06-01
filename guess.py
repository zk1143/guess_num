import random
start = input('請輸入隨機數字開始值:')
end = input('請輸入隨機數字結束值:')
start = int(start)
end = int(end)

r = random.randint(start,end)
count = 0
while True:
	count += 1
	num = input('猜猜看數字:')
	num = int(num)
	if r == num:
		print('yes')
		print('你已經猜了', (count) , '次')
		break
	elif r > num:
		print('答案比數字大')
	elif r < num:
		print('答案比數字小')
	print('你已經猜了', (count) , '次')	






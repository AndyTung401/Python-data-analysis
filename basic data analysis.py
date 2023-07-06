import matplotlib.pyplot as plt
from math import sqrt
import numpy as np

#####變數宣告（？？？#####
sumx=0
sumy=0
sumx2=0
sumy2=0
sumxy=0
pix=1
xlist=[]
ylist=[]



#####輸入資料#####
mode=int(input("輸入 1 為一維分析、2 為二維分析："))



if mode==1:
	print("----------")
	print("一維數據分析")
	print("----------")
	n=int(input("輸入資料筆數："))
	print("開始輸入資料")
	for i in range(0,n):
		x=float(input("第"+str(i+1)+"筆："))
		xlist.append(x)
		#####計算總和、平方合、相乘合#####
		sumx += float(x)
		pix*=x
		sumx2+= float(x)**2
	xlist.sort()

	print(" ")
	print(" ")
	print(xlist)

	#####中位數#####
	if len(xlist)%2 == 0:
		print("中位數：",(xlist[int(len(xlist)/2)]+xlist[int(len(xlist)/2-1)])/2)
	else:
		print("中位數",xlist[int(len(xlist)/2-0.5)])

	#####平均#####
	avgx=sumx/n
	print("算數平均數：",round(avgx,4))
	print("幾何平均數：",round(np.power(pix,1/n),4))
	#####標準差#####
	print("標準差：",round(sqrt(sumx2/n-avgx**2),4))



elif mode==2:
	print("----------")
	print("二維數據分析")
	print("----------")
	n=int(input("輸入資料筆數："))
	print("輸入資料x及y，以空白分隔，例如「第1筆：37 53」")
	for i in range(0,n):
		x,y=input("第"+str(i+1)+"筆：").split()
		x=float(x)
		y=float(y)
		xlist.append(x)
		ylist.append(y)
		#####計算總和、平方合、相乘合#####
		sumx += float(x)
		sumy += float(y)
		sumx2+= float(x)**2
		sumy2+= float(y)**2
		sumxy+= float(x)*float(y)

	#####找出極值、算平均、標準差、相關係數、斜率#####
	max_x=float(max(xlist))
	max_y=float(max(ylist))
	min_x=float(min(xlist))
	min_y=float(min(ylist))
	avgx=sumx/n
	avgy=sumy/n
	sigmax=sqrt(sumx2/n-avgx**2)
	sigmay=sqrt(sumy2/n-avgy**2)
	r=(sumxy/n-avgx*avgy)/(sigmax*sigmay)
	m=r*sigmay/sigmax

	#####輸出結果#####
	print(" ")
	print(" ")
	print("x資料：",xlist)
	print("y資料：",ylist)
	print("- - - - - - - - - - - - -")
	print("平均數：(",round(avgx,4),",",round(avgy,4),")")
	print("標準差：(",round(sigmax,4),",",round(sigmay,4),")")
	print("- - - - - - - - - - - - -")
	print("相關係數：",round(r,4),"；決定係數：",round(r**2,4))
	print("--------------------------")
	print("關閉圖表以利用回歸線預測資料")

	#####製圖#####
	plt.scatter(xlist,ylist)
	z = np.polyfit(np.array(xlist), np.array(ylist), 1)
	p = np.poly1d(z)
	plt.plot(xlist, p(xlist))
	func="y="+str(round(m,4))+"x+"+str(round(-m*avgx+avgy,4))
	text="r^2="+str(round(r**2,4))
	if m<0:
		plt.text(0.7*max_x+0.3*min_x,0.9*max_y+0.1*min_y,func)
		plt.text(0.7*max_x+0.3*min_x,0.85*max_y+0.15*min_y,text)
	else:
		plt.text(0.7*max_x+0.3*min_x,0.1*max_y+0.9*min_y,func)
		plt.text(0.7*max_x+0.3*min_x,0.05*max_y+0.95*min_y,text)
	plt.show()

	#####迴歸線預測#####
	print("- - - - - - - - - - - - -")
	while True:
		predx=float(input("輸入x值預測y值："))
		print(round(m*(predx-avgx)+avgy,4))

else:
	print("----------")
	print("庭維數據分析")
	print("----------")
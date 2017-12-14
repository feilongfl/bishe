import cv2

image = cv2.imread('./data/data.bin.png')

GrayImage=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret,binImage=cv2.threshold(GrayImage,127,255,cv2.THRESH_BINARY)

binImage;

def calch(h):
	(x,y)=h.shape
	b = [0 for z in range(0, x)]
	#print (b[0])
	for j in range(0,y):
		for i in range(0,x):
			if  h[i,j]==0:
				b[i]=b[i]+1
				h[i,j]=255  
		#print (b[i])   

	for i in range(0,x):
		for j in range((y-b[i]),y):
			h[i,j]=0
		#print (b[i])  

	#cv2.imshow('img',h)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	cv2.imwrite('./data/data.minh.png', h)
	y=999;
	height=0;
	for i in range(0,x):
	    if  b[i]!=0:
		    height+=1
		    if i < y:
			    y = i
	return y,height



def calcv(v):
	(x,y)=v.shape
	a = [0 for z in range(0, y)]
	#print (a[0])
	for j in range(0,y):
		for i in range(0,x):
			if  v[i,j]==0:
				a[j]=a[j]+1
				v[i,j]=255
		#print (j)         
            
	for j  in range(0,y):
		for i in range((x-a[j]),x):
			v[i,j]=0

	#print (x,y)

	#cv2.imshow('img',v)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()

	cv2.imwrite('./data/data.minv.png', v)
	x=999;
	width=0;
	for i in range(0,y):
	    if  a[i]!=0:
		    width+=1
		    if i < x:
			    x = i
	return x,width

#def subImg(img,x,y,w,h,dstw,dsth):
#	x ==5
#	y-=5
#	w+=10
#	h+=10
#	tmp = img[x:x+w.y:y+h]
#	return cv2.resize(tmp, (dstw,dsth))


y,h = calch(binImage.copy())
x,w = calcv(binImage.copy())
print(x,y,w,h)

#x=274
#y=139
#w=130
#h=256

size = (h, w)[w>h]
new_x=x+w/2-size/2
new_y=y+h/2-size/2

ori=image[int(new_y):int(new_y + size),int(new_x):int(new_x + size)]
sml=cv2.resize(ori, (28,28))

#cv2.imshow('img',sml)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

cv2.imwrite('./data/data.min.png', sml)

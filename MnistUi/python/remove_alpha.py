from PIL import Image

im = Image.open('data.png') 
x,y = im.size 
try: 
    p = Image.new('RGBA', im.size, (255,255,255)) 
    p.paste(im, (0, 0, x, y), im) 
    p.save('data.bin.png') 
except: 
    pass 

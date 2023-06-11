import shutil


src_path = "D:/Documents/03_Projects/burgfalkenscenery-master/panorama/maker-c8-ttx/output/"
dst_path = "D:/Documents/03_Projects/burgfalkenscenery-master/panorama/maker-c8-ttx/output_renamed/"



for a in range(0,8):
    for b in range(0,16):
        index = a*16+b+1
        sourcefile="image"+str(index)+".ttx"
        #destfile="burgfalken"+str(b)+str(a)+"c.ttx"
        destfile="burgfalken"+f"{b:x}"+f"{a:x}"+"c.ttx"
        print(sourcefile, destfile)
        shutil.copy(src_path+sourcefile, dst_path+destfile)
        #print('Copied')

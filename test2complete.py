a=[]
k=[1077,1500,900,1160,960,1340,1200,1000,1125]#ราคาที่ลดไป
r=[2513,3500,2100,4690,3840,5360,1200,1000,1125]#ราคาที่จ่ายจริง
r=0
while True:
    b=input('**********ร้าน modshop ยินดีต้อนรับ*********\n เลือกสินค้า[a]\n แสดงรายการที่สั่งซื้อ[s]\n ออกจากระบบ[x]\n')
    b=b.lower()
    if b=='a': #ถ้าผู้ใช้เลือก a ก็คือเลือกสินค้า
        print('Adidas \n Superstar ราคา 3590 บาท[1]\n NMD R1 ราคา 5000 บาท[2]\n STAN SMITH ราคา 3000 บาท[3]\n')
        print('Nike \n Nike Air Max 97 Premium ราคา 5800 บาท[4]\n Nike Air Max ราคา 4800 บาท[5]\n Nike Zoom ราคา 6700 บาท[6]\n')
        print('Vans \n Vans Old Skool ราคา 2400 บาท[7]\n Vans Classic ราคา 2000 บาท[8]\n Vans slip on ราคา 2250 บาท[9]\n')
        c=input('ป้อนชื่อรุ่นที่ต้องการ(กรอกหมายเลข): ')#ให้ผู้ใช้เลือกรุ่นจากหมายเลข
        if c=='1': #ถ้าผู้ใช้เลือกหมายเลข 1 
            a.append('Superstar:3590:30%:2513')#แทรกข้อมูล
            r+=2513#ราคารวม
        elif c=='2':
            a.append('NMD R1:5000:30%:3500')
            r+=3500
        elif c=='3':
            a.append('atan smith:3000:30%:2100')
            r+=2100
        elif c=='4':
            a.append('Nike Air Max Premium:5800:20%:4690')
            r+=4690
        elif c=='5':
            a.append('Nike Air Max:4800:20%:3840')
            r+=3840
        elif c=='6':
            a.append('Nike Zoom:6700:20%:5360')
            r+=5360
        elif c=='7':
            a.append('Vans Old Skool:2400:50%:1200')
            r+=1200
        elif c=='8':
            a.append('Vans Classic:2000:50%:1000')
            r+=1000
        elif c=='9':
            a.append('Vans slip on :2250:50%:1125')
            r+=1125
        print('\n*****ข้อมูลได้เข้าระบบแล้ว******\n')
    elif b=='s':
        print('{0:-<20}{0:-<10}{0:-<15}{0:-<10}'.format(""))
        print('{0:<20}{1:<10}{2:<15}{3:10}'.format('รุ่น','ราคา','ส่วนลด','จ่ายจริง'))
        print('{0:-<20}{0:-<10}{0:-<15}{0:-<10}'.format(""))
        count = 0
        for d in a:
            e=d.split(":")
            count += 1
            print('{0[0]:<20}{0[1]:<10}{0[2]:<15}{0[3]:10}'.format(e))
            continue
        print('{0:-<20}{0:-<10}{0:-<15}{0:-<10}'.format(""))
        print('รวมเป็นเงิน                                   ',r)
        print('{0:-<20}{0:-<10}{0:-<15}{0:-<10}'.format(""))
    elif b=='x':
        break
print('ทำคำสั่งต่อไป')

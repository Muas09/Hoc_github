#2:
"""for n in range(5):
   print ("HELLO")"""
#3:
"""age =20
print(age)
print("age")"""
#4
"""value = 0
value = value +2
print ( value )"""
#5
"""age = 19
for n in range(6) :
    print ( age )
    age = age +2"""
#6
"""age = 1
while age < 10 :
    print ( age )
    age = age + 1"""
#7
"""age = 14
size = 21
print ( "My name is",age,"and","my size is", size )"""
#8
"""repetition = int (input("n:"))
for n in range  ( repetition) :
    print ("HELLO")"""
#9
"""n= int(input("Nhap so:"))
if n==0:
    print("Good choice!")
else:
    print("bad choice!")
"""
#1
"""thenumber =int(input("nhap so:"))
if thenumber <= 0:
    print("Negative")
else:
    print("Positive")"""
#2
"""theNumber=int(input())
if theNumber<0 :
    theNumber = theNumber*(-1)
    print(theNumber)"""
#3 Tinh tong bien 1 va bien 2:
"""firstNumber = int(input("nhap so:"))
secondNumber = int(input("nhap so:"))
print(firstNumber+secondNumber)"""
#4 hai so bang nhau thi no in numbers are equal va nguoc lai
"""firstNumber = int(input("nhap so:"))
secondNumber =int(input("nhap so:"))
if firstNumber == secondNumber :
    print("numbers are equal")
else:
    print("number are not equal")"""
#5 cong hai so lai voiw nhau
"""firstNumber = int(input("nhap so:"))
secondNumber = int(input("nhap so:"))
if (firstNumber+secondNumber)<20:
    print("sum is less than 20")
else:
    print("sum is greater or equal to 20")
"""
#6
"""score = int(input("nhap so:"))
if score < 50:
    print("bad!")
elif 50 <= score <80:
    print("not bad, not good")
elif 80<= score <= 100:
    print("excellent!")
elif score>100:
    print("are you crazy?!")"""
#7
"""firstNumber = int(input("nhap so:"))
secondNumber = int(input("nhap so:"))
if firstNumber > secondNumber:
    print("greatest number is:",firstNumber)
else:
    print("greatest number is:",secondNumber)"""
#8
"""firstNumber = int(input("nhap so:"))
secondNumber = int(input("nhap so:"))
if firstNumber < secondNumber:
    print("smallest number is:",firstNumber)
else:
    print("smallest number is:",secondNumber)
"""
#9
"""firstNumber = int(input("nhap so:"))
secondNumber = int(input("nhap so:"))
thirdNumber = int(input("nhap so:"))
if (firstNumber==secondNumber==thirdNumber):
    print("all equal")
else:
    print("not all equal")"""
"""n=str(input("nhap text:"))
textnew=""
for i in range(len(n)):
    if n[i]=='A':
        textnew= textnew+"6"
    elif n[i]=='B':
        textnew=textnew+"5"
    else:
        textnew=textnew+ n[i]
print(textnew)"""

"""n=str(input("nhap text:"))
counta=0
countb=0
for i in range(len(n)):
    if n[i]=='A' :
       counta=counta+1
    elif n[i]=='B':
        countb=countb+1
print(counta) 
print(countb) """
"""n=str(input("nhap text:"))
counta=0
countb=0
countc=0
for i in range(len(n)):
    if n[i]=='A' or n[i]=='a':
       counta=counta+1
    elif n[i]=='B'or n[i]=='b':
        countb=countb+1
    elif n[i]=='C'or n[i]=='c':
        countc=countc+1
print(counta) 
print(countb) 
print(countc) """

"""n=str(input("nhap text:"))
textnew=""
for i in range(len(n)):
    if n[i]=='A':
        textnew= "6"+textnew
    elif n[i]=='B':
        textnew=textnew+"5"
    else:
        textnew=textnew+ n[i]
print(textnew) """ 
"""text1 = "my name is "
name = input("what your name")
text2 = " my age is"
age = int(input("How old are you"))
sentence = text1 + name + text2 + age
print(sentence)
print(text1, name, text2, age)"""


"""a = str(input("nhap chuooi:"))
b=""
for i in (a):
    if i !=" ":
        b= b+i
print(b)
        """
        
        
"""nb1 = "3"
for i in range(nb1):
    print("hello" + True)"""
# number = 4.5
# integer = int(number)
# text = str(number)
# boolean = bool(number)
#boolean =b
"""text = "class2024"
for i in range (len(text)):
    print(text[i])"""
    
    
"""text="class2024"
a=""
for i in range (len(text)):
    a=a+text[i]+","
print(a[:-1])
"""
"""text="class2024"
print(text[3:5])"""


        


#Nh???p m???t chu???i v?? g??n n?? cho m???t bi???n c?? t??n l?? v??n b???n 
#?????m xem c?? bao nhi??u k?? t??? "a" trong ?????u v??o n??y. N???u kh??ng c?? k?? t??? "a" xu???t "a not found" 

"""n=str(input("nhap chu???i"))
a=0
for i in range(len(n)):
    if n[i]=="a":
        a=a+1
if a==0:
    print("a not found")
else:
    print(str(a)+ "a found")"""

# Nh???p m???t chu???i v?? g??n gi?? tr??? c???a n?? cho m???t bi???n c?? t??n l?? v??n b???n. 
# N???u chu???i n??y ch???a k?? t??? "a" th?? hi???n th??? "a t??m th???y t???i ch??? m???c c???a [s??? ch??? m???c, s??? ch??? m???c n???u c?? nhi???u a]" 
# N???u kh??ng, xu???t ra "a not found" 
"""n=str(input("nhap chuoi:"))
a=""
for i in range(len(n)):
    if n[i] =="a":
        a=a+ str(i)+","
if a=="":
    print("a not found")
else:
    print("a found at the index of " +a[:-1])"""
#Ch??ng ta c?? text = "alibaba" 
#Thay th??? t???t c??? k?? t??? "a" trong chu???i n??y b???ng "e" V?? v???y, cu???i c??ng ch??ng ta s??? c?? chu???i m???i v???i gi?? tr??? n??y "elibebe"
"""text= "alibaba" 
a=""
for i in(text):
    if i=="a":
        a=a+ "e"
    else:
        a=a+i
print(a)"""

#Nh???p m???t chu???i v?? g??n gi?? tr??? c???a n?? cho m???t bi???n c?? t??n l?? text. 
#N???u t??? nh???p n??y l?? t??? ?????i x???ng hi???n th??? "It is symmetric word" 
#Ng?????c l???i hi???n th??? "It isn't symmetric word" 
# L??u ??: ?????i x???ng l?? t??? ???????c vi???t t??? tr??i sang ph???i gi???ng nh?? t??? ph???i sang tr??i nh?? aba, madam ,noon ,mom ,c???p ????? \

"""n = str(input("nhap chu???i: "))
check =""
for i in range(len(n)):
    check=check+n[(len(n)-1)-i]   
if check ==n:
    print(n,"la so doi xung")
else:
    print(n," khong phai  la so doi xung")"""
#text = "class2024" 
#B???ng c??ch s??? d???ng bi???n v??n b???n n??y, h??y vi???t Python ????? ????a ra k???t qu??? nh?? b??n d?????i. 
    # c 
    # l 
    # a 
    # s 
    # s 
    # 2 
    # 0 
    # 2 
    # 4
"""text = "class2024"
for i in range (len(text)):
    print(text[i])"""  
# T??nh gi?? tr??? tuy???t ?????i
"""n=int(input("nhap n:")  )
if n<=0:
    n=n*(-1)
print(n)   """
# Gi???i ph????ng tr??nh b???c nh???t
a=int(input("nhap:"))
b=int(input("nhap:"))
if a==0:
    if b==0:
        print("v?? s??? nghi???m")
    else:
        print("v?? nghi???m")
else:
    x=-b/a
    print(x)
# Tinhd t???ng v?? ??i???m trung b??nh.
"""a=float(input("nhap:"))
b=float(input("nhap:"))
c=float(input("nhap:"))
sum=0
Avg=0
sum= (a+b+c)
Avg= sum/3
print(sum)
print(Avg)"""
# T??nh chu vi di???n t??ch.
"""r= float(input("nhap b??n k??nh:"))
pi = 3.12
chuVi= 2*pi*r
DienTich = pi*r*r
print(chuVi)
print(DienTich)"""
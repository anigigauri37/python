# while - სანამ
# while ციკლის მუშაობა ეყრდნობა პირობას და სანამ პირობა სწორია იქამდე გაეშვება კოდი

#fol loop პირდაპირ ვეუბნებით რამდენჯერ გვინდა კოდის გაშვება ხოლო while loop პირდაპირ პირობას ვუწერთ 



#1

num = 0
while num < 5:
    print("ani")
    num = num + 1
     

#2 password

password = 'ani123'
autorized = False

while autorized != True:
    is_text = input("xelaxla scadet")
    if is_text == password:
        autorized = True


#3 gouss game

num = int(input("enter number"))

while num != 10:
    num = int(input("enter number"))

    if num == 10:
        print("dasruleba")
    else:
        print("scadet xelaxla")


#4 luwi ricxvebis shekreba

num = 0
sum = 0
while num < 10:
    num = num + 2
    sum = sum + num

    print(sum)

#5 

age = int(input("enter your age"))

if age >= 18:
    print("qtven xart srulwlovan")
else:
    print("qtven ar xart swulwlovani")
   

#6 shoop

budget = int(input("enter budget"))

if budget == 100:
    print("shen shegidzlia iyido tansacmeli")
elif budget == 150:
    print("tqven iyidit telepons")
elif budget == 500:
    print("tqven iyidit saxls")
else:
    print("tqven shegidzliat iyidit rac gindat")


#7 momxmarebels shemovataninot agasi da davprintot aris tu ara is bavshvi

age = int(input('enter your age'))

if age >= 5 and age < 13:
    print("tqven xart bavshvi")
elif age >= 15 and age < 18:
    print('tqven ar xart bavshvi')
else:
    print('srulwlovani')



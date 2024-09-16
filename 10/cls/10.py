# cudi gza 

print("ani")
print("ani")
print("ani")
print("ani")
print("ani")
print("ani")

#2 kargi gza

for i in range(20):
    print("ani")



#3 yvelaze kargi gza

def print_name():
    for i in range(20):
        print("ancho")

#punqcias swirdeba gamodzaxeba

print_name()



#4 

def print_name(name):
    print(name)

#punqcias swirdeba gamodzaxeba

print_name("ani")

#5


def print_name(name, surname):
    print(name + " " + surname)

#punqcias swirdeba gamodzaxeba

print_name("ani", "gigauri")



#6

def print_name(name):
    for i in range(10):
        print(name)

#punqcias swirdeba gamodzaxeba

print_name("anushki")
print_name("GOA")


#7

def print_number():
    for i in range(10):
        print(i + 5)

print_number()



#8 gamovtvalot am ricxvebis aritmetikuli

def calculate_avarage():
    numbers = [1,2,3,4,5]
    print(sum(numbers) / len(numbers))

calculate_avarage()


#9 ramdenjerme gamovidzaxot punqcia da gadavcet sxvadasxva mnishvnelobebi

def print_number(start, end):
    for i in range(start, end):
        print(i)
    print("end")

print_number(1, 10)
print_number(5, 9)


#10


def print_name(name):
    print("welcome" + name)

print_name("ani")
print_name("gio")

 
#11 rogor movamzadot sendvichi

def make_sendwich(ingredients):
    print("open bread")
    print(ingredients)
    print("end bread")

make_sendwich(["cheese", "tomatoes", "lettuce", "bacon"])


#12 davabrunot sendvichi


def make_sendwich():
    return"sendwich"

my_orded = make_sendwich()
print(my_orded)


#13 vipovot am ricxvebs shoris yvela ricxvis jami


def print_sum(numbers_list):
    sum = 0

    for i in numbers_list:
        sum = sum + i
    return sum

print(print_sum([1,2,3,4,5]))


#14 

def manual_max(num1, num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else:
        return "numbers are equal"

print(manual_max(10,5))


#15 amovigon yvela ricxvi da davaxarisxot luwebad da kentebad

def filter_list(numbers_list):
    for num in numbers_list:
        if num % 2 == 0:
            print("even:", num)
        else:
            print("odd:", num)
filter_list([1,2,3,4,5,6,7,8,9,10])


#16 
  
def print_name(n):
    for i in range(2,n + 1):
        if i % 2 == 0:
            print(i)
print_name(10)



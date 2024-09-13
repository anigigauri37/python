# list - სია
# collection - სია

#1

food = ['shaurma', 'xinkali', 'mwvadi', 'cezari']
print(len(food))

#2

cars = ['bmw', 'mercedes', 'subaro']
print(cars[0:2])

#3

books = ['harry potter', 'shecdoma', 'bidzia tomas qoxi']
books1 = ['cduneba']
books2 = books + books1
print(books2)

#4

cars = ['merso', 'bmw']
print(cars[len(cars) -1])


#5

cars = ["ferari", "mercedesi", "toiota"]
cars[2] = "subaro"
print(len(cars))


#6

cars = ["ferari", "mercedesi", "toiota"]
cars.append("ani")
print(cars)

#append - დამატება


#7 sheqmenit punqcia romelic 1 dan 10 gamoitvlis yvela ricxvs da daamatebs siashi

numbers = []

for i in range(1,10):
    numbers.append(i)

print(numbers)
print(len(numbers))


#8

start = int(input("enter start number"))
end = int(input("enter end number"))

numbers = []
for i in range(start, end):
    numbers.append(i)
    print(numbers)


#9 max

numbers = [1,2,3,4,5]

print(max(numbers))


#10 min

numbers = [5,2,3,10,25]

print(min(numbers))


#11 shemovitamos ricxvi da davbewdot am ricxvebis max, min, yvela ricxvis jami

start = int(input("enter start number"))
end = int(input("enter end number"))

numbers = []
for i in range(start, end):
    numbers.append(i)

print(max(numbers))
print(min(numbers))
print(sum(numbers))


#12

count = int(input("enter numbers"))

numbers = []

for i in range(count):
    num = int(input("enter number " + str(i + 1 ) + ": "))
    numbers.append(num)
    print(numbers)

#13

for i in range(10):
    print(str(i + 1) + "ani")


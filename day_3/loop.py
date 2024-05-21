#while and for loop
# while loop
# x=0
# while (x<5):
#     print(x)
#     x+=1

#for loop
for x in range(5,10):
    print(x)

#create a array
days=["mon","tusday","wen","thu","fri","sat","sun"]
for d in days:
     print(d)

days=["mon","tusday","wen","thu","fri","sat","sun"]
for d in days:
    if(d=="fri"):break
    print(d)

days=["mon","tusday","wen","thu","fri","sat","sun"]
for d in days:
    if(d=="fri"):continue
    print(d)
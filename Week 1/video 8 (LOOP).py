#{} - curly braces []- parenthesis
# name=[ 'jd', 'arnab' , 'ola']
# for i in name :
#     print (i)
# for i in range (1,101):
#  print (i)
# x=1
# for  i in range (3):
#     for j in range (3):
#         print (x, end=" ")
#         x +=1
#     print ()
# i=0
# while i<3:
#     j=0
#     while j <3:
#         print (x, end =" ")
#         x +=1
#         j +=1
#     print ()
# # i +=1
# x= 1
# i =1
# while i <2:
#     j=0
#     while j<3:
#         print(x, end="")
#         x+=1 
#         j+=1
#     print ()
#     i+=1
# x=1
# for i in range (3):
#     for j in range (3):
#         print (x, end= "")
#         x+=1
#     print ()
# Task of video 8
# x="*"
# for i in range (4):
#     for j in range (4):
#         print (x, end="")
#         j+=1
#     print ()
# for i in range (4):
#     for j in range (i+1):
#         print (x, end= " ")
#     print ()
# for i in range (1,4):
#     for j in range (i*i):# not needed
#         print (i, end="")
#     print()

# for i in range(1, 5): 
#     for j in range(i): 
#         print(i, end="")
# #     print()
# for i in range(1,5): 
#     for j in range(1,i*2,2): 
#         print(i, end="")
#     print()

x=1
i=0
while i<3:
    j=0
    while j<3:
        print(x, end="")
        x+=1
        j+=1
    print()
    i+=1
x="*"
for i in range (4):
    for j in range (4):
        print (x, end = "")
    print ()
x= "*"
for i in range (4):
    for j in range (i+1):
        print (x,end= "")
    print ()
for i in range (1,5):
    for j in range (i):
        print ( i, end =" ")
    print()
for i in range (1,5):
    for j in range (1,i*2,2):
        print (j, end="")
    print()

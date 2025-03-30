list =  [1,2,"some text",2.3,44,55] # list -> mutable
print(list)
print(list[2])
list[3]= 11
print(list[5])
# slice below string
l= [1,2,3,4,5,6,7,8,9,10]
r= l[1:8:3]
print(r)

tuple = (1,2,3,4,5,6,7,9,8) #tuple --> immutabl
print(tuple)
set = {1,2,3,4,5,6,7,8,9} # set --> can not have repeatative values
dict = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd'
}
print(dict)

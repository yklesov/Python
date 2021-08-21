# thisdict={'name':'Aram','year':1994}
# print(thisdict)
# thisdict['year']=2014
# print(thisdict)
# thisdict['age']=26
# print(thisdict)
# del thisdict['age']
# print(thisdict)
# thisdict.clear()
# this_set={"apple","banana","cherry"}
# for x in this_set:
#     print(x)
# print("banana" in this_set)
# set1={"a","b","c"}
# set2={1,"a",3}
# set3=set1.union(set2)
# print(set3)
# set1={12,23,'11',"hello"}
# set2={14,3,'141',"world"}
# print(set1.isdisjoint(set2))
# x={'1':'Valod','2':'Valod','3':'Valod','4':'Valod','5':'Valod','6':'Valod','7':'Valod','8':'Valod','9':'Valod','10':'Valod'}
# print(x)
# y={'Valod':5,'Abdul':2,'Arsen':3}
# print(y.values())
# x=y.values()
# z=0
# count=0
# for i in x:
#     z=z+i
#     count+=1
# print(z/count)
count = 0
while (True):
    harc_1 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
    if harc_1 is True:
        count += 1
    else:
        count == 0
        print("You lose")
        break
    harc_2 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
    if harc_2:
        count += 1
    else:
        count == 0
        print("You lose")
        break
    harc_3 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
    if harc_3:
        count += 1
    else:
        count == 0
        print("You lose")
        break
    harc_4 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
    if harc_4:
        count += 1
    else:
        count == 0
        print("You lose")
        break
    harc_5 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
    if harc_5:
        count += 1
    else:
        count == 0
        print("You lose")
        break
    harc_6 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
    if harc_6:
        count += 1
    else:
        count == 0
        print("You lose")
        break
    harc_7 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
    if harc_7:
        count += 1
    else:
        count == 0
        print("You lose")
        break
    harc_8 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
    if harc_8:
        count += 1
    else:
        count == 0
        print("You lose")
        break
    sharunakel=input("Duq uzumeq sharunakel\n\ta:Yes\n\tb:No\n")
    if sharunakel=="a":
        harc_9 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
        if harc_9:
            count += 1
        else:
            count == 0
            print("You lose")
            break
        harc_10 = input("Im @nkeroch anun@\n\ta:Valod\n\tb:Alex\n\tc:Hamo\n\td:Edo\n") == "Valod"
        if harc_10:
            count += 1
        else:
            count == 0
            print("You lose")
            break
    elif sharunakel=="b":
        print("Duq havaqeleq", count, " miavor")
        break
    print("Duq havaqeleq", count, " miavor")
    break


my_dict={"Вадим":2002, "Илона":1992, "Наташа":1970}
print (my_dict)
print(my_dict["Илона"])
print(my_dict.get("Олеся"))

my_dict.update({"Марина":1972, "Лена":1974})
print(my_dict)

a=my_dict.pop("Лена")
print(my_dict)
print(a)

my_set={7,8,1,7,2.5,5.6,"лось",False,(3,9,2,5)}
print(my_set)

my_set.add(76)
print(my_set)

my_set.discard(76)
print(my_set)





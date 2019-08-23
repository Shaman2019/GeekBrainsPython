# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.
name1 = input("Введите имя игрока: ")
name2 = input("Введите имя соперника: ")

player = {"name":name1,"health":400,"damage":60}
enemy = {"name":name2,"health":400,"damage":60}

def attack(pl1,pl2):
    pl2["health"]-=pl1["damage"]
    return pl1,pl2
#player,enemy = attack(player,enemy)

# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.

player["armor"] = 1.2
enemy["armor"]=1.2

def newdamage(player1,player2):
    return player1["damage"]/player2["armor"]

def attack2(pl1,pl2):
    pl2["health"]-=newdamage(pl1,pl2)
    return pl1,pl2

def saveplayer(pls):
    with open(pls["name"]+".txt","w",encoding="UTF-8") as f:
        for name,val in pls.items():
            f.write(name+":"+str(val) + "\n")
saveplayer(player)
saveplayer(enemy)

def readplayer(plname):
    with open(plname + ".txt", "r", encoding="UTF-8") as f:
        result = {}
        for line in f:
            if line.split(":")[0]=="name":
                result[line.split(":")[0]]=line.split(":")[1].replace("\n","")
            else:
                result[line.split(":")[0]] = float(line.split(":")[1].replace("\n", ""))
    return result

def game(fighter1,fighter2):
    while True:
        if fighter1["health"]<=0:
            return fighter2["name"]+" : "+str(fighter2["health"])
        else:
            attack2(fighter1, fighter2)

        if fighter2["health"] <= 0:
            return fighter1["name"]+" : "+str(fighter1["health"])
        else:
            attack2(fighter2, fighter1)

rplayer=readplayer(name1)
renemy=readplayer(name2)

print("Победитель: ",game(rplayer,renemy))

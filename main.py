"""Создать репозиторий для решения задачи. Для решения создать 3 ветки.
В первой ветке решение 1-3 задачи, в второй 4-6, в третьей - 7-10. Отправить мне.
После одобрения вливать в main при помощи пулл-реквестов."""

my_list = [42, 43]
my_dict = {
    "foo": {
        "a": 12,
        "b": (1, 2, 3, 4, my_list)
    },
    "bar": {
        "c": 12,
        "d": {5, 6, 7}
    },
    "moo": {
        "e": 12,
        "f": {"lol": ["l", "o", "l"]}
    },
}

# Ветка 1
# задание 1-3
print(my_dict["foo"])
print(my_dict["foo"].get("b"))
my_list.append(44)

# Ветка 2
# задание 4-6

print(my_dict["foo"].get("b"))
print(my_dict["bar"].get("d"))
my_dict["bar"].get("d").add(9)

# Ветка 3
# задание 7-10

print(my_dict["bar"].get("d"))
my_dict["moo"].get("f").get("lol").remove("o")
key = {"k": ["K", "e", "k"]}
my_dict["moo"].get("f").update(key)
print(my_dict["moo"].get("f"))
my_dict.clear()
print(my_dict)
class_points = [2, 4, 100, 70, 40, 66]
your_points = 66


def better_than_average(class_points, your_points):
    print(sum(class_points) / len(class_points))
    return False if sum(class_points) / len(class_points) > your_points else True


print(better_than_average(class_points, your_points))


def seyshely_vacation(d):
    return


print(seyshely_vacation(2))
print(seyshely_vacation(4))
print(seyshely_vacation(8))


def converter(usd):
    pass

usd = 15
usd2 = 465

print(converter(usd))

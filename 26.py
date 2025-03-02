file = open('26.txt')
a = file.readlines()[1:]
file.close()
cars = [[int(y) for y in x.split()] for x in a]
cars.sort(key=lambda x: x[0])
print(cars)
gases = {'gas92': [], 'gas95': []}
time1, time2 = cars[0][0], cars[0][0]
count = 0
refueled, not_refueled = 0, 0
flag = True
for x in cars:
    time_arrive, time_refueling, num_gas = x  # распаковываю входные данные

    if len(gases['gas92']) >= 1:
        if gases['gas92'][0] <= time_arrive:  # проверка на удаления из очереди тех, кто уже заправился
            gases['gas92'].pop(0)
            count += 1
    if len(gases['gas95']) >= 1:
        if gases['gas95'][0] <= time_arrive:
            gases['gas95'].pop(0)

    if num_gas == 0:  # если автомобиль может заправиться на любой колонке
        if len(gases['gas92']) <= len(gases['gas95']):  # проверка колонки с меньшей очередью
            if len(gases['gas92']) < 5:  # проверка, что в очереди меньше 5 машин
                gases['gas92'].append(time_refueling + time1)  # добавляю в очередь автомобиль
                time1 += time_refueling  # время, когда автомобиль полностью заправиться
            else:
                not_refueled += 1  # счетчик -> не заправился
        else:
            if len(gases['gas95']) < 5:
                gases['gas95'].append(time_refueling + time2)
                time2 += time_refueling
            else:
                not_refueled += 1

    elif num_gas == 1:
        if len(gases['gas92']) < 5:
            gases['gas92'].append(time_refueling + time1)
            time1 += time_refueling
        else:
            not_refueled += 1
    else:
        if len(gases['gas95']) < 5:
            gases['gas95'].append(time_refueling + time2)
            time2 += time_refueling
        else:
            not_refueled += 1

for x in gases['gas92']:
    if x <= 24 * 60:
        count += 1
    else:
        break
print(count, not_refueled)
# Ответ: 248 495

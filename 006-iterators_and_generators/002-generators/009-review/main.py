def summa():
    yield 'Summa Cum Laude'


def magna():
    yield 'Magna Cum Laude'


def cum_laude():
    yield 'Cum Laude'

# Write your code below:


# Checkpoint 1
# def graduation_countdown(days):
#     while days >= 0:
#         yield days
#         days -= 1

# Checkpoint 3
def graduation_countdown(days):
    while days >= 0:
        days_left = yield days
        if days_left is not None:
            days = days_left
        else:
            days -= 1


days = 25
gpas = [3.2, 4.0, 3.6, 2.9]

# Checkpoint 2
countdown_generator = (day for day in range(days, -1, -1))
for x in countdown_generator:
    print(x)

# Checkpoint 4
grad_days = graduation_countdown(days)
for x in grad_days:
    if x == 15:
        grad_days.send(10)

# Checkpoint 5
    elif x == 3:
        grad_days.close()

    print('Days Left:', x)

# Checkpoint 6


def honors_generator(gpas):
    for x in gpas:
        if x > 3.9:
            yield from summa()
        elif x > 3.7:
            yield from magna()
        elif x > 3.5:
            yield from cum_laude()


# Checkpoint 7
honors = honors_generator(gpas)
for x in honors:
    print(x)

steps = 316

buffer = [0]
current = 0

for step in range(1, 2018):
    current = ((current + steps) % len(buffer)) + 1
    buffer.insert(current, step)

print(buffer[buffer.index(2017)+1])

i = 0
value_after_0 = 0

for step in range(1, 50000001):
    i = (i + steps) % step + 1
    if i == 1:
        value_after_0 = step

print(value_after_0)

def round_to_2(err):
    return round(err, 2)

real = [12,21,23,32,43]
predicted = [11,20,22,31,42]
tests = [0]
results = []

def mean_absolute_difference_solution(real, predicted):
    err = ((real[0] - predicted[0]) + (real[1] - predicted[1]) + (real[2] - predicted[2]) + (real[3] - predicted[3]) + (real[4] - predicted[4])) / 5
    print(err)
    round_to_2(err)
    results.append(err)



mean_absolute_difference_solution(real, predicted)
if results > tests:
    print('Все тесты прошли успешно!')
else:
    print('Произошла ошибка')
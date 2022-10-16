# Функция, которая подсчитывает число покупателей, попадающих в каждую группу,
# если нумерация ID сквозная и начинается с 0. На вход функция получает целое
# число n_customers (количество клиентов).


def clients1(n_customers: int):
    n_id = 0
    for i in range(n_id, n_customers):
        sum_clients = n_id + i
    return sum_clients + 1

print(clients1(100))

# Функция, аналогичная первой, если ID начинается с произвольного числа.
# На вход функция получает целые числа: n_customers (количество клиентов) и
# n_first_id (первый ID в последовательности).


def clients2(n_first_id: int, n_customers: int):
    for i in range(n_first_id, n_customers):
        sum_clients = i - n_first_id
    return sum_clients + 1

print(clients2(12, 100))
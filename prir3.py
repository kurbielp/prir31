import math,sys,time
import pp

# Liczba "procesow"
N = 8
# Macierz wejsciowa
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 1, 2],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 1, 2],
    [3, 4, 5],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 1, 2],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 1, 2],
    [3, 4, 5],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 1, 2],
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0, 1, 2],
    [3, 4, 5]
]
# Wektor wejsciowy
x = [
    1,
    1,
    1
]

def print_matrix(matrix):
    for row in matrix:
        print row

def count_result(id, tasks, number, A, x):
    pos_start = id * number
    if pos_start >= len(A):
        return None;
    if id == tasks - 1:
        pos_stop = len(A)
    else:
        pos_stop = pos_start + number
    cell = pos_start
    res = []
    while cell < pos_stop:
        row = A[cell]
        cell_res = 0
        for i in range(len(row)):
            cell_res += row[i] * x[i]
        res.append(cell_res)
        cell += 1
    return res

print "Macierz wejsciowa"
print_matrix(A)
print "Wektor wejsciowy"
print x

job_server = pp.Server()
parallels = []

cells_per_task = int(round(len(A) / float(N)))
if cells_per_task < 1:
    cells_per_task = 1

#start tumera
start_time = time.time()

print "Zlecam zadania"
for i in range(N):
    parallels.append(job_server.submit(count_result, (i, N, cells_per_task, A, x)))

print "Zbieram wyniki"
res =[]
for i in range(N):
    task_res = parallels[i]()
    print "Zadanie zwrocilo ", task_res
    if task_res:
        res.extend(task_res)
print res

print "Time elapsed: ", time.time() - start_time, "s"
import math, sys, time
import pp


def mnoz(dane):
	A = dane[0]
	X = dane[1]

	nrows = len(A)
	ncols = len(A[0])
	y = []
	for i in xrange(nrows):
		s = 0
		for c in range(0, ncols):
			s += A[i][c] * X[c][0]
			time.sleep(0.1)

		y.append(s)

	return y

def read(fname):
	f = open(fname, "r")
	nr = int(f.readline())
	nc = int(f.readline())

	A = [[0] * nc for x in xrange(nr)]
	r = 0
	c = 0
	for i in range(0,nr*nc):
		A[r][c] = float(f.readline())
		c += 1
		if c == nc:
			c = 0
			r += 1

	return A

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
            cell_res += row[i] * x[i][0]
        res.append(cell_res)
        cell += 1
    return res

ncpus = int(sys.argv[1]) if len(sys.argv) > 1 else 2
fnameA =  sys.argv[2] if len(sys.argv) > 3 else "AA.dat"
fnameX = sys.argv[3] if len(sys.argv) > 3 else "XX.dat"


A = read(fnameA)

X = read(fnameX)
'''
print "wypsuje a \n"
print A
print "wypisuje x \n"
print X
'''

job_server = pp.Server()
parallels = []
threads_number = 1

cells_per_task = int(round(len(A) / float(threads_number)))
if cells_per_task < 1:
    cells_per_task = 1

#start tumera
start_time = time.time()

print "Zlecam zadania"
for i in range(threads_number):
    parallels.append(job_server.submit(count_result, (i, threads_number, cells_per_task, A, X)))

print "Zbieram wyniki"
res =[]
for i in range(threads_number):
    task_res = parallels[i]()
    print "Zadanie zwrocilo ", task_res
    if task_res:
        res.extend(task_res)
print res
print "Time elapsed: ", time.time() - start_time, "s"
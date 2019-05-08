import multiprocessing as mp

def my_func(x):
    print("The power of ", x, ' is ', x**x, ' ---done by ', mp.current_process().name)

def main():
    print(mp.cpu_count())

    #mp.Pool dictates that max amount of cores that can be used, Pool is a constructor with methods
    pool = mp.Pool(mp.cpu_count())
    firstList = [1,2,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    secondList = [2,4,6]

    print('*' * 25)
    print('\t First List')
    pool.map(my_func, firstList)

    print('*' * 25)
    pool.map(my_func,secondList)

if __name__ == "__main__":
    main()

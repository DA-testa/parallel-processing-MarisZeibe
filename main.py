# python3

def parallel_processing(n, m, data):
    output = []
    threads = [0]*n
    time = 0
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    while len(data) > 0:
        freeThreadIndex = min(range(n), key=lambda i : threads[i])
        time += threads[freeThreadIndex]
        output.append((freeThreadIndex, time))
        threads = [x-threads[freeThreadIndex] for x in threads]
        threads[freeThreadIndex] = data.pop(0)

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for x in result:
        print(x[0], x[1])



if __name__ == "__main__":
    main()

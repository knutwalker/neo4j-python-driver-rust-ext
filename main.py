from timeit import default_timer as timer 


def main():
    start = timer()
    print('Hello World!')
    end = timer()
    print_time(start, end)


def print_time(start, end):
    ms = int((end - start) * 1000) 
    print('Time elapsed: {}ms'.format(ms))


if __name__ == '__main__':
    main()
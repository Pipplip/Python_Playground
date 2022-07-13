
start_value = 19
current_loop = 0
max_loop = 50

def calc(value):
    global current_loop
    global max_loop

    print(int(value), end=" ")

    if max_loop == current_loop:
        return

    current_loop += 1

    if value % 2 == 0:
        calc(value/2)
    else:
        calc(3*value+1)

if __name__ == "__main__":
    calc(start_value)

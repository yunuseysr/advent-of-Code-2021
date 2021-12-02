

class Dive():
    datas = []
    with open("C:\\Users\\yunus\\OneDrive\\Masaüstü\\AdventofCode\\2021\\Day - 2\\input.txt") as f:
        datas = f.readlines()

    def positions(lines):

        horizontal, depth, aim = 0,0, 0 #Part -2 has aim

        for line in lines:
            line, value = line.split()
            value = int(value)


            if line == "forward":
                horizontal += value
                depth += aim * value # Part -2 depth in "forward"
            elif line == "down":
                aim += value # Part -1 depth += value 
            else:
                aim -= value # Part -2 depth -= value
        return print(horizontal *depth)


    positions(datas)


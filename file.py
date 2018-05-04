try:
    infile = open("WORDS1.txt", "r")
    lines = infile.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].rstrip()

    num_lines = 0
    cal_int = []
    for line in lines:
        for i in lines:
            cal_int.append(i)
        num_lines += 1
    print(cal_int)

except FileNotFoundError:
    print("WORDS1.txt is not found")

import os

def solution():
    # read input
    list1 = []
    list2 = []
    ans = 0

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "./input.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path, "r") as file:
        content = file.readlines()
        for line in content:
            data = line.rstrip("\n").split()
            list1.append(int(data[0]))
            list2.append(int(data[1]))
    
    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        ans += abs(list1[i] - list2[i])
    return ans
print(solution())
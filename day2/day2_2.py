import os

def solution():
    numSafe = 0

    script_dir = os.path.dirname(__file__)
    rel_path = "./input.txt"
    file_path = os.path.join(script_dir, rel_path)

    with open(file_path, "r") as input:
        content = input.readlines()
        for line in content:
            data = line.rstrip("\n").split()
            if check_safe(data):
                numSafe += 1
            else: # unsafe, check removing levels
                for i in range(len(data)):
                    testLevel = data.copy()
                    testLevel.pop(i)
                    if check_safe(testLevel):
                        numSafe += 1
                        break
    return numSafe

def check_safe(data):
    increasing = None
    safe = True
    for i in range(len(data) - 1):
        diff = int(data[i]) - int(data[i + 1])
        if increasing == None:
            increasing = diff < 0
        if (abs(diff) < 1 or abs(diff) > 3) or (increasing and diff > 0) or (not increasing and diff < 0):
            safe = False
    return safe


print(solution())
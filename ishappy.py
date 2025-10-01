import math
import os

def isHappy(n):
    happyNumbers = []
    while n != 1 and n not in happyNumbers:
        happyNumbers.append(n)
        n = sum(int(x)**2 for x in str(n))
    return n == 1

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    os.makedirs("bind_mount", exist_ok=True)

    with open("bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to bind_mount/output.txt")



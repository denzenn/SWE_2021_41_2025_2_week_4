import math
import os

def isHappy(n):
    happyNumbers = []
    for i in range(int(math.log10(n)) + 1):
        number = int(n / pow(10, int(math.log10(n)) - i))
        nextNumber = number
        if nextNumber > 10:
            number = nextNumber % 10
        happyNumbers.append(number)

    result = [x**2 for x in happyNumbers]
    planB = sum(result)
    return planB == 1

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    os.makedirs("/app/bind_mount", exist_ok=True)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")


git add divisors.py
git commit -m "Add divisors.py"
git push origin main
import sys

number = int(sys.argv[1])

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")

print()

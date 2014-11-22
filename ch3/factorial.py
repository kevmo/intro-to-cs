from sys import argv


num = int(argv[1])


def factorial():
    result = 1

    for i in range(num, 1, -1):
        result *= i

    return result

print factorial()

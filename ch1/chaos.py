def main():
  x = input("Enter a number between 0 and 1: ")
  y = input("Enter another number between 0 and 1:")
  for i in range(11):
    x = x * (1 - x) * 3.7
    y = y * (1-y) * 3.7
    print "|  ", x, "  |  ", y, "  |  l"

if __name__ == '__main__':
  main()

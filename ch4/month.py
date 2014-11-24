from sys import argv

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

def main():

    month = int(argv[1])

    start_index = 3 * (month - 1)
    end_index = start_index + 3

    return months[start_index:end_index]

print main()
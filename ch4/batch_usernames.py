import string


def main():
    """This program creates a file of user names."""

    infileName = raw_input("Which file are the names in? ")
    outfileName = raw_input("Into which file should we place the user names?")

    infile = open(infileName, 'r')
    outfile = open(outfileName, 'w')

    for line in infile:
        first, last = string.split(line)

        uname = string.lower(first[0] + last[:7])

        outfile.write(uname + '\n')

    infile.close()
    outfile.close()

    print "Done."

main()

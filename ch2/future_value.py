def main():
    prompt = "->"

    print "We gon figure out how much money you'll have in 10 years."

    print "What's the principal amount of money?"
    principal = int(raw_input(prompt))

    print "What's the interest rate?"
    interest = int(raw_input(prompt))

    for i in range(10):
        principal = principal * (1 + (interest/100.0))

    print "You'll have {0} dollars in 10 years.".format(principal)

main()


def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """

    counter = range(start, stop+1)
    for count in counter:
        print(count)


##count_up(5, 7)

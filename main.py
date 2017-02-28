import get_input
import find_disjoint_sets
import find_sets
import time
import sys


def main():
    # get input file name from command line argument
    file_name = sys.argv[1]

    start_time = time.time()
    # parse the input and return a list of cards
    list_of_cards = get_input.get_input(file_name)

    # find the number of SET's
    no_of_sets, list_of_sets = find_sets.find_set(list_of_cards)

    # find the disjoint SET's
    no_of_disjoint_sets,list_of_disjoint_sets  = find_disjoint_sets.find_disjoint(list_of_sets)

    print("Execution time : %s" % (time.time() - start_time))

    # print the results
    print(no_of_sets)
    print(no_of_disjoint_sets)
    print()
    for y in list_of_disjoint_sets:
        for z in range(3):
            print(y[z])
        print()
    print("Execution time : %s" % (time.time() - start_time))

if __name__ == '__main__':
    main()
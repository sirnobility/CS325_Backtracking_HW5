# Name: Peter Orndoff
# Class: CS 325 - Analysis of Algorithms.
# Description: Given a list of hungry dogs & biscuits, returns the maximum number of dogs that can be fed.

def feedDog(dog_hunger_list, biscuit_list):
    """
    Greedy Algorithm Implementation. Both lists are iterated through which results in a (O)n^2 worst case runtime.

    :param dog_hunger_list: Passed hunger level of dogs
    :param biscuit_list: Passed biscuit size
    :return: Returns the number of Dogs that can be fed
    """

    # Start by sorting passed lists from large to small values.

    number_of_biscuits = len(biscuit_list)  # Grabs number of biscuits
    number_of_dogs = len(dog_hunger_list)  # Grabs number of dogs.

    dog_sorted = sorted(dog_hunger_list)
    biscuit_sorted = sorted(biscuit_list)

    print(dog_sorted, biscuit_sorted)

    if dog_sorted[0] < biscuit_sorted[0]:
        return 0

    dogs_fed = 0
    dog_iterator = 0
    biscuit_iterator = 0

    iterator_stop = min(number_of_dogs, number_of_biscuits)

    while dog_iterator != iterator_stop or biscuit_iterator != iterator_stop:

        if biscuit_iterator > len(biscuit_sorted) - 1:
            return dogs_fed

        if dog_iterator > len(dog_sorted) - 1:
            return dogs_fed

        if dog_sorted[dog_iterator] <= biscuit_sorted[biscuit_iterator]:

            dog_iterator += 1
            biscuit_iterator += 1
            dogs_fed += 1

        elif dog_sorted[dog_iterator] > biscuit_sorted[biscuit_iterator] and biscuit_iterator + 1 < iterator_stop:
            biscuit_iterator += 1

        else:
            dog_iterator += 1
            biscuit_iterator += 1

    return dogs_fed

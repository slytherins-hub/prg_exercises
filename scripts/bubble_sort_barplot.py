import random

import matplotlib.pyplot as plt


def bubble_sort(values):

    for end in range(len(values) - 1, 0, -1):
        swapped = False
        for index in range(end):
            if values[index] > values[index + 1]:
                values[index], values[index + 1] = values[index + 1], values[index]
                swapped = True


            index_highlight1 = index
            index_highlight2 = index + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("XXX Sort")
            plt.pause(0.01)
            

        if not swapped:
            break


    return values


if __name__ == "__main__":
    numbers = random.sample(range(5, 200), 20)
    print("Puvodni seznam:", numbers)
    sorted_numbers = bubble_sort(numbers)
    print("Serazeny seznam:", sorted_numbers)

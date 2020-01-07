import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walk as long as the program is active
while True:
    # Make a Random Walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in thw walk
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors = 'none', s=15)

    #Show the random walk
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

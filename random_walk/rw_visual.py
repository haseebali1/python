import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Keep making new walk as long as the program is active
while True:
    # Make a Random Walk
    rw = RandomWalk()
    rw.fill_walk()

    # Plot the points in thw walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(19.2, 10.8))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
            edgecolors = 'none', s=15)

    #Emphasize the first and the last points
    ax.scatter(0, 0, c='green', edgecolors='none', s =100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
            edgecolors='none', s =100)

    #Show the random walk
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

import matplotlib.pyplot as plt
from randomwalk import RandomWalk
while True:
    rw =RandomWalk()
    rw.fill_walk()
    plt.style.use('classic')
    fig,ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values,s = 15, c = point_numbers, cmap=plt.cm.Blues)
    plt.show()
    keepwalk = input('是否继续呢？Y/N:')
    if keepwalk == 'N' and 'n':

        break
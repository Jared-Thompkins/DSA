"""
Game of Hot potato. Rules:
Start with a group of people in a circle. One person
is holding a potato, Each turn the person passes it
N people to their left. The person with the potato gives it to the
person to their left and leaves the circle.
"""


from pythonds.basic.queue import Queue

def hotPotato(namelist, num):
    simQueue = Queue()
    for name in namelist:
        simQueue.enqueue(name)

    while simQueue.size() > 1:
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())

        simQueue.dequeue()

    return simQueue.dequeue()


print(hotPotato(["Bill", "Bob", "Betsy", "Dave", "Trish"], 3))

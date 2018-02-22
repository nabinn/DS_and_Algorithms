from simple_queue import Queue


def hot_potato(namelist, num):
    """ Simulation of hot potato game.
    :param namelist: a list of names
    :param num: a constant used for counting
    :return: name of the last person remaining after
    repetitive counting by num

    Assume that the person holding the potato will be
    at the front of the queue. Upon passing the potato,
    the simulation will simply dequeue and then immediately
    enqueue that person, putting her at the end of the line.
    She will then wait until all the others have been at the
    front before it will be her turn again.
    After num dequeue/enqueue operations, the person at the front
    will be removed permanently and another cycle will begin.
    This process will continue until only one name remains
    (the size of the queue is 1).
    """
    simple_queue = Queue()
    for name in namelist:
        simple_queue.enqueue(name)

    while simple_queue.size() > 1:
        for i in range(num):
            simple_queue.enqueue(simple_queue.dequeue())

        simple_queue.dequeue()

    return simple_queue.dequeue()


if __name__ == "__main__":
    names = ["Bill","David","Susan","Jane","Kent","Brad"]
    winner = hot_potato(names, 7)
    print(winner)
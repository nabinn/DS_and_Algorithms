"""Simulation of printer operation, referenced from:
http://interactivepython.org/runestone/static/pythonds/BasicDS/SimulationPrintingTasks.html
"""

import random
from simple_queue import Queue


class Task:
    """
    The Task class represents a single printing task.
    When the task is created, a random number generator
    will provide a length from 1 to 20 pages.
    """
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.pages = random.randrange(1, 21)

    def get_timestamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


class Printer:
    """
    The Printer class tracks whether it has a current task.
    If it does, then it is busy and the amount of time needed
    can be computed from the number of pages in the task.
    The constructor allows the pages-per-minute setting to be
    initialized. The tick method decrements the internal timer
    and sets the printer to idle if the task is completed.
    """
    def __init__(self, page_per_min):
        self.page_rate = page_per_min
        self.current_task = None
        self.time_remaining = 0

    def busy(self):
        return self.current_task is not None

    def tick(self):
        """decrements the internal timer and sets the printer to idle
        if the task is completed."""
        if self.busy():
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


def new_print_task():
    """Decides whether a new printing task has been created.
    Print tasks arrive once every 180 seconds. So the random
    event can be simulated by arbitrarily choosing 180 from
    a range of random integers.
    """
    num = random.randrange(1, 181)
    return num == 180


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range (num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if not lab_printer.busy() and not print_queue.is_empty():
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining"%(average_wait,
                                                         print_queue.size()))


if __name__ == "__main__":
    # running 10 trials. In each trial:
    # running simulation for a period of 1 hour (3600 s)
    # using a page rate of 5 pages per minute.
    for i in range(10):
        simulation(3600, 5)
    print("---------------------")
    # using a page rate of 10 pages per minute
    for i in range(10):
        simulation(3600, 10)

import threading
import philosophers
import time
import curses

visualization = curses.initscr()

visualization.immedok(True)

def DiningPhilosophersProblem():
    
    forks = [threading.Lock() for i in range(5)]
        
    philosopher_array = [philosophers.Philosopher(i, forks[i], forks[(i+1)%5], visualization) for i in range(5)]


    for i in philosopher_array:
        i.start()

    
    time.sleep(50)

    for i in philosopher_array:
        i.alive = False



DiningPhilosophersProblem()

curses.endwin()









import threading, time, random, curses


class Philosopher(threading.Thread):

    alive = True

    def __init__(self, my_number, fork_on_the_left, fork_on_the_right, screen):

        threading.Thread.__init__(self)

        self.my_name = 'P'+str(my_number)
        self.fork_on_the_left = fork_on_the_left
        self.fork_on_the_right = fork_on_the_right

        self.left_fork_number = my_number
        self.right_fork_number = (my_number+1)%5

        self.screen_x_position = my_number*20

        self.win = curses.newwin(10, 20, 10, self.screen_x_position)
        self.win.immedok(True)

        self.win_fork = curses.newwin(10, 20, 20, self.screen_x_position)
        self.win_fork.immedok(True)

    def run(self):
        
        while(self.alive):

            #thinking..    
            self.win.erase()
            self.win.addstr(self.my_name + ' is thinking..')

            time.sleep(random.uniform(3,6))

            #hungry..
            self.win.erase()
            self.win.addstr(self.my_name + ' is hungry :(')


            while(self.alive):
                                    
                self.fork_on_the_left.acquire(True)

                if self.fork_on_the_right.acquire(False):

                    #eating..
                    self.win.erase()
                    self.win.addstr(self.my_name + ' is eating :)')
                    
                    self.win_fork.erase()
                    self.win_fork.addstr(self.my_name+' using fork '+str(self.left_fork_number) + ' '+str(self.right_fork_number))

                    time.sleep(random.uniform(3,6))

                    self.fork_on_the_left.release()
                    self.fork_on_the_right.release()

                    self.win_fork.erase()
                    break

                else:
                    self.fork_on_the_left.release()
                    continue 

        




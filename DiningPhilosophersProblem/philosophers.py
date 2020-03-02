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

        self.screen_x_position = my_number*30

        self.win = curses.newwin(10, 30, 10, self.screen_x_position)
        self.win.immedok(True)

        self.win_fork = curses.newwin(10, 30, 20, self.screen_x_position)
        self.win_fork.immedok(True)

    def run(self):
        
        while(self.alive):

            #thinking..    
            for i in range(5):
                self.win.erase()
                self.win.addstr(self.my_name + ' is thinking'+'.'*i)

                time.sleep(random.uniform(0.7,1.0))

            #hungry..
            self.win.erase()
            self.win.addstr(self.my_name + ' is hungry :(')


            while(self.alive):
                                    
                if self.fork_on_the_left.acquire(True, 5):

                    if self.fork_on_the_right.acquire(False):

                        #eating..
                    
                        for i in range(5):

                            self.win.erase()
                            self.win.addstr(self.my_name + ' is eating :)'+'.'*i)
                    
                            self.win_fork.erase()
                            self.win_fork.addstr(self.my_name+' using fork '+str(self.left_fork_number) + ' '+str(self.right_fork_number))

                            time.sleep(random.uniform(0.7,1.0))

                        self.fork_on_the_left.release()
                        self.fork_on_the_right.release()

                        self.win_fork.erase()
                        break

                    else:
                        self.fork_on_the_left.release()
                        continue 
                else:
                    time.sleep(0.5)
                    continue

        




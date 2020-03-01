import threading, time, random


class Philosopher(threading.Thread):

    alive = True

    def __init__(self, my_name, fork_on_the_left, fork_on_the_right):

        threading.Thread.__init__(self)

        self.my_name = my_name
        self.fork_on_the_left = fork_on_the_left
        self.fork_on_the_right = fork_on_the_right

    def run(self):
        
        while(self.alive):

            #thinking..    
            print(self.my_name + 'is thinking..')
            time.sleep(random.uniform(1,3))

            #hungry..
            print(self.my_name + 'is hungry :(')

            while(self.alive):
                
                if self.fork_on_the_left.acquire(False):
                    
                    self.fork_on_the_left.acquire()

                    if self.fork_on_the_right.acquire(False):

                        self.fork_on_the_right.acquire()

                        #eating..
                        print(self.my_name + 'is eating :)')
                        time.sleep(random.uniform(1,3))
                        self.fork_on_the_left.release()
                        self.fork_on_the_right.release()
                        break

                    else:
                        self.fork_on_the_left.release()
                        continue    
                else:
                    continue

        




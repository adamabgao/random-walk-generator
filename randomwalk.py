from random import choice
class RandomWalk:
    '''A class to generate random walk data.'''

    def __init__(self, num_steps=5000):
        '''Initialize attributes for a random walk.'''
        #init coordinates
        self.num_steps = num_steps
        self.x_list = [0]
        self.y_list = [0]

        #storage
        self.walks_list = []

    def go_for_walk(self):
        '''Generate random walk coordinates.'''
        while len(self.x_list) < self.num_steps:
            x_step, y_step = self.random_steps()
            if x_step == 0 and y_step == 0:  
                continue

            x = self.x_list[-1] + x_step
            y = self.y_list[-1] + y_step
            self.x_list.append(x)
            self.y_list.append(y)
        
        return self.x_list, self.y_list

    def random_steps(self):
        '''Generate a random step in x and y directions.'''
        x_direction = choice([1, -1])
        x_distance = choice(range(1, 11))
        x_step = x_direction * x_distance

        y_direction = choice([1, -1])
        y_distance = choice(range(1, 11))
        y_step = y_direction * y_distance

        return x_step, y_step

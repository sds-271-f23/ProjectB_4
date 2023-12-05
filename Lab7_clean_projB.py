#Group D
import random 
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn

class monte_carlo_pi():
    def __init__(self, length, radius, darts_monte_carlo_number):
        """
        Initializes class of monte_carlo_pi and sets attributes self.length, self.radius, and self.darts_monte_carlo_number
        ------
        Params
        
        :param length: (int) length of square
        :param radius: (int) radius of circle
        :param darts_monte_carlo_number: (int) number of dart throws and number of monte carlo reps
        ------
        :returns: Nothing
        """
        self.length = length
        self.radius = radius
        self.darts_monte_carlo_number = darts_monte_carlo_number


    
    def create_visualization(self, xy_info_df):
        """
        Creates scatterplot visualization for set of one dart throws
        ------
        Params
        
        :param xy_info_df: (dataframe) dataframe that stores the number of dart throws inside the circle and outside the circle
        ------
        :return: None
        """
        x = []
        y = []
        for i in xy_info_df:
            x.append(i[0])
            y.append(i[1])

        plt.scatter(x, y, label='visualization')
        plt.legend()
        plt.show()

    
    def rand_point_generator(self):
        """
        Generates random points for dart throws
        :returns: points_list: (list) list of x,y pair for points
        """
        li = []
        for i in range(self.darts_monte_carlo_number):
            x = random.randint(0, self.length)
            y = random.randint(0, self.length)
            pair = [x,y]
            li.append(pair)
        return li


        
    
    
    def in_circle(self, points_list):
        """
        Checks to see if generated dart throw points are inside or outside circle
        ------
        Params
        
        :param points_list: (list) list of x,y pair for points
        ------
        :returns: inside_circle_count (int) number of dart throws that are inside the circle
        """
        center = [self.length/2,self.length/2]
        count = 0
        for i in points_list:
            dis= math.dist(center,i)
            if dis < self.radius:
                count +=1
        return count

    
    def calc_pi(self):
        """
        Calculate estimate of pi 
        :returns: [pi, inside_circle_return] (list) list containing estimate of pi and number of dart throws inside circle
        """
        points_list = self.rand_point_generator()
        count = self.in_circle(points_list)
        return count/self.darts_monte_carlo_number
    
    def monte_carlo_reps(self):
        """
        Do Monte Carlo repetitions on dart throws and save pi estimate errors for each set of throws to calculate standard error
        :returns: [pi_estimate_average, std_error_of_pi_estimate] (list) list of average pi estimate and standard error of estimate
        """
            # appends inside circle result to overall list for all monte carlo reps for
            # storage in pd.DataFrame later
            # adds pi estimate error to error total to calculate std error
            # adds pi estimate to pi estimate total to calculate avg pi estimate later
        # calculates standard deviation of the pi estimates 
        # calculates average pi estimate 
        temp=[]
        for i in range(self.darts_monte_carlo_number):
            temp.append(self.calc_pi())
        ave = np.average(temp)
        std_error= np.std(temp)
        return [ave, std_error]
        








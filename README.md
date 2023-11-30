# SDS271Lab7

## Prompt

Your class should:

- store the length, radius, number of monte carlo iterations, and number of dart throws as internal attributes (you can choose between class and instance attributes as you see fit)
- simulate some large (but variable) number of dart throws inside the square
- calculate how many of those throws also landed inside the circle if the circle is centered in the middle of the square
- store the results of each experiment (set of dart throws) in a dataframe
- use the relationship between the area of a circle and the area of a square to estimate pi from those two numbers (with error!)
- create a visualization of the simulation (the dart throws on the circle/square)
- return the estimate of pi along with the standard error on that estimation

# README

Our module supplies classes for estimating the value of pi using a circle inscribed in a square.

<h3><i>class</i> monte_carlo_pi(length, radius, darts_monte_carlo)</h3>

A **monte_carlo_pi** object represents a calculator that, given the dimensions of a circle inscribed in a square, stimulates dart throws, visualizes the dart throws in and outside the circle, and uses information from the dart throws to estimate pi. 

<h4><i>classmethod</i> monte_carlo_pi.create_visualization(dataframe)</h4>

Creates scatterplot visualization for set of one dart throws

**Parameters:**

dataframe : *dataframe*
dataframe that stores the number of dart throws inside the circle and outside the circle

**Returns**

None

**Example**
```
# create instance of class
mcp = monte_carlo_pi(8, 4, 1000)
# call class method; the following method produces a plot of the dart throw set where points inside the circle are one color and points outside the circle are a different color
mcp.create_visualization()
```

<h4><i>classmethod</i> monte_carlo_pi.rand_point_generator(radius = monte_carlo_pi.radius, darts_monte_carlo_number = monte_carlo_pi.darts_monte_carlo)</h4>

Generates random points for dart throw set

**Parameters:**

radius : *int*
integer that represents the radius of the circle

darts_monte_carlo_number : *int*
integer that represents number of dart throws per set

**Returns**

out: *list*
list of x,y coordinate pairs for each dart throw in set

**Example**
```
# create instance of class
mcp = monte_carlo_pi(8, 4, 1000)
# call class method; the following method uses the instance attributes of self.radius and self.darts_monte_carlo_number to randomly generate x,y coordinate pairs for dart throws for self.darts_monte_carlo_number of throws and returns a list of those points 
mcp.rand_point_generator() -> list
```

<h4><i>classmethod</i> monte_carlo_pi.in_circle(list)</h4>

Checks to see if generated dart throw points are inside or outside circle and records results

**Parameters:**

list : *list*
list of x,y coordinate pairs for each dart throw in set

**Returns**

out: *int*
number of dart throws that are inside the circle

**Example**
```
# create instance of class
mcp = monte_carlo_pi(8, 4, 1000)
# call class method; the following method uses the list returned from the monte_carlo_pi.rand_point_generator() class method to calculate the numbers of dart throws inside the circle and returns that number
mcp.in_circle() -> int
```

<h4><i>classmethod</i> monte_carlo_pi.calc_pi()</h4>

Calculate estimate of pi

**Parameters:**

Calls monte_carlo_pi.in_circle() and uses result to calculate percentage of dart throws inside circle of the total

**Returns**

out: *tuple*
(estimate of pi, percent of dart throws that are inside the circle of total)

**Example**
```
# create instance of class
mcp = monte_carlo_pi(8, 4, 1000)
# call class method; the following method estimates pi using the return from monte_carlo_pi.in_circle() -> int divided by self.darts_monte_carlo_number, the total number of dart throws in a set, to estimate pi, and returns that pi estimate
mcp.calc_pi() -> int
```

<h4><i>classmethod</i> monte_carlo_pi.monte_carlo_reps()</h4>

Does Monte Carlo repetitions on dart throw sets and saves pi estimate errors for each set of throws to calculate overall standard error

**Parameters:**

None

**Returns**

out: *list*
[average estimate of pi, standard error of estimate of pi]

**Example**
```
# create instance of class
mcp = monte_carlo_pi(8, 4, 1000)
# call class method; the following method runs self.darts_monte_carlo number of monte carlo repetitions on the dart throw process and averages the pi estimate results and errors from each dart throw set and returns them
mcp.monte_carlo_reps() -> int
```

**Instance attributes:**

- monte_carlo_pi.**length**

The length of one side of the square that inscribes the circle

- monte_carlo_pi.**radius**

The radius of the circle inscribed in the square

- monte_carlo_pi.**darts_monte_carlo**

The number of dart throws per set and number of monte carlo repetitions (how many times we repeat a dart throw set)



## Docstrings and Comments For Class Methods
```class monte_carlo_pi():
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
        def create_visualization(self, xy_info_df):
                """
                Creates scatterplot visualization for set of one dart throws
                ------
                Params
                
                :param xy_info_df: (dataframe) dataframe that stores the number of dart throws inside the circle and outside the circle
                ------
                :return: None
                """
                
        def rand_point_generator(self):
                """
                Generates random points for dart throws
                :returns: points_list: (list) list of x,y pair for points
                """
         def in_circle(self, points_list):
                """
                Checks to see if generated dart throw points are inside or outside circle
                ------
                Params
                
                :param points_list: (list) list of x,y pair for points
                ------
                :returns: inside_circle_count (int) number of dart throws that are inside the circle
                """
        def calc_pi(self):
                """
                Calculate estimate of pi 
                :returns: [pi, inside_circle_return] (list) list containing estimate of pi and number of dart throws inside circle
                """
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
```












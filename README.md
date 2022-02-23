# projplot

[Under construction]

Developed by Kanika Chopra and Dr. Martin Lysy (2022)

This package is created to assist with testing optimization when building optimizers by providing additional visualizations. If a plot is pinpointed to a certain area (zoomed in) or too generalized (zoomed out), there can be misinterpretations regarding optimality. For example, a graph can look as if it has (has not) reached its optimal values despite it being the opposite. Two examples of plots that are misleading despite not being at the optimal value are given below. Figure 1 shows a plot that is too zoomed in and Figure 2 shows a plot that is too zoomed out. In both of these plots, we are misled about the optimal value. 

Figure 1: A misleading plot due to being too zoomed in

<img src="/docs/zoomedin.png" alt = "Plot zoomed in">


Figure 2: A misleading plot due to being too zoomed in

<img src="/docs/zoomedout.png" alt = "Plot zoomed out">

Although the optimal value calculated for x2 is is 1.647 this appears to be at 1.6 for the Figure 1 and around 2 for Figure 2. 

`projplot` provides an additional visual assessment of optimality. A plot is generated for each theta value being optimized. This plot varies the respective theta value while holding the other variables constant. This helps to determine if the specific theta has been optimized based on an upper and lower limit (provided by the user). 

For example, if we were optimizing `theta` and `mu`, we would have one plot where `mu` is held constant and `theta` is varying. This plot would show how the results of the objective function vary based on `theta`. By analysing this plot, we are able to determine if `theta` has reached its optimal value. An example of this plot can be found in the Examples section. 

## Contents

* `src/projplots`: contains the project directory for the projplot package. 
* `src/projplots/proj.py`: This file contains the functions needed to generate these varying plots. 
    * `projxvals()` generates a x-value matrix that has each variation of altering one x-variable, while holding others constaint. The x-values are the thetas that are being optimized. 
    * `projplot()` produces a plot for each x value based on a DataFrame containing the varying x value and corresponding calculated y. 
    * `projdata()`: will take a objective function and the x-value matrix generated and will create a DataFrame with the varying x-value and respective y-value. This will return the DataFrame and also plot the values using `projplot`.
* `src/test`: containts a package to test `projplot`.

## Examples

An overview of the package functionality is illustrated with the following example. Let `Q(x) = x^TAx - 2b^Tx` denote a quadratic objective function in `x` is in the d-dimensional real space. If `A` is a positive-definite matrix, then the unique minimum of `Q(x)` is `x̂ =A^{-1}b` (A inverse * b). 

For example, let 
A = [[3,2],
     [2,7]]

and 
b = [1,
     10]

Then we have that the optimal solution is `x̂ = (-0.765, 1.647)`. Now, `projplot` allows us to complete a visual check. As the user of this program, you will need to provide the following information:

* Objective function (`obj_fun`): This can be either a vectorized or non-vectorized function. 
*  Optimal values (`theta`): This will be the optimal solution for your function. 
*  Upper and lower bounds for each theta (`theta_lims`): This will provide an initial range of values to observe.
*  Parameter names (`theta_names`): These are the names of your parameters, i.e. theta, mu, sigma
*  Number of points to plot for each parameter (`n_pts`): This is the number of points that each parameter will be evaluated at for their respective plot. 

### Setup
```python
# Optimal values
theta = np.array([-0.76470588,  1.64705882])

# Upper and lower bounds
theta_lims = np.array([[-3., 1], [0, 4]])

# Parameter names
theta_names = ["x1", "x2"]

# Number of evaluation points per coordinate
n_pts = 10
```

### Vectorized Function
```python
from projplot import projxvals
from projplot import projdata

# Define vectorized function
def obj_fun(x):
    '''
    Params: 
        x: x is a nx2 vector

    Returns:
        The output of x'Ax - 2b'x
    '''
    # Transpose the x vector so it is 2xn where n is 2 * number of data points 
    x = x.T 
    A = np.array([[3,2], [2,7]])
    b = np.array((1,10)).T
    
    y = np.diag(x.T.dot(A).dot(x)) - 2 * b.dot(x)
        
    return y

# Generate first round of x_values
x_vals = projxvals(theta, theta_lims, n_pts)

# Obtain y_values and plots
plot_data = projdata(obj_fun, x_vals, theta_names, is_vectorized=True)
```

Below, we have the projection plot using this data and objective function. 

<img src="/docs/plot1.png" alt = "Plot from vectorized function">

### Non-Vectorized Function
```python
from projplot import projxvals
from projplot import projdata

# Define function
def obj_fun(x):
    '''
    Params: 
        x: x is a 2x1 vector

    Returns:
        The output of x'Ax - 2b'x
    '''
    A = np.array([[3,2], [2,7]])
    b = np.array((1,10)).T
    
    y = x.dot(A) @ x - 2 * b.dot(x) 

    return y

# Generate first round of x_values
x_vals = projxvals(theta, theta_lims, n_pts)

# Obtain y_values and plots
plot_data = projdata(obj_fun, x_vals, theta_names, is_vectorized=False)
```

Below, we have the projection plot using this data and objective function. 

<img src="/docs/plot2.png" alt = "Plot from non-vectorized function">

We can see that the produced plots for the vectorized and non-vectorized function are identical. Vectorized functions have the advantage of running more efficiently; however, are not necessary to utilize this tool.

## FAQ

**Does my function need to be vectorized?** 

No, it does not need to be vectorized in order for you to use this tool. There is a `is_vectorized` parameter that allows for both vectorized functions and non-vectorized functions. If your function is not vectorized, we will iterate through the x-values to generate the x-value matrix that will be used for the projection plots. If your function is vectorized, this will run more efficiently with generating the projection plots. 

**What is the point of generating the x-value matrix separately?**

The x-value matrix generates the combinations with the varying thetas that we will be inputting into the objective function to visualize the resulting changes in the output. By having this outputted separately, the user is able to view the values that will be inputted prior to plotting and alter it. In the future, an `equalize()` function will be added to fine-tune the scale to be more accurate. An example of what the x-value matrix looks like is given below (based on the example above): 

<img src="/docs/x_vals.png" alt = "Example of x-vals matrix">

**Can I see the data that is plotted as a DataFrame?**
In the examples above, you'll notice that the output of the `projdata()` function is set in the variable `plot_data`. If we were to call the `plot_data` variable, we would have the following DataFrame outputted (based on the example above):

<img src="/docs/plot_data.png" alt = "Example of plot_data DataFrame">

*This package will have a similar goal to `OptimCheck` in R.*

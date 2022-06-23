# projplot

*Kanika Chopra, Martin Lysy*

This package is created to assist with testing optimization when building optimizers by providing additional visualizations. If a plot is pinpointed to a certain area (zoomed in) or too generalized (zoomed out), there can be misinterpretations regarding optimality. For example, a graph can look as if it has (has not) reached its optimal values despite it being the opposite. Two examples of plots that are misleading despite not being at the optimal value are given below. Figure 1 shows a plot that is too zoomed in and Figure 2 shows a plot that is too zoomed out. In both of these plots, we are misled about the optimal value. 

Figure 1: A misleading plot due to being too zoomed in

<img src="docs/pages/images/zoomedin.png" alt = "Plot zoomed in">


Figure 2: A misleading plot due to being too zoomed in

<img src="docs/pages/images/zoomedout.png" alt = "Plot zoomed out">

Although the optimal value calculated for x2 is is 1.647 this appears to be at 1.6 for the Figure 1 and around 2 for Figure 2. 

`projplot` provides an additional visual assessment of optimality. A plot is generated for each parameter value being optimized. This plot varies the respective parameter value while holding the other variables constant. This helps to determine if the specific parameter has been optimized based on an upper and lower limit (provided by the user). 

For example, if we were optimizing `theta` and `mu`, we would have one plot where `mu` is held constant and `theta` is varying. This plot would show how the results of the objective function vary based on `theta`. By analysing this plot, we are able to determine if `theta` has reached its optimal value. An example of this plot can be found in the Examples section. 

This package has a similar goal to the R package [**optimCheck**](https://github.com/mlysy/optimCheck).


## Documentation

Read the documentation online at http://projplot.readthedocs.io/

Alternatively, build the documentation from the ``docs/`` folder

```bash
pip install sphinx
cd docs/
make html
```

## Example

An overview of the package functionality is illustrated with the following example. Let `Q(x) = x^TAx - 2b^Tx` denote a quadratic objective function in `x` is in the d-dimensional real space. If `A` is a positive-definite matrix, then the unique minimum of `Q(x)` is `x̂ =A^{-1}b` (A inverse * b). 

For example, let 
A = [[3,2],
     [2,7]]

and 
b = [1,
     10]

Then we have that the optimal solution is `x̂ = (-0.765, 1.647)`. Now, `projplot` allows us to complete a visual check. As the user of this program, you will need to provide the following information:

* Objective function (`obj_fun`): This can be either a vectorized or non-vectorized function. 
*  Optimal values (`x_opt`): This will be the optimal solution for your function. 
*  Upper and lower bounds for each parameter (`x_lims`): This will provide an initial range of values to observe.
*  Parameter names (`x_names`): These are the names of your parameters, i.e. theta, mu, sigma
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

This package can be used with one function or with intermediary functions for more advanced users. 

### Basic Use Case
This example will walk through how to use the main function `proj_plot()` with a vectorized function.

```python
import projplot as pjp

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

# Obtain plots without vertical x lines
plot_data = pjp.proj_plot(obj_fun, x_opt=theta, x_lims=theta_lims, 
                          x_names=theta_names, n_pts=n_pts, 
						  vectorized=True, plot=True)

# Obtain plots with vertical x lines
plot_data = pjp.proj_plot(obj_fun, x_opt=theta, x_lims=theta_lims, 
                          x_names=theta_names, n_pts=n_pts, 
						  vectorized=True, plot=True, opt_vlines=True)
```

Below, we have the projection plot using this data and objective function. This is without the vertical lines at the optimal value. 
<img src="docs/pages/images/plot1.png" alt = "Plot from vectorized function">

This next plot is including the vertical lines at the optimal value.
<img src="docs/pages/images/plot1b.png" alt = "Plot from vectorized function with vline=True">

### Advanced Use Cases

In these cases, the x-value matrix, projection DataFrame and plotting are done separately. Another added feature is that the user is able to plot vertical lines on the projection plots by providing an array whereas with `proj_plot()` this can only be done at the optimal values. 

#### Vectorized Function
```python
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
x_vals = pjp.proj_xvals(theta, theta_lims, n_pts)

# Obtain y_values and plots
plot_data = pjp.proj_data(obj_fun, x_vals, theta_names, vectorized=True)

# Plot vertical line at optimal values
pjp.proj_plot_show(plot_data, vlines=theta)
```

This would result in the same projection plot as the first example above with the vertical lines.

#### Non-Vectorized Function
```python
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
x_vals = pjp.proj_xvals(theta, theta_lims, n_pts)

# Obtain y_values and plots
plot_data = pjp.proj_data(obj_fun, x_vals, theta_names, vectorized=False)
pjp.proj_plot_show(plot_data)
```

Below, we have the projection plot using this data and objective function. 

<img src="docs/pages/images/plot2.png" alt = "Plot from non-vectorized function">

We can see that the produced plots for the vectorized and non-vectorized function are identical. Vectorized functions have the advantage of running more efficiently; however, are not necessary to utilize this tool.

## FAQ

**Does my function need to be vectorized?** 

No, it does not need to be vectorized in order for you to use this tool. There is a `vectorized` parameter that allows for both vectorized functions and non-vectorized functions. If your function is not vectorized, we will iterate through the x-values to generate the x-value matrix that will be used for the projection plots. If your function is vectorized, this will run more efficiently with generating the projection plots. 

**What is the point of generating the x-value matrix separately?**

The x-value matrix generates the combinations with the varying parameters that we will be inputting into the objective function to visualize the resulting changes in the output. By having this outputted separately, the user is able to view the values that will be inputted prior to plotting and alter it. In the future, an `equalize()` function will be added to fine-tune the scale to be more accurate. An example of what the x-value matrix looks like is given below (based on the example above): 

<img src="docs/pages/images/x_vals.png" alt = "Example of x-vals matrix">

**Can I see the data that is plotted as a DataFrame?**
Yes, if you want to see the data that is being plotted as a DataFrame, you can set `plot=False` in `proj_plot()` and it will return the DataFrame of values that would have been plotted. If we were to assign this to a variable `plot_data` and call it, we would have the following DataFrame outputted (based on the example above):

<img src="docs/pages/images/plot_data.png" alt = "Example of plot_data DataFrame">

**Do I have to include names for each parameter?** 
No, as a default if the list of names is empty, the function will label them x1,x2,...,xp based on p parameters. 

**What is the point of the opt_vlines and vlines parameters?** 
This allows the user to see where the solution for each parameter lies on the plot. For exxample, if the projection plot is given for values between -2 and 2 and was minimized at 0, if we believed the minimum was at -1, we would be able to visually tell that our optimization didn't work since the vertical line would not be at 0. 

With `proj_plot()` you are only able to plot vertical lines at the optimal values using `opt_vlines`. However, for the more advanced users, vertical lines (`vlines`) can be plotted at any values as long as an array is provided that is the length of the parameters for `proj_plot_show()`.


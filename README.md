# projplots

[Under construction]

Developed by Kanika Chopra and Dr. Martin Lysy (2022)

This package is created to assist with testing optimization when building optimizers by providing additional visualizations. If a plot is pinpointed to a certain area (zoomed in) or too generalized (zoomed out), there can be misinterpretations regarding optimality. For example, a graph can look as if it has (has not) reached its optimal values despite it being the opposite. Two examples of plots that are misleading despite not being at the optimal value are given below. Figure 1 shows a plot that is too zoomed in and Figure 2 shows a plot that is too zoomed out.


Figure 1: A misleading plot due to being too zoomed in


Figure 2: A misleading plot due to being too zoomed out

`projplots` provides an additional visual assessment of optimality. A plot is generated for each theta value being optimized. This plot varies the respective theta value while holding the other variables constant. This helps to determine if the specific theta has been optimized based on an upper and lower limit (provided by the user). 

For example, if we were optimizing $$\theta$$ and $$\mu$$, we would have one plot where $$\mu$$ is held constant and $$\theta$$ is varying. This plot would show how the results of the objective function vary based on $$\theta$$. By analysing this plot, we are able to determine if $$\theta$$ has reached its optimal value. An example of this plot can be found in the Examples section. 

## Contents

* `src/proj_plots`: contains the project directory for the proj_plot package. 
* `src/proj_plots/proj.py`: This file contains the functions needed to generate these varying plots. 
    * `proj_xvals()` generates a x-value matrix that has each variation of altering one x-variable, while holding others constaint. The x-values are the thetas that are being optimized. 
    * `proj_plot()` produces a plot for each x value based on a DataFrame containing the varying x value and corresponding calculated y. 
    * `proj_data()`: will take a objective function and the x-value matrix generated and will create a DataFrame with the varying x-value and respective y-value. This will return the DataFrame and also plot the values using `proj_plot`.
* `src/test`: containts a package to test `proj_plots`.

## Examples

An overview of the package functionality is illustrated with the following example. Let 

$$ Q(x) = x^TAx - 2b^Tx $$ 

denote a quadratic objective function in $$x \in \Re^d$$. If $$A_d$$ is a positive-definite matrix, then the unique minimum of $$Q(x)$$ is $$x̂ =A^{-1}b$$. 

For example, let
$$
A = \begin{bmatrix} 
    1 & 2 \\
    4 & 3
    \end{bmatrix}
$$ 
and 
$$ 
b = \begin{bmatrix}
    5 \\
    6
    \end{bmatrix}
$$ 

Then we have that the optimal solution is $$\hat{x} = $$. Now, `projplots` allows us to complete a visual check. As the user of this program, you will need to provide the following information:

* Objective function (`obj_fun`): This can be either a vectorized or non-vectorized function. 
*  Optimal values (`theta`): This will be the optimal solution for your function. 
*  Upper and lower bounds for each theta (`theta_lims`): This will provide an initial range of values to observe.
*  Parameter names (`theta_names`): These are the names of your parameters, i.e. theta, mu, sigma
*  Number of points to plot for each parameter (`n_pts`): This is the number of points that each parameter will be evaluated at for their respective plot. 

#### Vectorized Function
```python
from proj import proj_xvals
from proj import proj_data

# Define function

def obj_fun(x):
    '''
    Params: 
        x: x is a 2x1 vector

    Returns the output of x'Ax - 2b'x
    '''
    return x.dot(A) @ (x) - 2 * b.dot(x)

# Optimal values
theta = np.array([])

# Upper and lower bounds
theta_lims = np.array([[3., 8.], [0., .1], [.5, 2]])

# Parameter names
theta_names = ["mu", "sigma"]

# Number of evaluation points per coordinate
n_pts = 100

# Generate first round of x_values
x_vals = proj_xvals(theta, theta_lims, n_pts)

# Obtain y_values and plots
plot_data = proj_data(obj_fun, x_vals, theta_names, is_vectorized=True)
```

Below, we have the projection plot using this data and objective function. 

#### Non-Vectorized Function
```python
from proj import proj_xvals
from proj import proj_data

# Define function

def obj_fun(x):
    for i in range(len(x)):

# Optimal values
theta = np.array([])

# Upper and lower bounds
theta_lims = np.array([[3., 8.], [0., .1], [.5, 2]])

# Parameter names
theta_names = ["mu", "sigma"]

# Number of evaluation points per coordinate
n_pts = 100

# Generate first round of x_values
x_vals = proj_xvals(theta, theta_lims, n_pts)

# Obtain y_values and plots
plot_data = proj_data(obj_fun, x_vals, theta_names, is_vectorized=False)
```
Below, we have the projection plot using this data and objective function. 

We can see that the produced plots for the vectorized and non-vectorized function are identical. Vectorized functions have the advantage of running more efficiently; however, are not necessary to utilize this tool.

## FAQ

**Does my function need to be vectorized?** 

No, it does not need to be vectorized in order for you to use this tool. There is a `is_vectorized` parameter that allows for both vectorized functions and non-vectorized functions. If your function is not vectorized, we will iterate through the x-values to generate the x-value matrix that will be used for the projection plots. If your function is vectorized, this will run more efficiently with generating the projection plots. 


*This package will have a similar goal to `OptimCheck` in R.*
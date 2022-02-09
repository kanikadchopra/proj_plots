# projplots

[Under construction]

Developed by Kanika Chopra and Dr. Martin Lysy (2022)

This package is created to assist with testing optimization when building optimizers through additional visualizations. If a plot is pinpointed to a certain area (zoomed in) or the opposite (zoomed out), there can be misinterpretations regarding optimality. A graph can look as if it has (has not) reached its optimal values despite it being the opposite. 

`projplots` provides an additional visual assessment of optimality. A plot is generated for each theta value being optimized. This will help to determine if, while holding all other variables constant, this specific theta has been optimized based on the inputted limits. 

For example, if we were optimizing $\theta$ and $\mu$, we would have one plot where $\mu$ is held constant and $\theta$ is varying. This plot would show how the results of the objective function vary based on $\theta$. By analysing this plot, we are able to determine if $\theta$ has reached its optimal value. 

## Contents

* `src/proj_plots`: contains the project directory for the proj_plot package. 
* `src/proj_plots/proj.py`: This file contains the functions needed to generate these varying plots. 
    * `proj_xvals()` generates a x-value matrix that has each variation of altering one x-variable, while holding others constaint. The x-values are the thetas that are being optimized. 
    * `proj_plot()` produces a plot for each x value based on a DataFrame containing the varying x value and corresponding calculated y. 
    * `proj_data()`: will take a objective function and the x-value matrix generated and will create a DataFrame with the varying x-value and respective y-value. This will return the DataFrame and also plot the values using `proj_plot`.
* `src/test`: containts a package to test `proj_plots`.

## How to Use projplots

This is assuming the existence of a function `obj_fun(theta)`.

```python
from proj import proj_xvals
from proj import proj_data

# Set theta values and limits
theta  = np.array([5, 0.5, 1])
theta_lims = np.array([[3., 8.], [0., .1], [.5, 2]])
theta_names = ["mu", "sigma", "tau"]

# Number of evaluation points per coordinate
n_pts = 100

# Generate first round of x_values
x_vals = proj_xvals(theta, theta_lims, n_pts)

# Obtain y_values and plots
plot_data = proj_data(obj_fun, x_vals, theta_names, True)
```

## FAQ

**Does my function need to be vectorized?** 

No, it does not need to be vectorized in order for you to use this tool. There is a `is_vectorized` parameter that allows for both vectorized functions and non-vectorized functions. If your function is not vectorized, we will iterate through the x-values to generate the projection plots. 


*This package will have a similar goal to `OptimCheck` in R.*
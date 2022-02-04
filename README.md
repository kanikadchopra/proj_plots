# projplots

This package is currently under construction.

Developed by Kanika Chopra and Dr. Martin Lysy (2022)

## Examples of How To Use 

This is assuming the existence of a function `obj_fun(theta)`.

```python
# This will be cleaned up so functions are in the same file 
from proj_plots import proj_xvals
from proj_plots import proj_data

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

The goal of this package is to have the same functionality as `OptimCheck` in R. 
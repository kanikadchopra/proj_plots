# **projplot**: Utilities for Creating Projection Plots

**projplot** provides a set of tools to assess whether or not an optimization algorithm has converged to a local optimum.  Its main function does this by visualizing the "projection plots" of the objective function `f(x)` -- that is, by plotting `f` against each coordinate of `x` with the other coordinates fixed at the corresponding elements of the candidate optimal solution `x_opt`.  

This package has a similar goal to the R package [**optimCheck**](https://github.com/mlysy/optimCheck).

## Installation

This package is available on [PyPi](https://pypi.org/project/projplot/) and can be installed as follows:

```bash
pip install projplot
```

## Documentation

Available on [Read the Docs](http://projplot.readthedocs.io/).

## Example

An overview of the package functionality is illustrated with the following example. Let `f(x) = x^TAx - 2b^Tx` denote a quadratic objective function in `x`, which is in the d-dimensional real space. If `A` is a positive-definite `d x d` matrix, then the unique minimum of `f(x)` is `x_opt =A^{-1}b`. 

For example, suppose we have

```python
import numpy as np

A = np.array([[3., 2.],
              [2., 7.]])
b = np.array([1., 10.])
```

Then we have that the optimal solution is `x_opt = (-0.765, 1.647)`. Now, **projplot** allows us to complete a visual check. The following information will need to be provided:

* The objective function (`obj_fun`): This can be either a vectorized or non-vectorized function. 
*  Optimal values (`x_opt`): This will be the optimal solution for your function. 
*  Upper and lower bounds for each parameter (`x_lims`): This will provide an initial range of values to observe.
*  Parameter names (`x_names`): These are the names of your parameters, i.e. theta, mu, sigma
*  The number of points to plot for each parameter (`n_pts`): This is the number of points that each parameter will be evaluated at for their respective plot. 

```python
# Optimal values
x_opt = np.array([-0.765,  1.647])

# Upper and lower bounds for each component of x
x_lims = np.array([[-3., 1], [0, 4]])

# Parameter names
x_names = ["x1", "x2"]

# Number of evaluation points per coordinate
n_pts = 10

import projplot as pjp

def obj_fun(x):
    '''Compute x'Ax - 2b'x.'''
    y = np.dot(np.dot(x.T, A), x) - 2 * np.dot(b, x)
    return y

# Obtain plots with vertical x lines
pjp.proj_plot(obj_fun, x_opt=x_opt, x_lims=x_lims,
              x_names=x_names, n_pts=n_pts,
              opt_vlines=True)
```

This package can be used with one function or with intermediary functions for more advanced users. 

### Basic Use Case

This example will walk through how to use the main function `projplot.proj_plot()`.

```python
import projplot as pjp

def obj_fun(x):
    '''Compute x'Ax - 2b'x.'''
    y = np.dot(np.dot(x.T, A), x) - 2 * np.dot(b, x)
    return y

# Obtain plots without vertical x lines
pjp.proj_plot(obj_fun, x_opt=x_opt, x_lims=x_lims, 
	          x_names=x_names, n_pts=n_pts)

# Obtain plots with vertical x lines
pjp.proj_plot(obj_fun, x_opt=x_opt, x_lims=x_lims, 
              x_names=x_names, n_pts=n_pts, 
              opt_vlines=True)
```

![alt](docs/images/plot_vlines.png)

### Further Reading

See [documentation](http://projplot.readthedocs.io/) for advanced use cases and an FAQ.


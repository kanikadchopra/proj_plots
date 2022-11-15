---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Example

An overview of the package functionality is illustrated with the following example. Let

$$
f(\boldsymbol{x}) = \boldsymbol{x}'\boldsymbol{A}\boldsymbol{x} - 2\boldsymbol{b}'\boldsymbol{x}
$$ 

denote a quadratic objective function in $\boldsymbol{x}$, which is in the $d$-dimensional real space. If $\boldsymbol{A}$ is a positive-definite $d\times d$ matrix, then the unique minimum of $f(\boldsymbol{x})$ is $\boldsymbol{x}_{opt} = \boldsymbol{A}^{-1}\boldsymbol{b}$. 

For example, suppose we have

```{code-cell} ipython3
import numpy as np

A = np.array([[3., 2.],
              [2., 7.]])
b = np.array([1., 10.])
```

Then we have that the optimal solution is $\boldsymbol{x}_{opt} = (-0.765, 1.647)$. Now, **projplot** allows us to complete a visual check. The following information will need to be provided:

- The objective function (`obj_fun`): This can be either a vectorized or non-vectorized function. 
- Optimal values (`x_opt`): This will be the optimal solution for your function. 
- Upper and lower bounds for each parameter (`x_lims`): This will provide an initial range of values to observe.
- Parameter names (`x_names`): These are the names of your parameters in the plots.
- The number of points to plot for each parameter (`n_pts`): This is the number of points that each parameter will be evaluated at for their respective plot. 

## Setup

```{code-cell} ipython3
# Optimal values
x_opt = np.array([-0.765,  1.647])

# Upper and lower bounds for each component of x
x_lims = np.array([[-3., 1], [0, 4]])

# Parameter names
x_names = ["x1", "x2"]

# Number of evaluation points per coordinate
n_pts = 10
```

This package can be used with one function or with intermediary functions for more advanced users. 

## Basic Use Case

This example will walk through how to use the main function `projplot.proj_plot()`.

```{code-cell} ipython3
import projplot as pjp


def obj_fun(x):
    '''Compute x'Ax - 2b'x.'''
    y = np.dot(np.dot(x.T, A), x) - 2 * np.dot(b, x)
    return y


# Obtain plots without vertical x lines
pjp.proj_plot(obj_fun, x_opt=x_opt, x_lims=x_lims,
              x_names=x_names, n_pts=n_pts)
```

```{code-cell} ipython3
# Obtain plots with vertical x lines
pjp.proj_plot(obj_fun, x_opt=x_opt, x_lims=x_lims,
              x_names=x_names, n_pts=n_pts,
              opt_vlines=True)
```

## Advanced Use Cases

In these cases, the calculation of the x-value matrix, projection DataFrame and plotting are done separately. Another added feature is that the user is able to plot vertical lines on the projection plots by providing an array whereas with `projplot.proj_plot()` this can only be done at the optimal values. 

```{code-cell} ipython3
# Generate first round of x_values
x_vals = pjp.proj_xvals(x_opt, x_lims, n_pts)
x_vals
```

```{code-cell} ipython3
# Obtain a DataFrame for plotting
plot_data = pjp.proj_data(obj_fun, x_vals, x_names)
plot_data
```

```{code-cell} ipython3
# Plot vertical line at value specified by vlines
vlines = np.array([-1., 1.5]) # different from x_opt
pjp.proj_plot_show(plot_data, vlines=vlines)
```

### Vectorized Function

In the above, `obj_fun()` can only take a single vector `x` at a time.  Inside `projplot.proj_plot()` (or `projplot.proj_data()`) the function is run through a for-loop on each value of `x`.  Alternatively, `obj_fun()` can be vectorized over each row of `x` by providing the **projplot** functions with the argument `vectorized=True`. 

```{code-cell} ipython3
def obj_fun_vec(x):
    '''
    Vectorized computation of x'Ax - 2b'x.

    Params: 
        x: A nx2 vector.

    Returns:
        The output of x'Ax - 2b'x applied to each row of x.
    '''
    x = x.T
    y = np.diag(x.T.dot(A).dot(x)) - 2 * b.dot(x)
    return y


pjp.proj_plot(obj_fun_vec, x_opt=x_opt, x_lims=x_lims,
              x_names=x_names, n_pts=n_pts,
              vectorized=True,
              opt_vlines=True)
```

We can see that the produced plots for the vectorized and non-vectorized function are identical. Vectorized functions have the advantage of running more efficiently; however, they are not necessary to utilize **projplot**.

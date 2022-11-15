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

# FAQ

**Does my function need to be vectorized?** 

No, it does not need to be vectorized in order for you to use this tool. There is a `vectorized` parameter that allows for both vectorized functions and non-vectorized functions. If your function is not vectorized, we will iterate through the x-values to generate the x-value matrix that will be used for the projection plots. If your function is vectorized, this will run more efficiently with generating the projection plots. 

**What is the point of generating the x-value matrix separately?**

The x-value matrix generates the combinations with the varying parameters that we will be inputting into the objective function to visualize the resulting changes in the output. By having this outputted separately, the user is able to view the values that will be inputted prior to plotting and alter it. In the future, an `equalize()` function will be added to fine-tune the scale to be more accurate. An example of what the x-value matrix looks like is given below (based on the documentation [example](example.md)): 

```{code-cell} ipython3
import numpy as np
import projplot as pjp

# setup
x_opt = np.array([-0.765,  1.647]) # optimal values
x_lims = np.array([[-3., 1], [0, 4]]) # plot limits
n_pts = 10 # number of plotting points

x_vals = pjp.proj_xvals(x_opt, x_lims, n_pts)
x_vals
```

**Can I see the data that is plotted as a DataFrame?**

Yes, if you want to see the data that is being plotted as a `pandas.DataFrame`, you can set `plot=False` in `projplot.proj_plot()` and it will return the DataFrame of values that would have been plotted. If we were to assign this to a variable `plot_data` and call it, we would have the following DataFrame outputted (based on the documentation [example](example.md)):

```{code-cell} ipython3
x_names = ["x1", "x2"] # variable names

# objective function
def obj_fun(x):
    A = np.array([[3., 2.],
                  [2., 7.]])
    b = np.array([1., 10.])
    y = np.dot(np.dot(x.T, A), x) - 2 * np.dot(b, x)
    return y

plot_data = pjp.proj_data(obj_fun, x_vals, x_names)
plot_data
```

**Do I have to include names for each parameter?** 

No, as a default if the list of names is empty, the function will label them `x1`, `x2`, ..., `xd` based on $d$ parameters. 

**What is the point of the `opt_vlines` and `vlines` parameters?** 

This allows the user to see where the solution for each parameter lies on the plot. For exxample, if the projection plot is given for values between -2 and 2 and was minimized at 0, if we believed the minimum was at -1, we would be able to visually tell that our optimization didn't work since the vertical line would not be at 0. 

With `projplot.proj_plot()` you are only able to plot vertical lines at the optimal values using `opt_vlines`. However, for the more advanced users, vertical lines (`vlines`) can be plotted at any values as long as an array is provided that is the length of the parameters for `projplot.proj_plot_show()`.

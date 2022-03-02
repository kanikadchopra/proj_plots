==============================
Frequently Asked Questions
==============================

Does my function need to be vectorized?
========================================

No, it does not need to be vectorized in order for you to use this tool. There is a ``is_vectorized`` parameter that allows for both vectorized functions and non-vectorized functions. If your function is not vectorized, we will iterate through the x-values to generate the x-value matrix that will be used for the projection plots. If your function is vectorized, this will run more efficiently with generating the projection plots. 

What is the point of generating the x-value matrix separately?
================================================================

The x-value matrix generates the combinations with the varying thetas that we will be inputting into the objective function to visualize the resulting changes in the output. By having this outputted separately, the user is able to view the values that will be inputted prior to plotting and alter it. In the future, an ``equalize()`` function will be added to fine-tune the scale to be more accurate. An example of what the x-value matrix looks like is given below (based on the example above): 

.. image:: docs/images/x_vals.png
    :alt: Example of x-vals matrix

Can I see the data that is plotted as a DataFrame?
=====================================================

In the examples above, you'll notice that the output of the ``projdata()`` function is set in the variable ``plot_data``. If we were to call the ``plot_data`` variable, we would have the following DataFrame outputted (based on the example above):

.. image:: docs/images/plot_data.png
    :alt: Example of plot_data DataFrame

*This package will have a similar goal to OptimCheck in R.*


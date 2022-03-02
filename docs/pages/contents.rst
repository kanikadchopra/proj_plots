==============================
Contents
==============================

- ``src/projplot``: contains the project directory for the projplot package. 
- ``src/projplot/proj.py``: This file contains the functions needed to generate these varying plots. 
    * ``projxvals()`` generates a x-value matrix that has each variation of altering one x-variable, while holding others constaint. The x-values are the thetas that are being optimized. 
    * ``generate_plot()`` produces a plot for each x value based on a DataFrame containing the varying x value and corresponding calculated y. 
    * ``projdata()``: will take a objective function and the x-value matrix generated and will create a DataFrame with the varying x-value and respective y-value. This will return the DataFrame and also plot the values using ``generate_plot``.
- ``src/test``: containts a package to test ``projplot``.
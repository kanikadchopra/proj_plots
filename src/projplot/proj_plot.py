import numpy as np 
import pandas as pd
import seaborn as sns

def proj_xvals(x_opt, x_lims, n_pts):
    """
    Args:
        x_opt (NumPy array): An array of parameter values
        x_lims (NumPy array): An array of limits or a 2 x x_opt.shape[0] matrix of lower and upper limits for each parameter
        n_pts (int): The number of points to plot

    Returns:
        x_vals (NumPy array): An array of all possible combinations of the x-values based on the limits (x_lims) and optimal values (x_opt)

    Example: 
        >>> proj_xvals(np.array([1,15]), np.array([[0,2], [10, 20]]), 3)
        [[0, 15], [1, 15], [2, 15], [1, 10], [1, 15], [1, 20]]
    """
    
    x_space = np.linspace(x_lims[:,0], x_lims[:,1], n_pts).T
    n_x = x_lims.shape[0]
    x_vals = np.concatenate([x_opt[None].astype(float)] * n_x * n_pts)

    for i in range(n_x):
        x_vals[i*n_pts:(i+1)*n_pts,i] = x_space[i]

    return x_vals

def proj_plot_show(plot_data, x_vline=False):
    """
    Args:
        plot_data (DataFrame): A DataFrame that contains columns for the calculated y-value, varying x value and the respective x_opt name associated with the varying x
        x_vline (optional Bool): If this parameter is set to True, then a vertical line is plotted at each optimal x. The default is False.
    
    Produces a plot for each unique x_opt using the x and y values in plot_data
    """
            
    grid = sns.relplot(
        data=plot_data, kind="line",
        x="x", y="y", col="x_opt",
        facet_kws=dict(sharex=False, sharey=False))
    
    if x_vline == True:
        n_pts= plot_data.shape[1]
        n_param = np.unique(plot_data.x_opt).shape[0]
        x_temp = np.array([plot_data.loc[(n_pts*i)+1, 'x'] for i in range(n_param)])
    

        for i in range(len(grid.axes.flat)):
            ax = grid.axes.flat[i]
            ax.axvline(x=x_temp[i], color='red')

    return grid

def proj_data(fun, x_vals, x_names=[], vectorized = False):
    """
    Args:
        fun (Python function): The objective function that is being optimized
        x_vals (NumPy array): A matrix of the x_vals, this should be outputted from proj_xvals()
        x_names (optional List): A list of the names respective to varying x-values for plotting
        vectorized (Bool): TRUE if the objective function is vectorized, else FALSE

    Returns:
        plot_df (DataFrame): The y-value in each projection plot appended to the x-values in a DataFrame format that's amenable to plotting
    
    """
    n_x = x_vals.shape[0]
    n_param = x_vals.shape[1]
    n_pts = int(n_x/n_param)

    # If x_names is NONE, default list to ["x1", "x2", ..]
    if x_names is None:
        x_names = ['x' + str(i) for i in range(n_param)]
    
    # Initialize empty y vector
    y_vals = np.zeros(n_x)
    varying_x = np.concatenate([x_vals[i*n_pts:(i+1)*n_pts, i] for i in range(n_param)])
    
    # Function is not vectorized 
    if vectorized == False:
        for i in range(n_x):
            y_vals[i] = fun(x_vals[i])

    # Function is vectorized
    else: 
        y_vals = fun(x_vals)
        
    # Append the y_values to the dataframe
    plot_df = pd.DataFrame(varying_x, y_vals)
    plot_df.reset_index(inplace=True)
    plot_df.columns = ['y', 'x']
    plot_df['x_opt'] = np.repeat(x_names, n_pts)
    
    return plot_df

def proj_plot(fun, x_opt, x_lims, x_names=None, n_pts=100, vectorized=False, plot=True, x_vline=False):
    """
    Args:
        fun (Python function): The objective function that is being optimized
        x_opt (NumPy array): An array of parameter values
        x_lims (NumPy array): An array of limits or a 2 x x_opt.shape[0] matrix of lower and upper limits for each parameter
        x_names (anyof List None): A list of the names respective to varying x-values for plotting
        n_pts (int): The number of points to plot
        vectorized (Bool): TRUE if the objective function is vectorized, else FALSE
        plot (Bool): TRUE if the user wants a plot outputted, else FALSE
        x_vline (optional Bool): If this parameter is set to True, then a vertical line is plotted at each parameter. The default is set to False.


    Returns:
        plot_df (DataFrame): The y-value in each projection plot appended to the x-values in a DataFrame format that's amenable to plotting
        It will also plot the projection plots which results in a plot for each varying x_opt if plot is TRUE. 
    """

    # Get the x-value matrix
    x_vals = proj_xvals(x_opt, x_lims, n_pts)

    n_x = x_vals.shape[0]
    n_param = x_vals.shape[1]
    n_pts = int(n_x/n_param)
    
    # If x_names is NONE, default list to ["x1", "x2", ..]
    if x_names is None:
        x_names = ['x' + str(i) for i in range(n_param)]
        
    # Initialize empty y vector
    y_vals = np.zeros(n_x)

    # Function is not vectorized 
    if vectorized == False:
        for i in range(n_x):
            y_vals[i] = fun(x_vals[i])
    
    # Function is vectorized
    else: 
        y_vals = fun(x_vals)

    # Get the x-values that vary for each parameter 
    varying_x = np.concatenate([x_vals[i*n_pts:(i+1)*n_pts, i] for i in range(n_param)])
    
    # Append the y_values to the dataframe
    plot_df = pd.DataFrame(varying_x, y_vals)
    plot_df.reset_index(inplace=True)
    plot_df.columns = ['y', 'x']
    plot_df['x_opt'] = np.repeat(x_names, n_pts)

    if plot==True:
        proj_plot_show(plot_df, x_vline=x_vline)
    
    return plot_df
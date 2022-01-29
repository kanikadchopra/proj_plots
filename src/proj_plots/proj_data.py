def proj_data(fun, x_vals, theta_names, is_vectorized = False):
    """
    Args:
        fun (Python function): The objective function that is being optimized
        x_vals (NumPy array): A matrix of the x_vals, this should be outputted from proj_xvals()
        theta_names (List): A list of the theta names respective to varying x-values for plotting
        is_vectorized (Bool): TRUE if the objective function is vectorized, else FALSE

    Returns:
        plot_df (DataFrame): The y-value in each projection plot appended to the x-values in a DataFrame format that's amenable to plotting
        It will also plot the projection plots which results in a plot for each varying theta. 
    
    """
    n_x = x_vals.shape[0]
    
    # Temporary solution: Create a DataFrame first
    plot_df = pd.DataFrame(x_vals)

    
    # Initialize empty y vector
    y_vals = np.zeros(n_x)

    # Function is not vectorized 
    if is_vectorized == False:
        for i in range(n_x):
            y_vals[i] = fun(x_vals[i])
    
    # Function is vectorized
    else: 
        y_vals = fun(x_vals, axis=1)

    # Append the y_values to the dataframe
    plot_df = pd.DataFrame(np.unique(pd.DataFrame(x_vals)), y_vals)
    plot_df.reset_index(inplace=True)
    plot_df.columns = ['y', 'x']
    plot_df['theta'] = np.repeat(theta_names, x_vals.shape[0]/x_vals.shape[1])
    
    proj_plot(plot_df)
    
    return plot_df
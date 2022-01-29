def proj_plot(plot_data): 
    """
    Args:
        plot_data (DataFrame): A DataFrame that contains columns for the calculated y-value, varying x value and the respective theta name associated with the varying x
        x_vals (NumPy array): A matrix of the x_vals, this should be outputted from proj_xvals()
        is_vectorized (Bool): TRUE if the objective function is vectorized, else FALSE

    Returns:
        plot_df (DataFrame): The y-value in each projection plot appended to the x-values in a DataFrame format that's amenable to plotting.
    """
    sns.relplot(
    data=plot_data, kind="line",
    x="x", y="y", col="theta",
    facet_kws=dict(sharex=False, sharey=False))
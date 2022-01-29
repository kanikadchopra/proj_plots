import numpy as np 

def proj_xvals(theta, theta_lims, n_pts):
    """
    Args:
        theta (NumPy array): An array of parameter values
        theta_lims (NumPy array): An array of limits or a 2 x theta.shape[0] matrix of lower and upper limits for each parameter
        n_pts (int): The number of points to plot

    proj_xvals()`: Calculate a matrix of x-values (each column in an element of `theta`) such that evaluating `obj_fun()` on each row of `theta` produces the y-values in `proj_data()`.  So if `theta = [1, 15]` and `theta_lims = [[0, 2], [10, 20]]`, and `n_pts = 3`, then this would produce the matrix 

    Example: proj_xvals([1, 15], [[0, 2], [10, 20]], 3) => [[0, 15],
                                                                           [1, 15],
                                                                           [2, 15],
                                                                           [1, 10],
                                                                           [1, 15],
                                                                           [1, 20]]
    """
    
    x_theta = np.linspace(theta_lims[:,0], theta_lims[:,1], n_pts).T
    n_theta = theta_lims.shape[0]
    x_vals = np.empty((n_pts * n_theta, n_theta))

    for i in range(n_theta):
        theta_tmp = np.copy(theta)
        theta_tmp = np.delete(theta_tmp, i, axis=0) 

        tmp_grid = x_vals[i*n_pts:(i+1)*n_pts]
        # Initializes theta values that are changing in the tmp_grid
        tmp_grid[:, i] = x_theta[i]

        # Update the other two columns to be constant values in tmp_grid
        b = np.ones((n_theta), dtype=bool)
        b[i] = False

        tmp_grid[:, b] = np.ones((n_pts, n_theta-1)) * theta_tmp

    x_vals[i*n_pts:(i+1)*n_pts] = tmp_grid
    
    return x_vals
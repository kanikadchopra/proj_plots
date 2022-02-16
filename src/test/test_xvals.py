import unittest 

from projplot import projxvals
from projplot import projdata
from projplot import projplot
import numpy as np

class TestXVals(unittest.TestCase):
    def test_matrix(self):
        """
        Test that the correct x-value matrix is being outputted
        """

        theta = np.array([1, 15])
        theta_lims = np.array([[0,2], [10, 20]])
        n_theta = theta_lims.shape[0]
        n_pts = 3 

        result = proj_xvals(theta, theta_lims, 3)
        correct = np.array([[ 0., 15.], [ 1., 15.], [ 2., 15.],
                            [ 1., 10.], [ 1., 15.], [ 1., 20.]])

        np.testing.assert_array_equal(result, correct)
        #self.assertEqual(result, correct)

    
if __name__ == '__main__':
    unittest.main()

    
                            



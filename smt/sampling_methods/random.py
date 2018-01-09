"""
Author: Dr. John T. Hwang <hwangjt@umich.edu>

This package is distributed under New BSD license.

Random sampling.
"""
from __future__ import division
import numpy as np
from six.moves import range

from smt.sampling_methods.sampling_method import SamplingMethod

class Random(SamplingMethod):

    def _compute(self, n):
        """
        Compute the requested number of sampling points.

        Arguments
        ---------
        n : int
            Number of points requested.

        Returns
        -------
        ndarray[n, nx]
            The sampling locations in the input space.
        """
        xlimits = self.options['xlimits']
        nx = xlimits.shape[0]
        return np.random.rand(n, nx)

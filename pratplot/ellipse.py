import matplotlib.pyplot as plt
import numpy as np

from matplotlib.patches import Ellipse


def plot_cov_ellipse(cov, mu=None, ax=None, **kwargs):
    """Plots a 2-d covariance matrix as an ellipse on a set of axes.

    Parameters
    ----------
    cov : np.ndarray, shape (2, 2)
        The covariance matrix.
    mu : np.ndarray, shape (2,)
        The center of the covariance matrix, if desired.
    ax : matplotlib axis
        The axis on which to plot the covariance ellipse. If None, a new one
        will be created.
    **kwargs : keyword arguments
        Arguments for the ellipse artist.

    Returns
    -------
    ax : matplotlib axis
        The axis on which the ellipse is plotted.
    """
    if ax is None:
        _, ax = plt.subplots(1, 1, figsize=(5, 5))

    if mu is None:
        mu = np.array([0., 0.])

    u, v = np.linalg.eigh(cov)
    u = np.sqrt(u)
    ellipse = Ellipse(
        xy=mu,
        width=u[1],
        height=u[0],
        angle=180. * np.arctan2(v[1, -1], v[0, -1]) / np.pi,
        **kwargs
    )
    ax.scatter(mu[0], mu[1], color=kwargs.get('fc', None))
    ax.add_patch(ellipse)
    return ax

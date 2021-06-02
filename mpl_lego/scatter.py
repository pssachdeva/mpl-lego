def tighten_scatter_plot(ax, lim=[0, 1], **line_kwargs):
    """Tightens scatter plot so that limits on both axes are equal, and
    equalizes aspect ratio.

    Parameters
    ----------
    ax : matplolib.axis
        Axis object.
    lim : list
        The limits of the scatter plot.
    line_kwargs : kwargs
        A dictionary of keyword arguments for the identity line.

    Returns
    -------
    ax : matplotlib.axis
        Axis object, now tightened.
    """
    ax.set_xlim(lim)
    ax.set_ylim(lim)
    ax.set_aspect('equal')
    ax.plot(lim, lim, **line_kwargs)
    return ax

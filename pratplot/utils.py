def append_cax_to_ax(ax, spacing=0.05, width=0.05, which='x'):
    """Appends a colorbar axes to a provided axis.

    Parameters
    ----------
    ax : matplotlib object
        An axis object for which to add a colorbar axis.
    spacing : float
        The spacing, as a fraction of axis width or height, between the colorbar
        axis and the axis.
    width : float
        The width of the colorbar, as a fraction of the axis width or height.
    which : string
        Either 'x' or 'y', denoting whether the colobrbar is vertical or
        horizontal, respectively.

    Returns
    -------
    cax : matplotlib object
        The colorbar axes.
    """
    # Get axis dimensions and figure
    [[x0, y0], [x1, y1]] = ax.get_position().get_points()
    fig = ax.get_figure()

    # Add colorbar axes
    if which == 'x':
        cax = fig.add_axes(
            [x1 + spacing * (x1 - x0),
             y0,
             width * (x1 - x0),
             y1 - y0]
        )
    elif which == 'y':
        cax = fig.add_axes(
            [x1,
             y0 + spacing * (y1 - y0),
             x1 - x0,
             width * (y1 - y0)]
        )
    else:
        raise ValueError('Must specify whether colorbar extends x or y axis.')
    return cax


def append_colorbar_to_axis(
    ax, mappable, spacing=0.05, width=0.05, which='x', **kwargs
):
    """Appends a colorbar to a provided axis, such that the colobar matches the
    dimensions of the axis.

    Can either be appended vertically (extending the x-axis) or horizontally
    (extending the y-axis).

    Parameters
    ----------
    ax : matplotlib object
        An axis object for which to add a colorbar.
    mappable : matplotlib object
        A mappable object for the colobar.
    spacing : float
        The spacing, as a fraction of axis width or height, between the colorbar
        axis and the axis.
    width : float
        The width of the colorbar, as a fraction of the axis width or height.
    which : string
        Either 'x' or 'y', denoting whether the colobrbar is vertical or
        horizontal, respectively.

    Returns
    -------
    cb : matplotlib object
        The colorbar.
    cax : matplotlib object
        The colorbar axes.
    """
    fig = ax.get_figure()
    # Use helper function to construct axes
    cax = append_cax_to_ax(fig, ax, spacing, width)
    # Create colorbar with mappable
    cb = fig.colorbar(mappable, cax=cax, **kwargs)
    return cb, cax

def style_panel_axis(
    ax,
    *,
    facecolor="whitesmoke",
    grid_axis=None,
    grid_linestyle="--",
    grid_alpha=0.7,
    hide_spines=("top", "right"),
    axisbelow=True,
):
    """Apply common panel-style formatting to a matplotlib axis.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axis to style in place.
    facecolor : str or color-like, optional
        Background color for the plotting panel.
    grid_axis : {"x", "y", "both"} or None, optional
        Axis on which to draw grid lines. If None, no grid is added.
    grid_linestyle : str, optional
        Line style for the grid.
    grid_alpha : float, optional
        Transparency for the grid lines.
    hide_spines : iterable of str, optional
        Spine names to hide.
    axisbelow : bool, optional
        Whether ticks and grid lines should be drawn below plot elements.

    Returns
    -------
    ax : matplotlib.axes.Axes
        The styled axis, returned for chaining.
    """
    ax.set_facecolor(facecolor)

    if grid_axis is not None:
        ax.grid(axis=grid_axis, linestyle=grid_linestyle, alpha=grid_alpha)

    ax.set_axisbelow(axisbelow)

    for spine in hide_spines:
        ax.spines[spine].set_visible(False)

    return ax


def append_marginal_axis(ax, spacing=0.05, width=0.05, which='x'):
    """Appends a marginal plot to a provided axis.

    Parameters
    ----------
    ax : matplotlib object
        An axis object for which to add a colorbar axis.
    spacing : float
        The spacing, as a fraction of axis width or height, between the marginal
        axis and the provided axis.
    width : float
        The width of the axis, as a fraction of the axis width or height.
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

    # Add colorbar axes
    fig = ax.get_figure()
    if which == 'x':
        marginal = fig.add_axes(
            [x1 + spacing * (x1 - x0),
             y0,
             width * (x1 - x0),
             y1 - y0])
    elif which == 'y':
        marginal = fig.add_axes(
            [x0,
             y1 + spacing * (y1 - y0),
             x1 - x0,
             width * (y1 - y0)])
    else:
        raise ValueError('Must specify whether colorbar extends x or y axis.')
    return marginal

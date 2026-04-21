from matplotlib.lines import Line2D


def make_marker_legend_handles(
    labels,
    *,
    markers=None,
    colors="black",
    linestyle="None",
    formatter=None,
    **kwargs,
):
    """Create marker-only legend handles from labels.

    Parameters
    ----------
    labels : iterable
        Labels to attach to the legend handles.
    markers : iterable or None, optional
        Marker styles for each handle. If None, all handles use circles.
    colors : str or iterable, optional
        Marker and line colors. If a string is provided, it is reused for all
        labels.
    linestyle : str, optional
        Line style for each handle.
    formatter : callable or None, optional
        Function applied to each label before creating the handle.
    **kwargs
        Additional keyword arguments passed to ``matplotlib.lines.Line2D``.

    Returns
    -------
    handles : list of matplotlib.lines.Line2D
        Legend handles that can be passed to ``ax.legend``.
    """
    if markers is None:
        markers = ["o"] * len(labels)

    if isinstance(colors, str):
        colors = [colors] * len(labels)

    handles = []
    for label, marker, color in zip(labels, markers, colors):
        if formatter is not None:
            label = formatter(label)

        handles.append(
            Line2D(
                [0],
                [0],
                color=color,
                marker=marker,
                linestyle=linestyle,
                label=label,
                **kwargs,
            )
        )

    return handles

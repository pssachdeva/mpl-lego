import numpy as np
import string


def _bold_text(text):
    """Bold text helper function."""
    return r'\textbf{' + text + r'}'


def bold_text(text):
    """Bolds a string or list of strings in LaTeX fashion.

    This function converts the strings to raw strings.

    Parameters
    ----------
    text : str or list
        The text, as a single string, or list of strings.

    Returns
    -------
    bolded : str or list
        The bolded text.
    """
    if isinstance(text, str):
        bolded = _bold_text(text)
    elif isinstance(text, list):
        bolded = [_bold_text(s) for s in text]
    else:
        raise ValueError('Text must be a string or list of strings.')
    return bolded


def apply_subplot_labels(
    axes, labels=None, case='lower', bold=False, x=-0.15, y=1.05, ha='center',
    va='center', size=15, **kwargs
):
    """Applies labels to subplots.

    Parameters
    ----------
    axes : matplotlib.axis.Axis, or list
        The matplotlib axes for which to apply labels.
    labels : list of str, default None
        The subplot labels. If None, an alphabetical list will be used.
    case : str
        The case of the subplot labels. Only used if labels is not provided.
        Options are 'lower' and 'upper'.
    bold : bool
        If True, bolds the labels in LaTeX fashion.
    x : float
        The x-offset of the label, in axis space.
    y : float
        The y-offset of the label, in axis space.
    ha, va : str
        The horizontal and vertical alignments.
    size : int
        The size of the label.

    Returns
    -------
    axes : list
        The subplot axes, now labeled.
    """
    if not isinstance(axes, (list, np.ndarray)):
        axes = [axes]
    elif isinstance(axes, np.ndarray) and axes.ndim > 1:
        axes = axes.ravel()
    n_axes = len(axes)

    # Create and bold labels, if necessary
    if labels is None:
        if case == 'lower':
            labels = list(string.ascii_lowercase)[:n_axes]
        elif case == 'upper':
            labels = list(string.ascii_uppercase)[:n_axes]
    if bold:
        labels = bold_text(labels)
    # Apply label to each axis
    for label, ax in zip(labels, axes):
        ax.text(x=x,
                y=y,
                s=label,
                ha=ha,
                va=va,
                size=size,
                transform=ax.transAxes,
                **kwargs)
    return axes

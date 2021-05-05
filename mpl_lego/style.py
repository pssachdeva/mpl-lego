import matplotlib.pyplot as plt


def use_latex_style():
    """Use a style that uses Computer Modern font and LaTeX for mathtype."""
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "font.sans-serif": ["Computer Modern Roman"]
    })

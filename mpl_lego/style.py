from shutil import which  # modern alternative to find_executable
import matplotlib.pyplot as plt
import warnings



def check_latex_style_on():
    """Checks whether LaTeX style has been turned on."""
    return plt.rcParams.get('text.usetex')


def use_latex_style(check_latex=True):
    """Use a style that uses Computer Modern font and LaTeX for mathtype."""
    if check_latex and which('pdflatex'):
        try:
            plt.rcParams.update({
                "text.usetex": True,
                "font.family": "serif",
                "font.serif": ["Computer Modern Roman"],
            })
        except Exception as e:
            warnings.warn(f"Failed to enable LaTeX style: {e}", RuntimeWarning)
    else:
        warnings.warn("LaTeX not found or check_latex=False. Falling back on default RC parameters.", RuntimeWarning)
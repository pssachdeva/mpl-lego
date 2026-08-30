import matplotlib.pyplot as plt
import pytest

from mpl_lego.scatter import tighten_scatter_plot


@pytest.mark.parametrize(
    ("lim", "expected"),
    [(None, (-2, 4)), ("x", (-2, 4)), ("y", (-3, 5)), ((0, 10), (0, 10))],
)
def test_tighten_scatter_plot_equalizes_limits(lim, expected):
    _, ax = plt.subplots()
    ax.set_xlim(-2, 4)
    ax.set_ylim(-3, 5)

    result = tighten_scatter_plot(ax, lim=lim, identity=False)

    assert result is ax
    assert ax.get_xlim() == pytest.approx(expected)
    assert ax.get_ylim() == pytest.approx(expected)
    assert len(ax.lines) == 0


def test_tighten_scatter_plot_adds_configured_identity_line():
    _, ax = plt.subplots()

    tighten_scatter_plot(ax, lim=(0, 2), color="red", linestyle="--")

    assert ax.lines[0].get_xdata() == pytest.approx([0, 2])
    assert ax.lines[0].get_ydata() == pytest.approx([0, 2])
    assert ax.lines[0].get_color() == "red"
    assert ax.lines[0].get_linestyle() == "--"

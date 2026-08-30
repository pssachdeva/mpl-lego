import matplotlib.pyplot as plt
import pytest
from matplotlib.colors import to_rgba

from mpl_lego.axes import append_marginal_axis, style_panel_axis


def test_style_panel_axis_applies_requested_style():
    _, ax = plt.subplots()

    result = style_panel_axis(
        ax,
        facecolor="linen",
        grid_axis="x",
        hide_spines=("top",),
        axisbelow=True,
    )

    assert result is ax
    assert ax.get_facecolor() == pytest.approx(to_rgba("linen"))
    assert not ax.spines["top"].get_visible()
    assert ax.spines["right"].get_visible()
    assert ax.get_axisbelow() is True
    assert any(line.get_visible() for line in ax.get_xgridlines())


@pytest.mark.parametrize("which", ["x", "y"])
def test_append_marginal_axis_uses_parent_dimensions(which):
    _, ax = plt.subplots()
    parent = ax.get_position()

    marginal = append_marginal_axis(ax, spacing=0.1, width=0.2, which=which)
    position = marginal.get_position()

    if which == "x":
        assert position.x0 == pytest.approx(parent.x1 + 0.1 * parent.width)
        assert position.y0 == pytest.approx(parent.y0)
        assert position.width == pytest.approx(0.2 * parent.width)
        assert position.height == pytest.approx(parent.height)
    else:
        assert position.x0 == pytest.approx(parent.x0)
        assert position.y0 == pytest.approx(parent.y1 + 0.1 * parent.height)
        assert position.width == pytest.approx(parent.width)
        assert position.height == pytest.approx(0.2 * parent.height)


def test_append_marginal_axis_rejects_unknown_axis():
    _, ax = plt.subplots()

    with pytest.raises(ValueError, match="Must specify"):
        append_marginal_axis(ax, which="z")

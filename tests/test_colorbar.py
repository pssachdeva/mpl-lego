import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize

from mpl_lego.colorbar import append_colorbar_to_axis, scale_values_to_cmap


def test_scale_values_to_cmap_spans_colormap_when_minimum_is_zero():
    values = np.array([0.0, 1.0, 2.0])
    colors = scale_values_to_cmap(values, "viridis")
    cmap = plt.get_cmap("viridis")

    assert colors[0] == pytest.approx(cmap(0.0))
    assert colors[-1] == pytest.approx(cmap(1.0))


@pytest.mark.xfail(
    reason="https://github.com/pssachdeva/mpl-lego/issues/1",
    strict=True,
)
def test_scale_values_to_cmap_spans_colormap_for_nonzero_minimum():
    values = np.array([10.0, 15.0, 20.0])
    colors = scale_values_to_cmap(values, "viridis")
    cmap = plt.get_cmap("viridis")

    assert colors[0] == pytest.approx(cmap(0.0))
    assert colors[-1] == pytest.approx(cmap(1.0))


def test_append_colorbar_to_axis_returns_colorbar_and_axis():
    _, ax = plt.subplots()
    mappable = ScalarMappable(norm=Normalize(0, 1), cmap="viridis")

    colorbar, colorbar_axis = append_colorbar_to_axis(ax, mappable)

    assert colorbar.ax is colorbar_axis
    assert colorbar_axis in ax.get_figure().axes

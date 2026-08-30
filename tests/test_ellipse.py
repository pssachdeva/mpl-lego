import matplotlib.pyplot as plt
import numpy as np
import pytest
from matplotlib.patches import Ellipse

from mpl_lego.ellipse import plot_cov_ellipse


def test_plot_cov_ellipse_adds_ellipse_to_existing_axis():
    _, ax = plt.subplots()

    result = plot_cov_ellipse(
        np.array([[4.0, 1.0], [1.0, 2.0]]),
        mu=np.array([2.0, 3.0]),
        ax=ax,
        edgecolor="red",
    )

    assert result is ax
    assert len(ax.patches) == 1
    assert isinstance(ax.patches[0], Ellipse)
    assert ax.patches[0].get_edgecolor() == pytest.approx((1.0, 0.0, 0.0, 1.0))


def test_plot_cov_ellipse_can_include_mean_marker():
    _, ax = plt.subplots()

    plot_cov_ellipse(np.eye(2), mu=np.array([2.0, 3.0]), ax=ax, include_mu=True)

    np.testing.assert_allclose(ax.collections[0].get_offsets(), [[2.0, 3.0]])


@pytest.mark.xfail(
    reason="https://github.com/pssachdeva/mpl-lego/issues/3",
    strict=True,
)
def test_plot_cov_ellipse_can_mark_default_mean():
    ax = plot_cov_ellipse(np.eye(2), include_mu=True)

    np.testing.assert_allclose(ax.collections[0].get_offsets(), [[0.0, 0.0]])

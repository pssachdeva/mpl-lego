import matplotlib.pyplot as plt
import pytest

from mpl_lego.colors import get_default_ccycle, hex_to_rgb


def test_get_default_ccycle_matches_matplotlib_configuration():
    assert get_default_ccycle() == plt.rcParams["axes.prop_cycle"].by_key()["color"]


@pytest.mark.parametrize(
    ("color", "alpha", "expected"),
    [
        ("#ff8000", None, [1.0, 128 / 255, 0.0]),
        ("0000ff", 0.25, [0.0, 0.0, 1.0, 0.25]),
    ],
)
def test_hex_to_rgb(color, alpha, expected):
    assert hex_to_rgb(color, alpha=alpha) == pytest.approx(expected)


def test_hex_to_rgb_rejects_invalid_hex():
    with pytest.raises(ValueError):
        hex_to_rgb("not-a-color")

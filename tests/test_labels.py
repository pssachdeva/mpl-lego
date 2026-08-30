import matplotlib.pyplot as plt
import numpy as np
import pytest

from mpl_lego.labels import (
    add_significance_bracket_inplot,
    add_significance_label,
    apply_subplot_labels,
    bold_text,
    fix_labels_for_tex_style,
)


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("one_label", "one label"),
        (["one_label", "two_labels"], ["one label", "two labels"]),
    ],
)
def test_fix_labels_for_tex_style(text, expected):
    assert fix_labels_for_tex_style(text) == expected


def test_fix_labels_for_tex_style_rejects_other_types():
    with pytest.raises(ValueError, match="string or list"):
        fix_labels_for_tex_style(("a", "b"))


def test_bold_text_warns_and_returns_input_without_latex():
    with (
        plt.rc_context({"text.usetex": False}),
        pytest.warns(RuntimeWarning, match="LaTeX style is not turned on"),
    ):
        assert bold_text("label") == "label"


def test_bold_text_formats_strings_and_arrays_with_latex_enabled():
    with plt.rc_context({"text.usetex": True}):
        assert bold_text("first\nsecond") == "\\textbf{first}\n\\textbf{second}"
        assert bold_text(np.array(["a", "b"])) == ["\\textbf{a}", "\\textbf{b}"]


def test_apply_subplot_labels_flattens_axes_and_uses_uppercase():
    _, axes = plt.subplots(2, 2)

    result = apply_subplot_labels(axes, case="upper")

    assert list(result) == list(axes.ravel())
    assert [axis.texts[0].get_text() for axis in result] == ["A", "B", "C", "D"]


def test_add_significance_label_draws_top_marker_and_label():
    _, ax = plt.subplots()

    result = add_significance_label(ax, (1, 3), label="*", which="top")

    assert result is ax
    assert len(ax.lines) == 3
    assert all(min(line.get_ydata()) > 1 for line in ax.lines)
    assert ax.texts[0].get_text() == "*"


@pytest.mark.parametrize(
    ("which", "coordinate_getter"),
    [
        ("bottom", lambda line: line.get_ydata()),
        ("right", lambda line: line.get_xdata()),
    ],
)
@pytest.mark.xfail(
    reason="https://github.com/pssachdeva/mpl-lego/issues/2",
    strict=True,
)
def test_add_significance_label_uses_requested_lower_or_right_side(
    which, coordinate_getter
):
    _, ax = plt.subplots()

    add_significance_label(ax, (1, 3), which=which)
    outside_coordinates = np.concatenate(
        [np.asarray(coordinate_getter(line)) for line in ax.lines]
    )

    if which == "bottom":
        assert np.max(outside_coordinates) < 0
    else:
        assert np.min(outside_coordinates) > 1


@pytest.mark.parametrize(
    ("direction", "expected_spine", "expected_alignment"),
    [("up", 6.0, "bottom"), ("down", 4.0, "top")],
)
def test_add_significance_bracket_inplot(direction, expected_spine, expected_alignment):
    _, ax = plt.subplots()
    ax.set_ylim(0, 10)

    result = add_significance_bracket_inplot(
        ax,
        1,
        3,
        y=5,
        h=1,
        label="p < .05",
        direction=direction,
        text_offset=0.5,
    )

    assert result is ax
    assert len(ax.lines) == 3
    assert ax.lines[-1].get_ydata() == pytest.approx([expected_spine, expected_spine])
    assert ax.texts[0].get_verticalalignment() == expected_alignment

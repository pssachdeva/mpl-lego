from mpl_lego.legend import make_marker_legend_handles


def test_make_marker_legend_handles_uses_defaults():
    handles = make_marker_legend_handles(["one", "two"])

    assert [handle.get_label() for handle in handles] == ["one", "two"]
    assert [handle.get_marker() for handle in handles] == ["o", "o"]
    assert [handle.get_color() for handle in handles] == ["black", "black"]


def test_make_marker_legend_handles_accepts_styles_and_formatter():
    handles = make_marker_legend_handles(
        ["one", "two"],
        markers=["s", "^"],
        colors=["red", "blue"],
        formatter=str.upper,
        markersize=8,
    )

    assert [handle.get_label() for handle in handles] == ["ONE", "TWO"]
    assert [handle.get_marker() for handle in handles] == ["s", "^"]
    assert [handle.get_color() for handle in handles] == ["red", "blue"]
    assert all(handle.get_markersize() == 8 for handle in handles)

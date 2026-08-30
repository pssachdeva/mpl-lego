import matplotlib.pyplot as plt
import pytest

from mpl_lego import style


def test_check_latex_style_on_reads_matplotlib_configuration():
    with plt.rc_context({"text.usetex": True}):
        assert style.check_latex_style_on() is True


def test_use_latex_style_enables_latex_when_pdflatex_is_available(monkeypatch):
    monkeypatch.setattr(style, "which", lambda executable: "/usr/bin/pdflatex")

    with plt.rc_context({"text.usetex": False, "font.family": ["sans-serif"]}):
        style.use_latex_style()

        assert plt.rcParams["text.usetex"] is True
        assert plt.rcParams["font.family"] == ["serif"]
        assert plt.rcParams["font.serif"] == ["Computer Modern Roman"]


def test_use_latex_style_warns_when_pdflatex_is_unavailable(monkeypatch):
    monkeypatch.setattr(style, "which", lambda executable: None)

    with pytest.warns(RuntimeWarning, match="LaTeX not found"):
        style.use_latex_style()

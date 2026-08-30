# mpl-lego

[![PyPI](https://img.shields.io/pypi/v/mpl-lego)](https://pypi.org/project/mpl-lego/)
[![Python](https://img.shields.io/pypi/pyversions/mpl-lego)](https://pypi.org/project/mpl-lego/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/pssachdeva/mpl-lego/blob/main/LICENSE)

`mpl-lego` is a small collection of reusable utilities for building and
styling [Matplotlib](https://matplotlib.org/) figures. It includes helpers for
subplot labels, covariance ellipses, colorbars, legends, scatter plots, colors,
and consistent axis styling.

## Installation

Install the latest release from PyPI:

```bash
python -m pip install mpl-lego
```

`mpl-lego` supports Python 3.11 and newer and depends on Matplotlib and NumPy.

## Quick start

```python
import matplotlib.pyplot as plt
import numpy as np

from mpl_lego.axes import style_panel_axis
from mpl_lego.labels import apply_subplot_labels
from mpl_lego.scatter import tighten_scatter_plot

rng = np.random.default_rng(42)
observed = rng.normal(size=100)
predicted = observed + rng.normal(scale=0.35, size=100)

fig, ax = plt.subplots(figsize=(5, 5))
ax.scatter(observed, predicted, alpha=0.7)

style_panel_axis(ax, grid_axis="both")
tighten_scatter_plot(ax, color="black", linestyle="--")
apply_subplot_labels(ax, labels=["a"])

ax.set(xlabel="Observed", ylabel="Predicted")
fig.tight_layout()
plt.show()
```

## Utilities

| Module | Helpers |
| --- | --- |
| `mpl_lego.axes` | Style an axis or append a marginal axis. |
| `mpl_lego.colorbar` | Map values to colors and append matched colorbars. |
| `mpl_lego.colors` | Read the active color cycle and convert hex colors. |
| `mpl_lego.ellipse` | Plot a two-dimensional covariance ellipse. |
| `mpl_lego.labels` | Format labels, label subplots, and draw significance brackets. |
| `mpl_lego.legend` | Build marker-based legend handles. |
| `mpl_lego.scatter` | Equalize scatter-plot limits and add an identity line. |
| `mpl_lego.style` | Enable Computer Modern and LaTeX text rendering when available. |

All public functions include NumPy-style docstrings with their parameters and
return values.

## Development

Development uses [uv](https://docs.astral.sh/uv/) for dependency management,
virtual environments, testing, and package builds:

```bash
git clone https://github.com/pssachdeva/mpl-lego.git
cd mpl-lego
uv sync
uv run pytest
uv build
```

`uv sync` creates the project environment from `uv.lock` and installs the
development dependency group automatically.

Three known regressions are tracked in the
[issue tracker](https://github.com/pssachdeva/mpl-lego/issues). Their tests are
marked as expected failures until the corresponding fixes land.

## License

`mpl-lego` is distributed under the
[MIT License](https://github.com/pssachdeva/mpl-lego/blob/main/LICENSE).

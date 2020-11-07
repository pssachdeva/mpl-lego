def append_cax_to_ax(fig, ax, spacing=0.05, width=0.05):
    [[x0, y0], [x1, y1]] = ax.get_position().get_points()
    cax = fig.add_axes([x1 + spacing * (x1 - x0),
                        y0,
                        width * (x1 - x0),
                        y1 - y0])
    return cax


def append_colorbar_to_axis(fig, ax, mappable, spacing=0.05, width=0.05):
    cax = append_cax_to_ax(fig, ax, spacing, width)
    cb = fig.colorbar(mappable, cax=cax)
    return cb, cax

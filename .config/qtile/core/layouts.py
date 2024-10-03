from libqtile import layout
from libqtile.config import Match


# ---- Tiling ---------------------------- #
config = {
    'border_focus': "#23a2a2",
    'border_normal': "#aaa3f2",
    'border_width': 2,
    'margin': 10,
    'single_border_width': 0,
    'single_margin': 20,
}

layouts = [
    layout.MonadTall(
        **config,
        change_ratio=0.02,
        min_ratio=0.30,
        max_ratio=0.70,
    ),

    layout.Max(**config),
]

# ---- Floating -------------------------- #
floating_layout = layout.Floating(
    border_focus="#23a234",
    border_normal="#233aaa",
    border_width=0,
    fullscreen_border_width=0,

    float_rules=[
        *layout.Floating.default_float_rules,
    ],
)

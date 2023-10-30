from libqtile import layout
from libqtile.config import Match

def _get_pywal_colors(path):
    out = []
    with open(path) as f:
        for line in f:
            out.append(line.strip())
    return out

colors = _get_pywal_colors('/home/johannes/.cache/wal/colors')

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

layouts = [
    layout.Columns(border_focus_stack=colors[7],
                   border_width=5,
                   border_normal=colors[0],
                   ),
    layout.MonadTall(margin=8, border_focus='#5294e2',
                     border_width=8, ratio=0.65,
                     border_normal='#2c5380'),
    floating_layout,
    layout.Bsp(),
    layout.Columns(border_focus_stack='#d75f5f'),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]



from functools import partial as _partial

from curtsies import fmtstr

bold = _partial(fmtstr, style='bold')
red = _partial(fmtstr, style='red')
green = _partial(fmtstr, style='green')
yellow = _partial(fmtstr, style='yellow')

on_blue = _partial(fmtstr, style='on_blue')

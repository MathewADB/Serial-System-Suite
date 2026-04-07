from functools import partial

from PyQt6.QtGui import QShortcut, QKeySequence

from core.commands import exit_app

def init_shortcuts(window):
    QShortcut(QKeySequence("Esc"), window).activated.connect(partial(exit_app, window))

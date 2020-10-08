"""Application GUI wrapper to pseudonymise functionality in PyMedPhys
"""
import logging
import os
import subprocess
import sys

from PyQt5 import QtWidgets

# pylint: disable = relative-beyond-top-level
try:
    from . import qtpseudo_controller
except:
    import qtpseudo_controller  # type: ignore[no-redef]


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    qt_pseudo_main_window = QtWidgets.QMainWindow()
    # setting the application icon is an environment dependent thing
    # qt_pseudo_main_window.setWindowIcon()
    ui = qtpseudo_controller.PseudoMainWindow()
    ui.setupUi(qt_pseudo_main_window)
    qt_pseudo_main_window.show()
    sys.exit(app.exec_())

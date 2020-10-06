from PyQt5 import QtCore, QtWidgets

# pylint: disable = relative-beyond-top-level
try:
    from qtpseudo import qtpseudo_controller
except:
    from .qtpseudo import qtpseudo_controller  # type: ignore[no-redef]


import pytest


def test_qtpseudo_labels(qtbot):
    # app = QtWidgets.QApplication([])
    qt_pseudo_main_window = QtWidgets.QMainWindow()
    # setting the application icon is an environment dependent thing
    # qt_pseudo_main_window.setWindowIcon()
    ui = qtpseudo_controller.PseudoMainWindow()
    ui.setupUi(qt_pseudo_main_window)
    qtbot.addWidget(ui)
    assert ui.windowTitle() == ""
    assert ui.rb_input_directory_only.text() == "Input Directory Only"
    assert ui.check_box_disable_gender_keyword.text() == "Ignore PatientSex"
    assert ui.select_input_button.text() == "Select Input"
    assert ui.select_output_button.text() == "Select Output"
    assert ui.label_input_files.text() == "Input Files or Directory"
    assert ui.label_output_directory.text() == "Output Directory"
    assert ui.pseudonymise_button.text() == "Pseudonymise"
    assert not ui.rb_input_directory_only.isChecked()
    assert ui.check_box_disable_gender_keyword.isChecked()
    # app.closeAllWindows()

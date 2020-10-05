"""Slots for qtpseudonymise UI created using QtDesigner
"""
import logging
import os
import subprocess
import sys

from PyQt5 import QtWidgets

# pylint: disable=relative-beyond-top-level
import qtpseudonymise


class PseudoMainWindow(qtpseudonymise.Ui_qtpseudo_main_window, QtWidgets.QMainWindow):
    """Controller for Qt Pseudonymise View/GUI

    Parameters
    ----------
    qtpseudonymise : [type]
        [description]
    QtWidgets : [type]
        [description]
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setupUi(self, qtpseudo_main_window):
        self.main_window = qtpseudo_main_window
        super().setupUi(qtpseudo_main_window)

        self.pseudonymise_button.clicked.connect(self._on_pseudonymised_button_pressed)
        self.select_input_button.clicked.connect(self._on_input_select_button_pressed)
        self.select_output_button.clicked.connect(self._on_output_select_button_pressed)
        self.exit_select.triggered.connect(self._on_exit_select)

    def _on_exit_select(self):
        quit()


    def _on_input_select_button_pressed(self):

        file_dialog = QtWidgets.QFileDialog(
            self.main_window,
            caption="Select files to be pseudonymised",
            # filter="DICOM (*.dcm);;Python files (*.py);;XML files (*.xml)",
        )
        file_mode = 3  # 3 = Existing Files, i.e. multi-select;  2 = Directory
        if self.rb_input_directory_only.isChecked():
            file_mode = 2

        file_dialog.setFileMode(file_mode)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            print(selected_files)
            self.plain_text_edit_input_files.clear()
            self.plain_text_edit_input_files.appendPlainText("\n".join(selected_files))

    def _on_output_select_button_pressed(self):

        file_dialog = QtWidgets.QFileDialog(
            self.main_window,
            caption="Select directory for pseudonymised files",
            # filter="DICOM (*.dcm);;Python files (*.py);;XML files (*.xml)",
        )
        file_mode = 2  # 3 = Existing Files, i.e. multi-select;  2 = Directory
        file_dialog.setFileMode(file_mode)
        if file_dialog.exec_():
            selected_files = file_dialog.selectedFiles()
            print(selected_files)
            self.text_edit_output_directory.clear()
            self.text_edit_output_directory.setPlainText(
                selected_files[0]
            )  # (selected_file)

    def _on_pseudonymised_button_pressed(self):
        input_directory = self.plain_text_edit_input_files.toPlainText()
        input_files = self.plain_text_edit_input_files.toPlainText().splitlines()
        if len(input_files) > 1:
            # multi-select
            logging.debug("multiple files were selected")
        else:
            # single file or directory selection
            if os.path.isdir(input_directory):
                logging.debug("a directory was selected or specified")
            else:
                logging.debug("or a single file was selected")

        output_directory = self.text_edit_output_directory.toPlainText()
        successful_files = list()
        failed_files = list()
        error_messages = list()
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Pseudonymisation Outcome")
        for input_path in input_files:
            anon_file_command = (
                "pymedphys --verbose experimental dicom anonymise --pseudo".split()
                + [input_path]
                + f"-o {output_directory}".split()
            )
            if self.check_box_disable_gender_keyword:
                anon_file_command.append("-k")
                anon_file_command.append("PatientSex")

            print(anon_file_command)

            try:
                subprocess.check_output(anon_file_command)
                successful_files.append(input_path)
            except subprocess.CalledProcessError as e_called_process:
                print(e_called_process)
                failed_files.append(input_path)
                error_messages.append(e_called_process)
        failure_message = ""
        message_text = ""
        if len(failed_files) > 0:
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            failed_files_text = "\n".join(failed_files)
            failure_message = f"Failed to pseudonymise: {failed_files_text}"
            detailed_error_messages = "Check console or log files for further details\n"
            detailed_error_messages += str(error_messages)
            msg.setDetailedText(detailed_error_messages)
            message_text = failure_message + "\n"
        else:
            msg.setIcon(QtWidgets.QMessageBox.Information)

        if len(successful_files) > 0:
            msg.setInformativeText(f"See {output_directory} for results")
            successful_files_text = "\n".join(successful_files)
            message_text += f"Pseudonymisation succeeded for: {successful_files_text}"

        msg.setText(message_text)

        _ = msg.exec_()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    qt_pseudo_main_window = QtWidgets.QMainWindow()
    # setting the application icon is an environment dependent thing
    # qt_pseudo_main_window.setWindowIcon()
    ui = PseudoMainWindow()
    ui.setupUi(qt_pseudo_main_window)
    qt_pseudo_main_window.show()
    sys.exit(app.exec_())

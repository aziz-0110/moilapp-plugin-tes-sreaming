from src.models.model_apps import Model, ModelApps
from src.plugin_interface import PluginInterface
from PyQt6 import QtWidgets
from .ui_main import Ui_Form


class SetupDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

    # get the slot and signal of the result image (rectilinear) so it can be connected and display it continously
    def setup_result_signal(self, slot, signal):
        self.result_slot = slot
        self.result_signal = signal
        self.result_signal.connect(self.result_slot)

    # get the slot and signal of the original image (fisheye) so it can be connected and display it continously
    def setup_original_signal(self, slot, signal):
        self.original_slot = slot
        self.original_signal = signal
        self.original_signal.connect(self.original_slot)

    # Escape Key does not invoke closeEvent (to disconnect the signals and slots), so need to do it manually
    # def keyPressEvent(self, event):
    #     if event.key() == QtCore.Qt.Key.Key_Escape:
    #         self.close()
    #     else:
    #         super().keyPressEvent(event)

    # need to disconnect the signals and slots else RuntimeError: wrapped C/C++ object of type QLabel has been deleted
    # because the QLabel's lifetime will be over when the Setup Dialog is closed but the previous slot and signal will still call it
    def closeEvent(self, event):
        self.result_signal.disconnect(self.result_slot)
        self.original_signal.disconnect(self.original_slot)
        super().closeEvent(event)


class Controller(QtWidgets.QWidget):
    def __init__(self, model: Model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model
        self.set_stylesheet()
        # self.connect_to_button()

    def set_stylesheet(self):
        dialog = SetupDialog()
        # cek modul yg digunakan
        [label.setStyleSheet(self.model.style_label()) for label in self.findChildren(QtWidgets.QLabel)]
        [button.setStyleSheet(self.model.style_pushbutton()) for button in self.findChildren(QtWidgets.QPushButton)]

        self.ui.open.clicked.connect(self.streaming)

    def tutup(self, model_apps : ModelApps):
        # model_apps = ModelApps()
        model_apps.timer.stop()
        model_apps.__image_result = None
        model_apps.image = None
        model_apps.image_resize = None
        
        self.ui.label.setText(" ")
   
        self.ui.open.blockSignals(True)
        self.ui.open.blockSignals(False)
        self.ui.close.blockSignals(True)
        self.ui.close.blockSignals(False)
    
        model_apps.reset_config()
    
        if model_apps.cap is not None:
            try:
                model_apps.cap.close()
            except:
                pass
        model_apps.cap = None


    def streaming(self):
        model_apps = ModelApps()
        model_apps.create_moildev()
        model_apps.create_image_original()
        model_apps.update_file_config()
        source_type, cam_type, media_source, params_name = self.model.select_media_source()
        model_apps.set_media_source(source_type, cam_type, media_source, params_name)

        model_apps.image_result.connect(lambda img: self.update_label_image(img, self.ui.label))

        self.update_label_image(model_apps.image, self.ui.label)

        self.ui.open.clicked.connect(lambda: self.setup_tile(model_apps))
        self.ui.close.clicked.connect(lambda: self.tutup(model_apps))



    def setup_tile(self, model_apps : ModelApps):
        ui_setup = Ui_Form()
        dialog = SetupDialog()
        ui_setup.setupUi(dialog)

        # setup and gracefully close the slots and signals of image_result and signal_image_original from ModelApps
        update_result_label_slot = lambda img: self.update_label_image(img, ui_setup.label, 600, False)
        dialog.setup_result_signal(update_result_label_slot, model_apps.image_result)
        # update_original_label_slot = lambda img: self.update_label_image(img, ui_setup.label_image_original, 320, False)
        # dialog.setup_original_signal(update_original_label_slot, model_apps.signal_image_original)

        # start setup dialog
        dialog.exec()


    def update_label_image(self, image, ui_label, width=600, scale_content=True):
        self.model.show_image_to_label(ui_label, image, width=width, scale_content=scale_content)

class Percobaan(PluginInterface):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.description = "This is a plugins application"

    def set_plugin_widget(self, model):
        self.widget = Controller(model)
        return self.widget

    def set_icon_apps(self):
        return "icon.png"

    def change_stylesheet(self):
        self.widget.set_stylesheet()


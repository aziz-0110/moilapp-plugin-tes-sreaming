from src.plugin_interface import PluginInterface
from src.models.model_apps import Model, ModelApps
from src.controllers.control_anypoint import AnypointConfig
from .ui_main import Ui_Form
from PyQt6 import QtWidgets, QtCore

# class Controller(QtWidgets.QMainWindow):
#     def __init__(self, app: QtWidgets.QApplication, model: Model, model_apps: ModelApps):
#         super().__init__()
#
#         self.grid_manager = GridManager()
#
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#
#         self.model = model
#         self.model_apps = model_apps
#
#         self.model_apps.signal_image_original.connect(self.show_image_on_original_label)
#         self.model_apps.image_result.connect(self.show_image_on_result_label)
#
#         self.ui.open.clicked.connect(self.open_setup_dialog)
#
#         # self.ui.pushButton_viewPanorama.clicked.connect(self.set_panorama_view)
#         # self.ui.pushButton_viewAnypoint1.clicked.connect(lambda: self.set_anypoint_view(1))
#         # self.ui.pushButton_viewAnypoint2.clicked.connect(lambda: self.set_anypoint_view(2))
#         # self.ui.pushButton_viewFisheye.clicked.connect(self.set_fisheye_view)
#
#         self.set_stylesheet()
#
#     def open_setup_dialog(self):
#         dialog = SetupDialog(self.model_apps)
#         dialog.exec_()
#
#     def set_panorama_view(self):
#         self.grid_manager.set_slot(1, "Panorama")
#         self.model_apps.create_panorama_image()
#
#     def set_anypoint_view(self, index: int):
#         self.grid_manager.set_slot(index + 1, f"Anypoint{index}")
#         self.model_apps.create_anypoint_image(index)
#
#     def set_fisheye_view(self):
#         self.grid_manager.set_slot(4, "Fisheye")
#         self.model_apps.create_fisheye_image()
#
#
#     def update_label_image(self, ui_label, image, width: int = 300, scale_content: bool = False):
#         self.model.show_image_to_label(ui_label, image, width = width, scale_content = scale_content)
#
#     def show_image_on_original_label(self, img: np.ndarray):
#         self.update_label_image(self.ui.label_image_original, img)
#
#     def show_image_on_result_label(self, img: np.ndarray):
#         self.update_label_image(self.ui.label_image_result, img)
#
#     def set_stylesheet(self):
#         [label.setStyleSheet(self.model.style_label()) for label in self.findChildren(QtWidgets.QLabel)]
#         [button.setStyleSheet(self.model.style_pushbutton()) for button in self.findChildren(QtWidgets.QPushButton)]
#
#         # self.ui.label_title.setStyleSheet(self.model.style_label())
#         # self.ui.label_image_original.setStyleSheet(self.model.style_label())
#         # self.ui.label_image_result.setStyleSheet(self.model.style_label())
#         # self.ui.pushButton_openSetup.setStyleSheet(self.model.style_pushbutton())
#         # self.ui.pushButton_viewPanorama.setStyleSheet(self.model.style_pushbutton())
#         # self.ui.pushButton_viewAnypoint1.setStyleSheet(self.model.style_pushbutton())
#         # self.ui.pushButton_viewAnypoint2.setStyleSheet(self.model.style_pushbutton())
#         # self.ui.pushButton_viewFisheye.setStyleSheet(self.model.style_pushbutton())


# class Controller(QtWidgets.QWidget):
#     def __init__(self, model: Model):
#         super().__init__()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#         self.model = model
#         self.moildev = None
#         self.model_apps = ModelApps()
#         self.anypoint_config = AnypointConfig(self.ui)
#         self.model_apps.update_file_config()
#         self.set_stylesheet()
# 
#     def set_stylesheet(self):
#         # cek modul yg digunakan
#         [label.setStyleSheet(self.model.style_label()) for label in self.findChildren(QtWidgets.QLabel)]
#         [button.setStyleSheet(self.model.style_pushbutton()) for button in self.findChildren(QtWidgets.QPushButton)]
#         [spinbox.setStyleSheet(self.model.style_spinbox()) for spinbox in self.findChildren(QtWidgets.QSpinBox)]
# 
#         self.ui.open.clicked.connect(self.streaming)
#         self.ui.close.clicked.connect(self.close)
# 
#         # self.ui.doubleSpinBox_aplha.valueChanged.connect(self.tes)
#         # self.ui.doubleSpinBox_beta.valueChanged.connect(self.tes)
# 
#     def streaming(self):
#         # model_apps = ModelApps()
#         s_type, cam_type, m_sou, p_nm = self.model.select_media_source()
#         self.model_apps.set_media_source(s_type, cam_type, m_sou, p_nm)
#         # self.moildev = self.model.connect_to_moildev(p_nm)
#         # self.model_apps.image_result.connect(self.update_label_image)
# 
#         # ui_setup = Ui_Form()
#         dialog = SetupDialog()
#         # ui_setup.setupUi(dialog)
# 
#         update_original_label_slot = lambda img: self.update_label_image(img, self.ui.label_2, 600, False)
#         dialog.setup_original_signal(update_original_label_slot, self.model_apps.signal_image_original)
#         update_result_label_slot = lambda img: self.update_label_image(img, self.ui.label, 600, False)
#         dialog.setup_result_signal(update_result_label_slot, self.model_apps.image_result)
# 
#         update_result_label_slot_1 = lambda img: self.update_label_image(img, self.ui.label_3, 600, False)
#         dialog.setup_result_signal(update_result_label_slot_1, self.model_apps.image_result)
# 
#         # dialog.exec()
#         # mode 1
#         # self.model_apps.state_recent_view = "AnypointView"
#         # self.model_apps.change_anypoint_mode = "mode_1"
#         # self.model_apps.set_draw_polygon = True
#         # self.model_apps.create_maps_anypoint_mode_1()
# 
#         # self.model_apps.alpha_beta.connect(self.alpha_beta_from_coordinate)
#         # self.model_apps.state_rubberband = False # no idea what this is
# 
#         # mode 2
#         self.model_apps.state_recent_view = "AnypointView"
#         self.model_apps.change_anypoint_mode = "mode_2"
#         self.model_apps.set_draw_polygon = False
#         self.model_apps.create_maps_anypoint_mode_2()
# 
#         self.pano(s_type, cam_type, m_sou, p_nm)
#         # self.ui.label_2.mouseMoveEvent = lambda event: self.model_apps.label_original_mouse_move_event(self.ui.label_2, event)
#         # self.ui.label_2.mousePressEvent = lambda event: self.model_apps.label_original_mouse_move_event(self.ui.label_2, event)
#         # self.ui.label_2.leaveEvent = lambda evnet: self.model_apps.label_original_mouse_leave_event()
# 
#         # panorama
#         # self.model_apps.state_recent_view = "PanoramaView"
#         # self.model_apps.change_panorama_mode = "car"
#         # self.model_apps.create_maps_panorama_car()
# 
#         # tes
#         # self.model_apps.state_rubberband = False # no idea what this is
#         # self.model_apps.state_recent_view = "AnypointView"
#         # self.model_apps.change_anypoint_mode = "mode_1"
#         # # self.anypoint_config.showing_config_mode_1()
#         # self.model_apps.set_alpha_beta(-180, 120)
#         # self.model_apps.create_maps_anypoint_mode_1()
#         # self.model_apps.update_file_config()
# 
#         # untuk gambar
#         self.update_label_image(self.model_apps.image)
# 
#     def pano(self, s_type, cam_type, m_sou, p_nm):
#         print('213kjkljlk')
#         model_apps = ModelApps()
#         dialog = SetupDialog()
# 
#         model_apps.set_media_source(s_type, cam_type, m_sou, p_nm)
# 
#         # self.model_apps.image_result.connect(self.update_label_image)
# 
#         update_result_label_slot = lambda img: self.update_label_image(img, self.ui.label_4, 600, False)
#         dialog.setup_result_signal(update_result_label_slot, model_apps.image_result)
# 
#         model_apps.state_recent_view = "PanoramaView"
#         model_apps.change_panorama_mode = "car"
#         model_apps.create_maps_panorama_car()
# 
# 
#     def alpha_beta_from_coordinate(self, alpha_beta):
#         print(alpha_beta)
# 
#     def tes(self):
#         self.model_apps.state_recent_view = "AnypointView"
#         self.model_apps.change_anypoint_mode = "mode_1"
#         alpha = self.ui.doubleSpinBox_aplha.value()
#         beta = self.ui.doubleSpinBox_beta.value()
#         # self.model_apps.image_result = self.moildev.anypoint_mode1(self.model_apps.image_result, alpha, beta, 120)
#         self.model_apps.image_result = self.moildev.anypoint_mode1(self.model_apps.image_result, alpha, beta, 120)
# 
#         # self.model_apps.change_alpha_beta_by_spinbox(alpha=alpha, beta=beta)
#         # self.model_apps.update_file_config()
#         # self.model_apps.create_image_result()
#         self.model_apps.create_maps_anypoint_mode_1()
#         # self.model_apps.image_result.connect(self.update_label_image)
# 
#     def update_label_image(self, image, ui_label, width, scale_content=False):
#         self.model.show_image_to_label(ui_label, image, width, scale_content=scale_content)
# 
#     def mode1(self, img):
#         x_out, y_out = self.moildev.maps_anypoint_mode1(90, 10, 1)
#         self.model.remap_image(self.model_apps.image_result, x_out, y_out)
# 
#         self.model_apps.image_result.connect(self.update_label_image)
# 
#     def close(self):
#         self.ui.label.setText(" ")
#         self.ui.label_2.setText(" ")
#         self.ui.label_3.setText(" ")
#         self.ui.label_4.setText(" ")
#         self.model_apps.__image_result = None
#         self.model_apps.image = None
#         self.model_apps.image_result = None
#         self.model_apps.image_resize = None
#         self.model_apps.reset_config()
#         self.model_apps.cap = None

# # # GPT PROBLEM MODENYA TERTIMPA # # #

# class Controller(QtWidgets.QWidget):
#     def __init__(self, model: Model):
#         super().__init__()
#         self.ui = Ui_Form()
#         self.ui.setupUi(self)
#         self.model = model
#
#         # Create two instances of ModelApps
#         # self.model_apps_panorama = ModelApps()
#         # self.model_apps_anypoint = ModelApps()
#         self.model_apps = [ModelApps(), ModelApps(), ModelApps()]
#
#         self.set_stylesheet()
#         self.setup_ui_connections()
#
#     def set_stylesheet(self):
#         [label.setStyleSheet(self.model.style_label()) for label in self.findChildren(QtWidgets.QLabel)]
#         [button.setStyleSheet(self.model.style_pushbutton()) for button in self.findChildren(QtWidgets.QPushButton)]
#         [spinbox.setStyleSheet(self.model.style_spinbox()) for spinbox in self.findChildren(QtWidgets.QSpinBox)]
#
#     def setup_ui_connections(self):
#         self.ui.open.clicked.connect(self.start_processing)
#         self.ui.close.clicked.connect(self.close_processing)
#
#     def start_processing(self):
#         s_type, cam_type, m_sou, p_nm = self.model.select_media_source()
#         if m_sou is not None:
#             self.model_apps[0].update_file_config()
#             self.model_apps[0].set_media_source(s_type, cam_type, m_sou, p_nm)
#             self.model_apps[0].signal_image_original.connect(lambda img: self.update_label_image(self.ui.label, img, 600, False))
#
#
#             # Setup and start processing for panorama
#             self.setup_model_apps(self.model_apps[1], s_type, cam_type, m_sou, p_nm)
#             self.setup_panorama_view(self.model_apps[1], self.ui.label_2)
#             #
#             # # Setup and start processing for anypoint
#             # self.setup_model_apps(self.model_apps_anypoint, s_type, cam_type, m_sou, p_nm)
#             # self.setup_anypoint_view(self.model_apps_anypoint, self.ui.label_3)
#
#     def setup_model_apps(self, model_apps, s_type, cam_type, m_sou, p_nm):
#         model_apps.update_file_config()
#         model_apps.set_media_source(s_type, cam_type, m_sou, p_nm)
#
#     def setup_panorama_view(self, model_apps, label):
#         model_apps.state_recent_view = "PanoramaView"
#         model_apps.change_panorama_mode = "car"
#         model_apps.create_maps_panorama_car()
#         model_apps.update_file_config()
#
#         model_apps.image_result.connect(lambda img: self.update_label_image(label, img, 600, False))
#
#     def setup_anypoint_view(self, model_apps, label):
#         model_apps.state_recent_view = "AnypointView"
#         model_apps.change_anypoint_mode = "mode_2"
#         model_apps.set_draw_polygon = False
#         model_apps.create_maps_anypoint_mode_2()
#
#         model_apps.image_result.connect(lambda img: self.update_label_image(label, img, 600, False))
#
#     def update_label_image(self, ui_label, image, width, scale_content=False):
#         self.model.show_image_to_label(ui_label, image, width, scale_content=scale_content)
#
#     def close_processing(self):
#         self.ui.label.setText(" ")
#         self.ui.label_2.setText(" ")
#         self.ui.label_3.setText(" ")
#         self.ui.label_4.setText(" ")
#
#         for x in range(3):
#             self.reset_model_apps(self.model_apps[x])
#         # self.reset_model_apps(self.model_apps_panorama)
#         # self.reset_model_apps(self.model_apps_anypoint)
#
#     def reset_model_apps(self, model_apps):
#         model_apps.__image_result = None
#         model_apps.image = None
#         model_apps.image_result = None
#         model_apps.image_resize = None
#         model_apps.reset_config()
#         model_apps.cap = None
#

class Controller(QtWidgets.QWidget):
    def __init__(self, model: Model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model

        # Create instances of ModelApps for each view
        self.model_apps_panorama = ModelApps()
        self.model_apps_anypoint = ModelApps()
        self.model_apps_fisheye = ModelApps()

        self.set_stylesheet()
        self.setup_ui_connections()

    def set_stylesheet(self):
        [label.setStyleSheet(self.model.style_label()) for label in self.findChildren(QtWidgets.QLabel)]
        [button.setStyleSheet(self.model.style_pushbutton()) for button in self.findChildren(QtWidgets.QPushButton)]
        [spinbox.setStyleSheet(self.model.style_spinbox()) for spinbox in self.findChildren(QtWidgets.QSpinBox)]

    def setup_ui_connections(self):
        self.ui.open.clicked.connect(self.start_processing)
        self.ui.close.clicked.connect(self.close_processing)

    def start_processing(self):
        s_type, cam_type, m_sou, p_nm = self.model.select_media_source()
        if m_sou is not None:
            print("Media source selected:", m_sou)

            # Setup and start processing for panorama
            self.setup_model_apps(self.model_apps_panorama, s_type, cam_type, m_sou, p_nm)
            self.setup_panorama_view(self.model_apps_panorama, self.ui.label_2)

            # Setup and start processing for anypoint
            self.setup_model_apps(self.model_apps_anypoint, s_type, cam_type, m_sou, p_nm)
            self.setup_anypoint_view(self.model_apps_anypoint, self.ui.label_3)

            # Setup and start processing for fisheye
            self.setup_model_apps(self.model_apps_fisheye, s_type, cam_type, m_sou, p_nm)
            self.setup_fisheye_view(self.model_apps_fisheye, self.ui.label_4)

    def setup_model_apps(self, model_apps, s_type, cam_type, m_sou, p_nm):
        model_apps.update_file_config()
        model_apps.set_media_source(s_type, cam_type, m_sou, p_nm)
        print(f"ModelApps configured for {model_apps.state_recent_view}")

    def setup_panorama_view(self, model_apps, label):
        model_apps.state_recent_view = "PanoramaView"
        model_apps.change_panorama_mode = "car"
        model_apps.create_maps_panorama_car()
        model_apps.update_file_config()

        model_apps.image_result.connect(lambda img: self.update_label_image(label, img, 600, False))
        print("Panorama view setup complete")

    def setup_anypoint_view(self, model_apps, label):
        model_apps.state_recent_view = "AnypointView"
        model_apps.change_anypoint_mode = "mode_2"
        model_apps.set_draw_polygon = False
        model_apps.create_maps_anypoint_mode_2()

        model_apps.image_result.connect(lambda img: self.update_label_image(label, img, 600, False))
        print("Anypoint view setup complete")

    def setup_fisheye_view(self, model_apps, label):
        # model_apps.state_recent_view = "FisheyeView"
        # model_apps.create_maps_fisheye()
        # model_apps.update_file_config()
        # model_app.sset_media_source(s_type, cam_type, m_sou, p_nm)
        model_apps.signal_image_original.connect(lambda img: self.update_label_image(label, img, 600, False))


        # model_apps.image_result.connect(lambda img: self.update_label_image(label, img, 600, False))
        print("Fisheye view setup complete")

    def update_label_image(self, ui_label, image, width, scale_content=False):
        self.model.show_image_to_label(ui_label, image, width, scale_content=scale_content)
        print(f"Updated label {ui_label.objectName()} with new image")

    def close_processing(self):
        self.ui.label.setText(" ")
        self.ui.label_2.setText(" ")
        self.ui.label_3.setText(" ")
        self.ui.label_4.setText(" ")

        self.reset_model_apps(self.model_apps_panorama)
        self.reset_model_apps(self.model_apps_anypoint)
        self.reset_model_apps(self.model_apps_fisheye)
        print("Processing closed and reset")

    def reset_model_apps(self, model_apps):
        model_apps.__image_result = None
        model_apps.image = None
        model_apps.image_result = None
        model_apps.image_resize = None
        model_apps.reset_config()
        model_apps.cap = None
        print(f"ModelApps {model_apps.state_recent_view} reset")


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

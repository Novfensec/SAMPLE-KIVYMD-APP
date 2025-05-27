from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.utils.set_bars_colors import set_bars_colors


class SampleApp(MDApp):

    def __init__(self, **kwargs) -> None:
        super(SampleApp, self).__init__(**kwargs)
        self.theme_cls.primary_palette = "Darkblue"

    def build(self) -> MDScreen:
        self.appKv="""
MDScreen:
    MDButton:
        style: 'tonal'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press:
            app.apply_styles("Light") if (not app.theme_cls.theme_style == "Light") else app.apply_styles("Dark")

        MDButtonText:
            text: 'Hello, World!'
"""
        AppScreen = Builder.load_string(self.appKv)
        self.apply_styles("Light")
        return AppScreen

    def apply_styles(self, style: str = "Light") -> None:
        self.theme_cls.theme_style = style
        if style == "Light":
            Window.clearcolor = status_color = nav_color = app.theme_cls.surfaceColor
            style = "Dark"
        else:
            Window.clearcolor = status_color = nav_color = app.theme_cls.surfaceColor
            style = "Light"
        self.set_bars_colors(status_color, nav_color, style)

    def set_bars_colors(self, status_color: list[float] = [1.0, 1.0, 1.0, 1.0], nav_color: list[float] = [1.0, 1.0, 1.0, 1.0], style: str = "Dark") -> None:
        set_bars_colors(
            status_color,  # status bar color
            nav_color,  # navigation bar color
            style,  # icons style of status and navigation bar
        )

if __name__ == "__main__":
    app = SampleApp()
    app.run()
    

from libqtile.widget import base


class Notification(base._TextBox):

    def __init__(self, **config):
        super().__init__("", **config)
        self.text = "HOAAALA :)"
        # My widget's initialisation code here

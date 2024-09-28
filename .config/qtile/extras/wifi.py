import iwlib

from libqtile.widget import Wlan


def get_status(interface_name):
    interface = iwlib.get_iwconfig(interface_name)
    if "stats" not in interface:
        return None, None
    quality = interface["stats"]["quality"]
    essid = bytes(interface["ESSID"]).decode()
    return essid, quality


class Wifi(Wlan):
    def __init__(self, **config):
        super().__init__(**config)

    def poll(self):
        try:
            essid, quality = get_status(self.interface)
            disconnected = essid is None
            if disconnected:
                return self.disconnected_message

            return self.format.format(essid=essid, quality=quality, percent=(quality / 100))
        except EnvironmentError:
            return self.format.format(essid="", quality=1, percent=1)
            # return "󰈁"
            # logger.error(
            #     "%s: Probably your wlan device is switched off or "
            #     " otherwise not present in your system.",
            #     self.__class__.__name__,
            # )

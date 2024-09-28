from qtile_extras.widget import UPowerWidget
from libqtile.log_utils import logger


class Battery(UPowerWidget):
    def __init__(self, **config):
        super().__init__(**config)

    def mouse_enter(self, *args, **kwargs):
        self.show_text = True
        self.bar.draw()

    def mouse_leave(self, *args, **kwargs):
        self.show_text = False
        self.bar.draw()

    def draw(self):
        if not self.configured:
            return
        # Remove background
        self.drawer.clear(self.background or self.bar.background)

        # Define an offset for widgets
        offset = self.margin

        # Work out top of battery
        top_margin = (self.bar.height - self.battery_height) / 2

        # Loop over each battery
        for battery in self.batteries:
            # Get battery energy level
            if 'fraction' not in battery or 'percentage' not in battery:
                continue
            percentage = battery.get("fraction",0)
            # Get the appropriate fill colour
            if self.charging and self.fill_charge:
                fill = self.fill_charge
            else:
                # This finds the first value in self_colours which is greater
                # than the current battery level and returns the colour string
                fill = next(x[1] for x in self.colours if percentage <= x[0])

            # Choose border colour
            if (percentage <= self.percentage_critical) and not self.charging:
                border = self.border_critical_colour
            else:
                border = self.borders[self.charging]

            # Draw the border
            self.drawer._rounded_rect(
                offset, top_margin, self.battery_width, self.battery_height, 1
            )

            self.drawer.set_source_rgb(border)
            self.drawer.ctx.stroke()

            # Work out size of bar inside icon
            fill_width = 2 + (self.battery_width - 6) * percentage

            # Draw the filling of the battery
            self.drawer._rounded_rect(
                offset + 2, top_margin +
                2, fill_width, (self.battery_height - 4), 0
            )
            self.drawer.set_source_rgb(fill)
            self.drawer.ctx.fill()

            # Increase offset for next battery
            offset = offset + self.spacing + self.battery_width

            if self.show_text:
                # Generate text based on status and format time-to-full or
                # time-to-empty
                if self.charging:
                    text = self.text_charging.format(**battery)
                else:
                    text = self.text_discharging.format(**battery)

                # Create a text box
                layout = self.drawer.textlayout(
                    text, self.info_foreground, self.font,
                    self.fontsize, None, wrap=False
                )

                # We want to centre this vertically
                y_offset = (self.bar.height - layout.height) / 2

                # Set the layout as wide as the widget so text is centred
                layout.width = self.max_text_length()

                # Draw it
                layout.draw(offset, y_offset)

                # Increase the offset
                offset += layout.width

            # Draw the battery percentage over the battery icon
            battery_percentage_text = "{percentage:.0f}".format(**battery)
            overlayed_layout = self.drawer.textlayout(
                battery_percentage_text, self.foreground, self.font,
                self.fontsize, None, wrap=False
            )
            y_offset = (self.bar.height - overlayed_layout.height) / 2
            overlayed_layout.draw(self.spacing + 5, y_offset)

        # Redraw the bar
        self.drawer.draw(offsetx=self.offset,
                         offsety=self.offsety, width=self.length)

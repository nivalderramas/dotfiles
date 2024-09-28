import colorsys
from libqtile.lazy import lazy


differentiator = '#090909' 

def sort_colors_by_brightness(colors):
    # Convert hexadecimal colors to HSL tuples
    hsl_colors = [colorsys.rgb_to_hls(int(color[1:3], 16)/255.0,
                                      int(color[3:5], 16)/255.0,
                                      int(color[5:7], 16)/255.0)
                  for color in colors]
    # Sort colors based on lightness component
    sorted_colors = [color for _, color in sorted(zip([hsl[1] for hsl in hsl_colors], colors))]

    return sorted_colors

def blend_colors(color1, color2, alpha):
    '''
    Blend thow colors, the alpha represents how much does the second color influences the image
    the higher the alpha, the more the second color will domain the result
        Example usage
        color1 = '#FF0000'  # Red
        color2 = '#0000FF'  # Blue
        alpha = 0.5  # Blending factor
    '''
    # Remove the '#' symbol
    color1 = color1.lstrip('#')
    color2 = color2.lstrip('#')

    # Convert hexadecimal colors to RGB tuples
    r1, g1, b1 = tuple(int(color1[i:i+2], 16) for i in (0, 2, 4))
    r2, g2, b2 = tuple(int(color2[i:i+2], 16) for i in (0, 2, 4))

    # Perform blending for each color component
    blended_r = int(r1 + (r2 - r1) * alpha)
    blended_g = int(g1 + (g2 - g1) * alpha)
    blended_b = int(b1 + (b2 - b1) * alpha)

    # Convert back to hexadecimal representation
    blended_color = '#{:02X}{:02X}{:02X}'.format(blended_r, blended_g, blended_b)

    return blended_color




## Generate Secondary Palette
def secondary_pallete(colors):
    updated_colors = []
    for color in colors:
        result_int = blend_colors(color, differentiator, 0.3)
        updated_colors.append(result_int)
    return updated_colors

colors = []
cache='/home/nivalderramas/.cache/wal/colors'
def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(8):
            colors.append(file.readline().strip())
load_colors(cache)
colors = secondary_pallete(colors)
colors = sort_colors_by_brightness(colors)
lazy.reload()

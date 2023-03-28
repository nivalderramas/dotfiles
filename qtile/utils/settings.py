import json
from utils import dir

directory = f'{dir.get()}/config.json'
settings = {
    'bar': 'decorated',
    'simpleBar': 'simple',
    'browser': 'firefox',
    'colorscheme': 'nord',
    'terminal': {
        'main': '',
        'floating': '',
    },
    'wallpaper': '~/.config/qtile/wallpapers/anime.jpg',
    'wallpaper2': '~/.config/qtile/wallpapers/anime2.png',
}

try:
    with open(directory, 'r') as file:
        config = json.load(file)
except FileNotFoundError:
    with open(directory, 'w') as file:
        file.write(json.dumps(settings, indent=2))
        config = settings.copy()

from flask import Flask

import folium
from folium import plugins

def folim_create(start_coords):
    m = folium.Map(location=start_coords, width=1500, height=600, zoom_start=13)




    # line_to_new_delhi = folium.PolyLine(
    #     [
    #         [46.67959447, 3.33984375],
    #         [46.5588603, 29.53125],
    #         [42.29356419, 51.328125],
    #         [35.74651226, 68.5546875],
    #         [28.65203063, 76.81640625],
    #     ]
    # ).add_to(m)

    line_to_new_delhi = folium.PolyLine(
        [
            [51.5205898, -0.1424225],
            [51.503324, -0.119543],
            [51.5138453, -0.0983506],
            [51.5128019, -0.0834833],
            [51.508929 , -0.128299],
        ]
    ).add_to(m)


    # line_to_hanoi = folium.PolyLine(
    #     [
    #         [28.76765911, 77.60742188],
    #         [27.83907609, 88.72558594],
    #         [25.68113734, 97.3828125],
    #         [21.24842224, 105.77636719],
    #     ]
    # ).add_to(m)


    plugins.PolyLineTextPath(line_to_new_delhi, "To New Delhi", offset=-5).add_to(m)


    # plugins.PolyLineTextPath(line_to_hanoi, "To Hanoi", offset=-5).add_to(m)
    return m


app = Flask(__name__)


@app.route('/')
def index():
    start_coords = (51.5205898, -0.1424225)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map = folim_create(start_coords)
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
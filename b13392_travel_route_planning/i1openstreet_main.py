from flask import Flask

import folium
from folium import plugins

def folim_create(start_coords):
    m = folium.Map(location=start_coords, width='100%', height='70%', zoom_start=14)




    # line_to_new_delhi = folium.PolyLine(
    #     [
    #         [46.67959447, 3.33984375],
    #         [46.5588603, 29.53125],
    #         [42.29356419, 51.328125],
    #         [35.74651226, 68.5546875],
    #         [28.65203063, 76.81640625],
    #     ]
    # ).add_to(m)
    tooltip ='click me to see more'
    ic0 = plugins.BeautifyIcon(border_color='#00ABDC',
                           text_color='#00ABDC',
                           number=0,
                           inner_icon_style='margin-top:0;')
    ic1 = plugins.BeautifyIcon(border_color='#00ABDC',
                           text_color='#00ABDC',
                           number=1,
                           inner_icon_style='margin-top:0;')
    ic2 = plugins.BeautifyIcon(border_color='#00ABDC',
                           text_color='#00ABDC',
                           number=2,
                           inner_icon_style='margin-top:0;')
    # folium.Marker([51.5205898, -0.1424225], popup='ondon Central Hostel',tooltip=tooltip,icon=folium.Icon(color='red')).add_to(m)
    folium.Marker([51.5205898, -0.1424225],popup='ondon Central Hostel',tooltip=tooltip, icon=ic0).add_to(m)
    folium.Marker([51.503324, -0.119543], popup='Coca-Cola London Eye',tooltip=tooltip,icon=ic1).add_to(m)
    folium.Marker([51.5138453, -0.0983506], popup="St. Paul's Cathedral",tooltip=tooltip,icon=ic2).add_to(m)
    folium.Marker([51.5128019, -0.0834833], popup='Leadenhall Market',tooltip=tooltip).add_to(m)
    folium.Marker([51.508929 , -0.128299], popup='The National Gallery',tooltip=tooltip).add_to(m)

    line_to_new_delhi = folium.PolyLine(
        [
            [51.5205898, -0.1424225],
            [51.503324, -0.119543],
            [51.5138453, -0.0983506],
            [51.5128019, -0.0834833],
            [51.508929 , -0.128299],
        ],
        color='red'
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
    start_coords = (51.503324, -0.119543)
    # folium_map = folium.Map(location=start_coords, zoom_start=14)
    folium_map = folim_create(start_coords)
    return folium_map._repr_html_()


if __name__ == '__main__':
    app.run(debug=True)
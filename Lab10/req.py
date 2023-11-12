from flask import Flask, jsonify
import os

app = Flask(__name__)
PORT = int(os.environ.get("PORT", 3000))

info = [
    {"name": "widget1", "color": "blue"},
    {"name": "widget2", "color": "green"},
    {"name": "widget3", "color": "black"},
    {"name": "widgetX", "color": "blue"}
]

@app.route('/info')
def get_info():
    return jsonify(info)

@app.route('/api')
def get_widgets_json():
    widgets_path = os.path.join(os.path.dirname(__file__), 'public', 'widgets.json')

    try:
        with open(widgets_path, 'r') as file:
            widgets_data = file.read()
            return widgets_data
    except FileNotFoundError:
        return 'widgets.json not found', 404
    except Exception as e:
        print(f'Error reading widgets.json: {e}')
        return 'Internal Server Error', 500

if __name__ == '__main__':
    app.run(port=PORT)


from flask import Flask, render_template, send_from_directory
import os
import random

app = Flask(__name__)

@app.route('/')
def index():
    static_folder = os.path.join(app.root_path, 'static')
    image_files = [f for f in os.listdir(static_folder) if f.endswith('.png')]
    random_image = random.choice(image_files)
    return render_template('index.html', random_image = random_image)


@app.route('/static/<path:path>')
def serve_static(path): 
    # Serve static files from the static folder
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    app.run()

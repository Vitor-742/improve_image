from flask import Flask, request, jsonify, send_file
import os
import subprocess
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Ensure the upload directory exists
UPLOAD_FOLDER = '.'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'success': False, 'error': 'No image provided'})
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No image selected'})
    
    if file:
        # Save the uploaded file as input.png
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], 'input.png')
        file.save(input_path)
        
        try:
            # Run the Real-ESRGAN command
            subprocess.run([
                './realesrgan-ncnn-vulkan.exe',
                '-i', 'input.png',
                '-o', 'output.png'
            ], check=True)
            
            return jsonify({'success': True})
        except subprocess.CalledProcessError as e:
            return jsonify({'success': False, 'error': str(e)})
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/output.png')
def get_output():
    return send_file('output.png')

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
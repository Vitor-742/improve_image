from flask import Flask, request, jsonify, send_file
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)

# Ensure the upload directory exists
UPLOAD_FOLDER = '.'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configure Gemini API
#genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

@app.route('/')
def index():
    return send_file('index.html')

@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'success': False, 'error': 'No image provided'})
    
    if 'prompt' not in request.form:
        return jsonify({'success': False, 'error': 'No prompt provided'})
    
    file = request.files['image']
    prompt = request.form['prompt']
    
    if file.filename == '':
        return jsonify({'success': False, 'error': 'No image selected'})
    
    if file:
        try:
            # Read the image content
            content = file.read()
            image = Image.open(BytesIO(content))
            
            # Create Gemini client
            client = genai.Client()
            
            # Prepare the prompt
            text_input = f"Edit this image according to the following description: {prompt}"
            
            # Generate content using Gemini
            response = client.models.generate_content(
                model="gemini-2.0-flash-preview-image-generation",
                contents=[text_input, image],
                config=types.GenerateContentConfig(
                    response_modalities=['TEXT', 'IMAGE']
                )
            )
            
            # Process the response
            if response.candidates and len(response.candidates) > 0:
                for part in response.candidates[0].content.parts:
                    if part.inline_data is not None:
                        # Convert the edited image to base64
                        edited_image = Image.open(BytesIO(part.inline_data.data))
                        buffered = BytesIO()
                        edited_image.save(buffered, format="PNG")
                        edited_image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
                        
                        return jsonify({
                            'success': True,
                            'edited_image': f'data:image/png;base64,{edited_image_base64}'
                        })
            
            return jsonify({
                'success': False,
                'error': 'No edited image in response'
            })
            
        except Exception as e:
            return jsonify({'success': False, 'error': str(e)})

@app.route('/output.png')
def get_output():
    return send_file('output.png')

if __name__ == '__main__':
    app.run(debug=True, port=5000) 
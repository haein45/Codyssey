from flask import Flask, render_template, request
from gtts import gTTS
import io
import base64
from datetime import datetime

app = Flask(__name__)

VALID_LANGS = ['ko', 'en', 'ja', 'es']

def generate_tts(text, lang):
    try:
        tts = gTTS(text=text, lang=lang)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        return base64.b64encode(fp.read()).decode('utf-8')
    except Exception as e:
        print("TTS error:", e)
        return None

def log_input(text, lang):
    with open("input_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] Text: {text}, Lang: {lang}\n")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form.get('input_text', '').strip()
        lang = request.form.get('lang', 'ko')

        if not input_text:
            return render_template('index.html', error="입력값이 비어 있습니다.", audio=None)

        if lang not in VALID_LANGS:
            return render_template('index.html', error="잘못된 언어 코드입니다.", audio=None)

        audio_data = generate_tts(input_text, lang)
        if audio_data:
            log_input(input_text, lang)
            return render_template('index.html', audio=audio_data)
        else:
            return render_template('index.html', error="TTS 변환 실패", audio=None)

    return render_template('index.html', audio=None)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

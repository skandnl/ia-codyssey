from flask import Flask, render_template, request
from gtts import gTTS
import base64
import io
import os
import datetime

app = Flask(__name__)
ALLOWED_LANGS = {'ko', 'en', 'ja', 'es'}

@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    audio = None
    download_url = None

    if request.method == "POST":
        text = request.form.get("input_text", "").strip()
        lang = request.form.get("lang", "ko")

        # 로그 파일 기록
        with open("input_log.txt", "a", encoding="utf-8") as log:
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{now}] text: {text}, lang: {lang}\n")

        # 유효성 검사
        if not text:
            error = "⚠️ 텍스트를 입력해주세요."
        elif lang not in ALLOWED_LANGS:
            error = f"⚠️ 지원하지 않는 언어입니다: {lang}"
        else:
            try:
                tts = gTTS(text=text, lang=lang)
                fp = io.BytesIO()
                tts.write_to_fp(fp)
                fp.seek(0)

                # base64 인코딩
                b64_audio = base64.b64encode(fp.read()).decode("utf-8")
                audio = b64_audio

                # mp3 파일 저장
                filename = "static/output.mp3"
                with open(filename, "wb") as f:
                    f.write(base64.b64decode(b64_audio))

                download_url = "static/output.mp3"

            except Exception as e:
                error = f"❌ 음성 생성 실패: {str(e)}"

    return render_template("index.html", error=error, audio=audio, download_url=download_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

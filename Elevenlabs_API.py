import os
import requests
from pydub import AudioSegment
from pydub.playback import play
import io

api_key = os.getenv("ELEVEN_API_KEY")

# 설정 가능한 변수
output_filename = "output_audio.mp3"

url = "https://api.elevenlabs.io/v1/text-to-speech/9BWtsMINqrJLrRacOk9x"
headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}

# 문장을 입력받습니다.
text = input("텍스트를 입력하세요: ")

# 음성 생성 요청을 보냅니다.
data = {
    "text": text,
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.3,
        "similarity_boost": 1,
        "style": 1,
        "use_speaker_boost": True
    }
}

response = requests.post(url, json=data, headers=headers, stream=True)

if response.status_code == 200:
    audio_content = b""
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            audio_content += chunk

    segment = AudioSegment.from_mp3(io.BytesIO(audio_content))
    segment.export(output_filename, format="mp3")
    print(f"Success! Wrote audio to {output_filename}")

    # 오디오를 재생합니다.
    play(segment)
else:
    print(f"Failed to save file: {response.status_code}")

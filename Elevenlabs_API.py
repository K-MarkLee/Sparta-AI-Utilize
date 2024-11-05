import os
import requests
from pydub import AudioSegment
from pydub.playback import play
import io
import playsound


api_key = os.getenv("ELEVEN_API_KEY")


# 설정 가능한 변수
output_filename = "output_audio.mp3"


url = "https://api.elevenlabs.io/v1/text-to-speech/piTKgcLEGmPE4e6mEKli"
headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}


# 문장을 입력받습니다.
# text = input("텍스트를 입력하세요: ")

text = """
오늘은 무슨 일인 거니?
울었던 얼굴 같은 걸
그가 너의 마음을 아프게 했니?
나에겐 세상 젤 소중한 너인데
자판기 커피를 내밀어
그 속에 감춰온 내 맘을 담아
고마워 오빤 너무 좋은 사람이야
그 한마디에 난 웃을 뿐
혹시 넌 기억하고 있을까?
내 친구 학교 앞에 놀러 왔던 날
우리들 연인 같다 장난쳤을 때
넌 웃었고 난 밤 지새웠지
니가 웃으면 나도 좋아
넌 장난이라 해도
널 기다렸던 날, 널 보고 싶던 밤
내겐 벅찬 행복 가득한데
나는 혼자여도 괜찮아
널 볼 수만 있다면
늘 너의 뒤에서, 늘 널 바라보는
그게 내가 가진 몫인 것만 같아
친구들 지겹다 말하지
늘 같은 노랠 부르는 나에게
하지만 그게 바로 내 마음인 걸
그대 먼 곳만 보네요
혹시 넌 그날 내 맘을 알까?
우리를 아는 친구 모두 모인 밤
술 취한 널 데리러 온 그를 내게
인사시켰던 나의 생일 날
니가 좋으면 나도 좋아
니 옆에 그를 보며
나완 너무 다른, 난 초라해지는
그에게 널 부탁한다는 말 밖에
널 울리는 사람과
위로 밖에 못하는 나
니가 웃으면 나도 좋아
넌 장난이라 해도
널 기다렸던 날, 널 보고 싶던 밤
내겐 벅찬 행복 가득한데
나는 혼자여도 괜찮아
널 볼 수만 있다면 난
늘 너의 뒤에서, 늘 널 바라보는
그게 내가 가진 몫인 것만 같아"""

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
    playsound.playsound(output_filename)
else:
    print(f"Failed to save file: {response.status_code}")

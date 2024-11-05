import os
import requests
from pydub import AudioSegment
from pydub.playback import play
import io
import playsound


api_key = os.getenv("ELEVEN_API_KEY")


# 설정 가능한 변수
output_filename = "output_audio.mp3"


url = "https://api.elevenlabs.io/v1/text-to-speech/t0jbNlBVZ17f02VDIeMI"
headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
}


# 문장을 입력받습니다.
# text = input("텍스트를 입력하세요: ")

text = """
야
너네 자랑하고 싶은 거 있으면
얼마든지 해
난 괜찮어
왜냐면 나는 부럽지가 않어
한 개도 부럽지가 않어
어?
너네 자랑하고 싶은 거 있으면
얼마든지 해
난 괜찮어
왜냐면 나는 부럽지가 않어
전혀 부럽지가 않어
니가 가진 게 많겠니?
내가 가진 게 많겠니?
난 잘 모르겠지만
한 번 우리가 이렇게
한번 머리를 맞대고
생각을 해보자고
너한테 십만원이 있고
나한테 백만원이 있어
그러면 상당히 너는 내가 부럽겠지
짜증나겠지 근데 입장을
한번 바꿔서 우리가 생각을 해보자고
나는 과연 니 덕분에 행복할까?
내가 더 많이 가져서 만족할까?
아니지
세상에는 천만원을 가진 놈도 있지
난 그놈을 부러워하는 거야
짜증나는 거야
누가 더 짜증날까
널까?
날까?
몰라 나는
근데 세상에는 말이야
부러움이란 거를 모르는 놈도 있거든
그게 누구냐면 바로 나야
너네 자랑하고 싶은 거 있으면
얼마든지 해
난 괜찮어
왜냐면 나는 부럽지가 않어
한 개도 부럽지가 않어
어?
너네 자랑하고 싶은 거 있으면
얼마든지 해
난 괜찮어
왜냐면 나는 부럽지가 않어
전혀 부럽지가 않어
전혀
전혀
아 그게 다
부러워서 그러는 거지 뭐
아니 괜히 그러는 게 아니라
그게 다 부러워서 그러는 거야
아 부러우니까 자랑을 하고
자랑을 하니까 부러워지고
부러우니까 자랑을 하고
자랑을 하니까 부러워지고
부러워지고
부러워지고 부러우니까
자랑을 하고 자랑을 하고
자랑을 하고
자.자자.자 자랑을 하고
부부.부부부 부러워지고
부러우니까
자랑을 하고
자랑을 하니까
부러워지고
부러우니까
자랑을 하고
자랑을 하니까
부러워지고
부러우니까
자랑을 하고
자랑을 하니까
부러워지고
부러우니까 자랑을 하고
자랑을 하니까 부러워지고
자랑을 하니까 부러워지고
부러워지고 부러워지고
부러워지고 부러워지고
아주 뭐 너무 부러울 테니까
너네 자랑하고 싶은 거 있으면
얼마든지 해
난 괜찮어
왜냐면 나는 부럽지가 않어
한 개도 부럽지가 않어
어?
너네 자랑하고 싶은 거 있으면
얼마든지 해
난 괜찮어
왜냐면 나는 부럽지가 않어
전혀 부럽지가 않어
어
괜찮어
난 잔다"""

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

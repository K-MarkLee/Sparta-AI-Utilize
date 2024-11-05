from openai import OpenAI
import os

client = OpenAI(api_key = os.getenv("GPT_API_KEY"))

system_message = {
    "role":"system","content":"너는 학교 선생님이야, 나에게 가르침을 줘야해, 수학을 잘 모른다는 것을 가정하고 알려줘야해, 이해하기 쉽게 예제도 넣어주면 졸을거같아"
}

messages = [system_message]

while True:
    user_input = input("사용자 전달:")
    if user_input == 'exit':
        print("여기서 수업을 마치겠습니다!")
        break

    messages.append({"role":"user","content":user_input})
    completion = client.chat.completions.create(
        model = "gpt-4o",
        messages=messages
    )

    reply = completion.choices[0].message.content
    print("대답 :  "+reply)
    messages.append({"role":"assistnat","content":reply})
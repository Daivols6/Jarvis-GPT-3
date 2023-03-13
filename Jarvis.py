import speech_recognition as sr, pyaudio, openai, os

# Инициализация библиотеки OpenAI и установка API ключа
openai.api_key = "YOUR_API_KEY"

# Указание ключевого слова, которое будет активировать скрипт
WAKE_WORD = "джарвис"

# Функция для распознавания голоса с микрофона
def listen_microphone(r):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Говорите...")
        audio_data = r.listen(source, phrase_time_limit=10)

        text = ""
        try:
            # Распознавание голоса с помощью Google Speech Recognition
            text = r.recognize_google(audio_data, language="ru-RU")
            print(f"Распознанный текст: {text}")

        except sr.UnknownValueError:
            print("Google Speech Recognition не смог распознать аудио.")
        except sr.RequestError as e:
            print(f"Ошибка в Google Speech Recognition сервисе; {e}")

    return text.lower()

# Функция для отправки запроса в OpenAI и обработки ответа
def send_request_to_chatgpt(prompt):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}])
    print(completion.choices[0].message.content)
# Создание объекта для распознавания речи
r = sr.Recognizer()
while True:
    text = listen_microphone(r)
    # Если ключевое слово найдено в тексте
    if WAKE_WORD in text:
        prompt = text.replace(WAKE_WORD, "")
        send_request_to_chatgpt(prompt)

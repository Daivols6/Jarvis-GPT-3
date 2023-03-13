# Jarvis-GPT-3
Feel your self like as Tony Stark.


Используются библиотеки SpeechRecognition, pyaudio для распознавания голоса и библиотека OpenAI для интеграции с ChatGPT.
Установите необходимые библиотеки:
pip install SpeechRecognition pyaudio openai
Код слушает микрофон пользователя и ждет ключевое слово "Джарвис", после чего записывает аудио в течение 10 секунд и отправляет текст запроса на сервер OpenAI для ответа модели ChatGPT.

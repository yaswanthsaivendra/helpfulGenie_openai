import io
import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def speech_to_text(file_path):
    """
    converts question from speech to text format
    """
    audio_file = open(file_path, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1", file=audio_file, response_format="text"
    )
    print(transcription)
    return transcription


def question_to_answer(transcription_text):
    """
    replies with answer in text format to question in text format
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant designed to output JSON.",
            },
            {"role": "user", "content": transcription_text},
        ],
    )
    content = response.choices[0].message.content
    return content


def text_to_speech(speech_file_path, content):
    """
    converts answer in text format to speech
    """
    response = client.audio.speech.create(model="tts-1", voice="alloy", input=content)
    with io.BytesIO(response.content) as audio_file:
        audio_file.seek(0)
        with open(speech_file_path, "wb") as f:
            f.write(audio_file.read())

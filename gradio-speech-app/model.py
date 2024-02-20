import gradio as gr
import whisper
from transformers import pipeline


wav2vec_model = pipeline("automatic-speech-recognition", "./model_repo/wav2vec2-base-960h")
whisper_model = whisper.load_model("base")

def speech_to_text(speech):
    text = wav2vec_model(speech)["text"]
    return gr.Textbox(visible=True, value=text, interactive=True, show_copy_button=True)
    

def transcribe_speech(audio_file):
    result = whisper_model.transcribe(audio_file)
    return gr.Textbox(visible=True, value=result["text"], interactive=True, show_copy_button=True)
import os

import gradio as gr

from model import *

from utils import (
    get_theme,
    get_css,
    build_header,
    clear_audio_screen
)


with gr.Blocks(theme=gr.themes.Default()) as transcribe_audio_files:
    with gr.Column():
        gr.Markdown(
            """
            ## Audio Files
            Upload an `mp3/mp4 audio` file.
            """
        )
        audio = gr.Audio(sources="upload", type="filepath")
        with gr.Row():
            submit_button = gr.Button(value="Submit")
            clear_btn = gr.Button(value="Reset")

        output = gr.Textbox(label='Output', visible=False)

        gr.on(
            triggers=[submit_button.click],
            fn=transcribe_speech,
            inputs=audio,
            outputs=output,
        )

        gr.on(
            triggers=[clear_btn.click, audio.clear],
            fn=clear_audio_screen,
            inputs=[audio, output],
            outputs=[audio, output],
        )

        

with gr.Blocks(theme=gr.themes.Default()) as transcribe_microphone:
    with gr.Column():
        gr.Markdown(
            """
            ## Microphone
            Use the `microphone` to record.
            """
        )
        audio = gr.Audio(sources="microphone", type="filepath")
        with gr.Row():
            submit_button = gr.Button(value="Submit")
            clear_btn = gr.Button(value="Reset")
            
        output = gr.Textbox(label='Output', visible=False)

        gr.on(
            triggers=[submit_button.click],
            fn=transcribe_speech,
            inputs=audio,
            outputs=output,
        )

        gr.on(
            triggers=[clear_btn.click, audio.clear],
            fn=clear_audio_screen,
            inputs=[audio, output],
            outputs=[audio, output],
        )


        # examples=[
        #     [os.path.join(os.path.dirname(__file__),"audio/recording1.wav")],
        #     [os.path.join(os.path.dirname(__file__),"audio/cantina.wav")],
        # ],


def get_tabbed_app():
    
    tabbed_app = gr.TabbedInterface(
            interface_list=[transcribe_microphone, transcribe_audio_files], 
            tab_names=["Transcribe Microphone", "Transcribe Audio File"],
            title= "Audio Transcription",
        )
    return tabbed_app



def build_app():

    with gr.Blocks(
        title="Impaired Speech",
        theme=get_theme(),
        css=get_css(),
    ) as app:
        
        build_header()
        get_tabbed_app()

    return app


if __name__ == "__main__":

    # from transformers import pipeline
    # asr = pipeline("automatic-speech-recognition", "./model_repo/wav2vec2-base-960h")
    
    app = build_app()
    app.queue()
    app.launch(
        share=False, 
        server_name="0.0.0.0",
        debug=False, 
        ssl_verify=False,
        allowed_paths=[str(os.getcwd())])
    # (ssl_certfile=None, ssl_keyfile=None)
    # https://discuss.huggingface.co/t/how-to-run-gradio-with-0-0-0-0-and-https/38003

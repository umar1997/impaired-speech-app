import gradio as gr


def get_theme():
    theme = gr.themes.Base().set(
        background_fill_primary="#0d212c",
        button_primary_text_color="#FFFFFF",
        button_primary_background_fill="#7563F7",
        button_secondary_text_color="#FFFFFF",
        button_secondary_background_fill="#7563F7",
        background_fill_secondary="#202326",
        body_text_color="#FFFFFF",
        border_color_primary="#0d212c",
        color_accent_soft="#7563F7",
        input_background_fill="#202326",
        button_secondary_border_color="#7563F7",
        block_border_width="0px",
        block_label_border_width="0px",
    )
    return theme

def get_css():
    block_css = """
    .logos-container {
        display: flex;
        justify-content: space-between;
    }

    .logo-ai-speech, 
    .logo-mbzuai {
        display: inline-block;
    }

    .logo-ai-speech img, 
    .logo-mbzuai img {
        height: 70px;
        width: auto;
    }

    .header-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    }

    .header {
        font-family: 'Nexa', sans-serif;
        color: #FFFFFF;
        margin-top: 20px;
    }

    """
    return block_css



def build_header():
    logo_html = """
    <div class="logos-container">
        <div class="logo-ai-speech">
            <img src="file/files/speech-logo.png" alt="AI-Speech">
        </div>
        <div class="logo-mbzuai">
            <img src="file/files/mbzuai-logo.png" alt="MBZUAI">
        </div>
    </div>
    """
    header_html = """
    <div class="header-container">
        <div class="header">
            <h1 style="font-size: 40px;font-family: 'Helvetica'">Impaired Speech Application</h1>
        </div>
    </div>
    """
    logo_md = gr.Markdown(logo_html, visible=True)
    header_md = gr.Markdown(header_html, visible=True)
    return logo_md, header_md


def clear_audio_screen(audio, output):
    # audio.clear()
    # clear_btn.click(clear, [], [])
    return None, gr.Textbox(label='Output', visible=False)
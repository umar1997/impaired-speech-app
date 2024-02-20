import gradio as gr
     

with gr.Blocks(theme=gr.themes.Default()) as retrieval:
    with gr.Column():
        gr.Markdown(
            """
            ## Retrieval
            """
        )
        input = gr.Textbox(label='Input', show_label=False, placeholder="Describe your problem here")
        output = gr.Textbox(label='Output')

with gr.Blocks(theme=gr.themes.Default()) as ingestion:
    with gr.Column():
        gr.Markdown(
            """
            ## Ingestion
            Upload file(s) here.
            """
        )
        gr.File(file_count="multiple", file_types=['.pdf'])
        send_btn = gr.Button(value="Upload")
        output = gr.Textbox(label='Output', visible=False)


def build_ui():
    logo_md_html = """
    <div>
        <div align="left" class="logo-med42">
            <img src="./files/PDF.png" alt="M42">
        </div>
        <div align="right" class="logo-m42">
            <img src="./files/logo.svg" alt="Med42" >
        </div>
    </div>
    """
    logo_md = gr.Markdown(logo_md_html, visible=True)
    heading = gr.Markdown(
        """
        # PDF42
        """
        )
    return heading, logo_md


def get_tabbed_app():
    tabbed_app = gr.TabbedInterface(
        interface_list=[ingestion, retrieval], 
        tab_names=["Ingestion", "Retrieval"],
        # title= "PDF42",
    )
    return tabbed_app


def build_app():

    # logo_md = build_ui()
    # (tabbed_app) = 

# 29ab50
# 3deb71

    logo_md = build_ui()

    theme = gr.themes.Base().set(
        background_fill_primary="#0d212c",
        button_primary_text_color="#FFFFFF",
        button_primary_background_fill="#29ab50",
        button_secondary_text_color="#FFFFFF",
        button_secondary_background_fill="#29ab50",
        background_fill_secondary="#202326",
        body_text_color="#FFFFFF",
        border_color_primary="#54b550",
        # color_accent_soft="#7563F7",
        # input_background_fill="#e3e637",
        # button_secondary_border_color="#7563F7",
        block_border_width="0px",
        block_label_border_width="0px",
    )

    with gr.Blocks(
        title="PDF42",
        theme=theme
    ) as app:
        
        logo_md
        get_tabbed_app()
    return app
    

if _name_ == "_main_":

    app = build_app()
    app.launch(share=False, server_name="0.0.0.0",debug=False, ssl_verify=False)
    # (ssl_certfile=None, ssl_keyfile=None)
    # https://discuss.huggingface.co/t/how-to-run-gradio-with-0-0-0-0-and-https/38003

# "user_03", "Med42@70b)#"
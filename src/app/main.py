import gradio as gr

from src.app.config import LOGGER_NAME, LOGGER_LEVEL
from src.models.speech_to_text import SpeechToText
from src.remote_api.constants import ASR_MODEL
from src.utils.logger import Logger

transcriber = SpeechToText(model_name=ASR_MODEL)

logger = Logger(name=LOGGER_NAME, level=LOGGER_LEVEL)


def transcribe(audio):
    if audio is not None:
        return transcriber.transcribe(audio)
    return ""


with gr.Blocks() as demo:
    gr.Markdown("# Speech-to-Text Transcription")

    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                sources=["microphone", "upload"],
                type="numpy",
                label="Record or Upload Audio"
            )
        with gr.Column():
            transcript_output = gr.Textbox(label="Transcription")

    transcribe_btn = gr.Button("Transcribe")

    transcribe_btn.click(
        fn=transcribe,
        inputs=[audio_input],
        outputs=[transcript_output]
    )

logger.info("Starting Gradio app")
demo.launch()

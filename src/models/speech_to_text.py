import numpy as np
import torch
from transformers import pipeline

from src.remote_api.constants import ASR_MODEL


class SpeechToText:
    def __init__(self, model_name=ASR_MODEL):
        self.transcriber = pipeline("automatic-speech-recognition", model=model_name)

    def transcribe(self, audio):
        if audio is not None:
            sr, y = audio

            # Convert to mono if stereo
            if y.ndim > 1:
                y = y.mean(axis=1)

            # Ensure y is a numpy array
            if isinstance(y, torch.Tensor):
                y = y.numpy()

            # Convert to float32 and normalize
            y = y.astype(np.float32) / np.iinfo(np.int16).max

            result = self.transcriber({"sampling_rate": sr, "raw": y})
            return result["text"]
        return ""

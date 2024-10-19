from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

from src.remote_api.config import LOGGER_NAME, LOGGER_LEVEL
from src.remote_api.constants import ASR_MODEL, HOST, PORT
from src.utils.logger import Logger

app = FastAPI()

# Initialize logger
logger = Logger(name=LOGGER_NAME, level=LOGGER_LEVEL)

# Load your ASR model
logger.info("Loading ASR model")
transcriber = pipeline("automatic-speech-recognition", model=ASR_MODEL)
logger.info("ASR model loaded successfully")


class AudioData(BaseModel):
    sampling_rate: int
    audio_data: list[float]


@app.post("/transcribe")
async def transcribe_audio(audio: AudioData):
    try:
        # Convert list back to numpy array
        audio_array = np.array(audio.audio_data, dtype=np.float32)

        # Transcribe
        result = transcriber({"sampling_rate": audio.sampling_rate, "raw": audio_array})

        return {"text": result["text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    import uvicorn

    logger.info("Starting FastAPI server")
    uvicorn.run(app, host=HOST, port=PORT)

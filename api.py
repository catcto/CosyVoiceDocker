#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from fastapi import FastAPI, Form
import os
import uuid
from fastapi.responses import StreamingResponse
from cosyvoice.cli.cosyvoice import CosyVoice
from cosyvoice.utils.file_utils import load_wav
import torchaudio
from io import BytesIO

cosyvoice = CosyVoice('pretrained_models/CosyVoice-300M-SFT')
print(cosyvoice.list_avaliable_spks())
app = FastAPI()

# Text to Speech (TTS) API
@app.post("/v1/tts")
async def tts(
    text: str = Form(None),
    spk: str = Form("中文女"),
):
    audio_buffer = BytesIO()
    for output in cosyvoice.inference_sft(text, spk, stream=False):
        torchaudio.save(audio_buffer, output['tts_speech'], 22050, format="wav")
    audio_buffer.seek(0)

    return StreamingResponse(audio_buffer, media_type="audio/wav", headers={"Content-Disposition": "attachment; filename=output.wav"})

if __name__ == "__main__":
    api_port = os.getenv("API_PORT", 8080)
    api_host = os.getenv("API_HOST", "127.0.0.1")
    import uvicorn
    uvicorn.run(app, host=api_host, port=int(api_port))

# CosyVoiceDocker

This repository provides a Docker image for [CosyVoice](https://github.com/FunAudioLLM/CosyVoice), enabling you to deploy the CosyVoice ASR service within a Docker container.

## Usage

To run this Docker container, you’ll need a machine with NVIDIA GPU support and the NVIDIA Container Toolkit installed. For detailed installation steps, please refer to the [NVIDIA Container Toolkit](https://notes.xiaowu.ai/%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0/AI/NVIDIA#%E5%AE%89%E8%A3%85+NVIDIA+Container+Toolkit) guide.

### Build the Docker image

```shell
$ docker build -t cosyvoice .
```

### Using docker command

```shell
$ docker run -d --name cosyvoice_server -p 8080:8080 \
         --runtime=nvidia \
         -e NVIDIA_DRIVER_CAPABILITIES=all \
         -e NVIDIA_VISIBLE_DEVICES=all \
         cosyvoice
```

### Using docker compose

1. Create a `docker-compose.yml` file:
```yaml
services:
  cosyvoice_server:
    image: cosyvoice
    container_name: cosyvoice_server
    ports:
      - "8080:8080"
    restart: always
    runtime: nvidia
    environment:
      NVIDIA_DRIVER_CAPABILITIES: all
      NVIDIA_VISIBLE_DEVICES: all
```
2. Start the container:
```shell
$ docker compose up -d
```

## Testing

To test the API, use `curl`:

```shell
curl -X POST \
  "http://127.0.0.1:8080/v1/tts" \
  -F "text=你好，欢迎使用语音合成服务" \
  -F "spk=中文女" \
  --output output.wav
```
FROM continuumio/miniconda3

WORKDIR /app
COPY . .
RUN apt-get update && apt-get install libgl1-mesa-glx -y

RUN conda install python=3.10
RUN python -m pip install -r requirements.txt

EXPOSE 7860
ENV GRADIO_SERVER_NAME="0.0.0.0"

CMD ["python", "app.py"]

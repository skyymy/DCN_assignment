FROM python:3.5

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g nyu nyu

WORKDIR /app

USER nyu 

ENV PYTHONBUFFERED=0

COPY --chown=nyu:nyu . .

CMD ["python", "./server.py"]



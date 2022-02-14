FROM python:3.5

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g nyu nyu

# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ \
        &&pip install Flask pytz

USER nyu

COPY --chown=nyu:nyu . .

CMD [ "python", "./run.py" ]

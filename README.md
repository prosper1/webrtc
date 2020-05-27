**Video conference with webrtc**

demostrates django-channels as a signaling server

**Requirements**
-python 3
-postgresql if you working offline.
-redis, more info https://redislabs.com/get-started-with-redis/

**Installation**
virtualenv [Your virtual env name ]

activate your your environment by:

linux - source [Your env Name]/bin/activate

windows - [Your env Name]/Scripts/activate

--install requirements.--

pip install -r requirements.txt

**Run the Server**

python manage.py runserver 8000

**Features**

creates room for video conferencing.

[CHANGELOG]: ./CHANGELOG.md
[version-badge]: https://img.shields.io/badge/version-0.5.1-blue.svg

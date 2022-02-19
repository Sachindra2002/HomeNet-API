import base64
import json

from flask import Flask, request, Response, jsonify, make_response
import os
import tensorflow as tf
import tensorflow_io as tf_io
from werkzeug.utils import secure_filename
import firebase_admin
from firebase_admin import credentials, messaging
import random
import config.config as mongo_setup
from models.user import *
from mongoengine import *
from datetime import datetime

mongo_setup.global_init()

app = Flask(__name__)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

tokens = ["e2XEzeIoTh-SWA2O9GiAVc"
          ":APA91bFNjXJt432d1VWVFIcXktm_WLWWGzi2ka2iLY5GfxBQfJfSIKtpJV1JixcygrhimXqJy_l4XfQCAMUDcuRqEMMUF9QAolAhaPUOFcQSeW3KJ9VRiwg51aA7hxWywaD5NPK1gZfM"]

saved_model_path = 'audio_recognition'
reloaded_model = tf.saved_model.load(saved_model_path)

my_classes = ['dog', 'crying_baby', 'glass_breaking', 'door_wood_knock']


@tf.function
def load_wav_16k_mono(filename):
    """ Load a WAV file, convert it to a float tensor, resample to 16 kHz single-channel audio. """
    file_contents = tf.io.read_file(filename)
    wav, sample_rate = tf.audio.decode_wav(
        file_contents,
        desired_channels=1)
    wav = tf.squeeze(wav, axis=-1)
    sample_rate = tf.cast(sample_rate, dtype=tf.int64)
    wav = tf_io.audio.resample(wav, rate_in=sample_rate, rate_out=16000)
    return wav


def send_notification(title, msg, registration_token, dataObject=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )

    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the audio file from the POST request
        print("POST METHOD CALLED")
        f = request.files['file']

        # Save the WAV file from the POST request
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, 'uploads',
                                 secure_filename(str(random.random()) + ".wav"))
        f.save(file_path)

        print("FILE SAVED - PROCEEDING TO PREDICTION")
        print("PREDICTING...")

        waveform = load_wav_16k_mono(file_path)

        print(f'WAVEFORM VALUES -  + {waveform}')

        reloaded_results = reloaded_model(waveform)
        your_top_class = tf.argmax(reloaded_results)
        your_inferred_class = my_classes[your_top_class]

        print("PREDICTED")
        print("PREDICTED RESULT - " + your_inferred_class)

        if your_inferred_class == "dog":
            send_notification("Sound Detected!", "A dog had been heard barking", tokens)
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            History(
                sound="Dog Bark",
                time=current_time
            ).save()

        elif your_inferred_class == "crying_baby":
            send_notification("Sound Detected!", "A baby has been heard crying", tokens)
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            History(
                sound="Baby Crying",
                time=current_time
            ).save()

        elif your_inferred_class == "glass_breaking":
            send_notification("Breaking of glass sound detected!", "Proceed with caution", tokens)
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            History(
                sound="Glass Breaking",
                time=current_time
            ).save()

        elif your_inferred_class == "door_wood_knock":
            send_notification("Sound Detected!", "Someone is heard knocking the door", tokens)
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            History(
                sound="Door Knocking",
                time=current_time
            ).save()

        return jsonify(content=your_inferred_class)


@app.route('/api/register-user', methods=['POST'])
def register_user():
    if request.method == 'POST':
        email = request.json['email']
        firstname = request.json['firstname']
        lastname = request.json['lastname']
        telephone = request.json['telephone']
        password = request.json['password'].encode("utf-8")

        try:
            user = User(
                email=email,
                firstname=firstname,
                lastname=lastname,
                telephone=telephone,
                password=base64.b64encode(password)
            ).save()

            print(user.json())

            return make_response(user.json(), 200)

        except NotUniqueError:
            return make_response(json.dumps('Email already in use'), 400)


@app.route('/api/auth/login', methods=['POST'])
def login():
    if request.method == 'POST':
        email = request.json['email']
        password = request.json['password'].encode("utf-8")

        user = User.objects(email=email).first()
        print(user)
        if user is None:
            return make_response("User not found", 400)

        if user:
            print(user)
            decoded_password = base64.b64decode(user.password)
            if password == decoded_password:
                return jsonify("success"), 200
            else:
                return make_response("error", 400)


@app.route('/api/history', methods=['GET'])
def history():
    if request.method == 'GET':
        print("get")
        history_list = History.objects().to_json()
        return make_response(history_list, 200)

    if __name__ == '__main__':
        app.run()

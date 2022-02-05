import random

from flask import Flask, request, jsonify, make_response
import os
import tensorflow as tf
import tensorflow_io as tf_io
from werkzeug.utils import secure_filename
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, messaging
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/home_net'
mongo = PyMongo(app)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

tokens = ["d5rMjWX9SVicWEllSU2wrP:APA91bHuJhJH9d_gQjnp_MYLGjSnaXK1WWo45f3vyzPDamX2jcA1lqhXPixrkfvXO1CqDsvStaTDc57XvU8"
          "-kW5MOTogPe_XZ_D5StDfv8Lo2q00x4mr48obuks4jKlGFljkUJfIQcn9"]

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
        elif your_inferred_class == "crying_baby":
            send_notification("Sound Detected!", "A baby has been heard crying", tokens)
        elif your_inferred_class == "glass_breaking":
            send_notification("Breaking of glass sound detected!", "Proceed with caution", tokens)
        elif your_inferred_class == "door_wood_knock":
            send_notification("Sound Detected!", "Someone is heard knocking the door", tokens)

        return jsonify(content=your_inferred_class)


@app.route('/register-user', methods=['POST'])
def register_user():
    current_collection = mongo.db.users
    email = request.json['email']
    firstname = request.json['firstName']
    lastname = request.json['lastName']
    telephone = request.json['telephone']

    user = current_collection.insert(
        {'email': email, 'firstname': firstname, 'lastname': lastname, 'telephone': telephone})
    return make_response(jsonify(user), 200)


if __name__ == '__main__':
    app.run()

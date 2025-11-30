import librosa
from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/audio-analysis', methods=['GET'])
def get_data():
  try:
    data = request.json
    file_path = data.get('file_path')
    print("got file")
    y, sr = librosa.load(file_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    print("got bpm")
    duration = librosa.get_duration(path=file_path)
    print("got duration")
    response = {
              "status": "success",
              "bpm": "{:.2f}".format(tempo[0]),
              "duration": "{:.2f}".format(duration)
          }
    return jsonify(response)
  except Exception as e:
    return {
        "status": "error",
        "message": str(e)
    }, 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
import requests

def main():
  try:
    file_path = "example.mp3"
    response = requests.get(
              "http://localhost:5002/audio-analysis",
              json={"file_path": file_path}
          )
    result = response.json()
    print("Response recieved")
    print(f"BPM: {result['bpm']}")
    print(f"Duration: {result['duration']}")
  except requests.exceptions.ConnectionError:
    print("Can't connect to microservice")
  except Exception as e:
      print(f"Test failed with error: {e}")

if __name__ == "__main__":
        main()
# audio-analysis-microservice

## How to request data
Send a GET request to the microservice containing a json object with the filename of your desired file

```
requests.get(
              "http://localhost:5002/audio-analysis",
              json={"file_path": file_path}
          )
```

## How to request data
The microservice will respond with a json object containing the data

```
{
  "status": "success",
  "bpm": "107.67",
  "duration": "267.24"
}
```
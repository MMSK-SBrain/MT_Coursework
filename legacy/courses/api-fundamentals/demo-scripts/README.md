# Demo Scripts for API Fundamentals Workshop

This folder contains all demonstration scripts for use during the workshop.

## Setup Requirements

```bash
# Install required packages
pip install requests fastapi uvicorn
```

## Scripts Overview

### Consuming APIs (Sessions 2-3)

| Script | Description | Usage |
|--------|-------------|-------|
| `01_simple_get.py` | Basic GET request | `python 01_simple_get.py` |
| `02_parsed_weather.py` | JSON parsing demo | `python 02_parsed_weather.py` |
| `03_interactive_weather.py` | Complete weather app | `python 03_interactive_weather.py` |

### HTTP Methods Theory (Session 1)

| Script | Description | Usage |
|--------|-------------|-------|
| `04_http_methods_demo.py` | All 4 methods compared | `python 04_http_methods_demo.py` |
| `05_post_example.py` | POST in detail | `python 05_post_example.py` |
| `06_put_example.py` | PUT in detail | `python 06_put_example.py` |

### FastAPI Demos (Session 5 - Showcase)

| Script | Description | Usage |
|--------|-------------|-------|
| `07_fastapi_hello.py` | Hello World API | `uvicorn 07_fastapi_hello:app --reload` |
| `08_fastapi_crud.py` | Full CRUD API | `uvicorn 08_fastapi_crud:app --reload` |
| `09_fastapi_weather_api.py` | Weather API wrapper | `uvicorn 09_fastapi_weather_api:app --reload` |

## API Keys

Several scripts require an OpenWeatherMap API key:
1. Sign up at https://openweathermap.org/api
2. Get your free API key
3. Replace `YOUR_API_KEY_HERE` in the scripts

## Running FastAPI Demos

FastAPI servers run with uvicorn:

```bash
# Start the server
uvicorn 07_fastapi_hello:app --reload

# The --reload flag enables auto-restart on code changes
```

Once running, open:
- http://localhost:8000 - API root
- http://localhost:8000/docs - Interactive documentation (Swagger UI)
- http://localhost:8000/redoc - Alternative documentation

## Demo Order Recommendation

1. **Session 1**: Run `04_http_methods_demo.py` to show GET/POST/PUT/DELETE
2. **Session 2**: Build `01_simple_get.py` live with students
3. **Session 3**: Evolve to `02_parsed_weather.py`, then `03_interactive_weather.py`
4. **Session 5**: Live-code starting from `07_fastapi_hello.py`, show `08_fastapi_crud.py`

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: requests` | Run `pip install requests` |
| `ModuleNotFoundError: fastapi` | Run `pip install fastapi uvicorn` |
| API returns 401 | Check your API key is correct and activated |
| Port 8000 in use | Use `uvicorn app:app --port 8001` |

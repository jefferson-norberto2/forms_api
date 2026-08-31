docker run -it -d \
  -v $(pwd):/app \
  -w /app \
  --name forms_api \
  -p 9300:9300 \
  python:3.14.3-slim \
  bash
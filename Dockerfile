FROM python:3.12-slim

WORKDIR /app
COPY app.py .

EXPOSE 8080

# HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
#     CMD python -c "import urllib.request; r = urllib.request.urlopen('http://127.0.0.1:8080/health', timeout=3); raise SystemExit(0 if r.status == 200 else 1)"

CMD ["python", "-u", "app.py"]

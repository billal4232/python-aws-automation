import requests

URL = 'https://aws.stadiumbuzz.live'

try:
    response = requests.get(URL,timeout=5)

    if response.status_code == 200:
        print(f"✅ Site is up — status {response.status_code}")
    else:
        print(f"❌ Site is down — status {response.status_code}")

    x_cache = response.headers.get('x-cache')
    if x_cache:
        print(f"✅ Served by CloudFront — {x_cache}")
    else:
        print("❌ CloudFront header missing")
except requests.exceptions.Timeout:
    print(f"❌ Health check failed: site did not respond within 5 seconds")

except Exception as e:
    print(f"❌ Health check failed: {e}")
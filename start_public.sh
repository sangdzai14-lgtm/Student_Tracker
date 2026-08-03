#!/bin/bash

echo "🚀 INITIATING PUBLIC DEPLOYMENT SEQUENCE..."

# 1. Environment Check
if [ ! -d "venv" ]; then
    echo "📦 Creating Virtual Environment..."
    python3 -m venv venv
fi
source venv/bin/activate
pip install -r requirements.txt flask-cors python-dotenv > /dev/null

# 2. Cloudflare Tunnel Setup
if ! command -v cloudflared &> /dev/null; then
    echo "📥 cloudflared not found. Installing..."
    # OS Detection
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        curl -L https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64 -o cloudflared
        chmod +x cloudflared
        sudo mv cloudflared /usr/local/bin/
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew install cloudflare/cloudflare/cloudflared
    fi
fi

# 3. Start Flask Server in background
echo "🐍 Starting Academic AI Backend..."
python3 app.py &
FLASK_PID=$!

# Wait for Flask to stabilize
sleep 5

# 4. Launch Cloudflare Tunnel and Capture URL
echo "🛡️ Establishing Secure Tunnel..."
cloudflared tunnel --url http://localhost:5000 > tunnel.log 2>&1 &
TUNNEL_PID=$!

# Wait for URL to be generated
echo "⏳ Awaiting Public HTTPS Link..."
while ! grep -q "trycloudflare.com" tunnel.log; do
  sleep 2
done

PUBLIC_URL=$(grep -o 'https://[a-zA-Z0-9.-]*\.trycloudflare\.com' tunnel.log | head -n 1)

echo ""
echo "========================================================"
echo "✅ SYSTEM IS NOW PUBLICLY ACCESSIBLE!"
echo "🔗 URL: $PUBLIC_URL"
echo "========================================================"
echo ""

# Save to .env for persistence
echo "API_BASE_URL=$PUBLIC_URL" > .env

# 5. Open Browser (OS Dependent)
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    xdg-open "$PUBLIC_URL/analysis"
elif [[ "$OSTYPE" == "darwin"* ]]; then
    open "$PUBLIC_URL/analysis"
fi

echo "Press Ctrl+C to terminate the session."
trap "kill $FLASK_PID $TUNNEL_PID; exit" INT
wait

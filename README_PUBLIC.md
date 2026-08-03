# 🌍 Academic AI - Public Deployment Guide

This project is now configured for instant public internet access using **Cloudflare Tunnels**. No port forwarding or static IP required.

## 🚀 One-Click Start

### Windows
Double-click `start_public.bat`.
This will:
1. Initialize your Python environment.
2. Start the Flask backend on port 5000.
3. Launch a secure Cloudflare Tunnel.
4. **Automatically capture the public URL** (e.g., `https://random-words.trycloudflare.com`).
5. Open your default browser to the public Analysis dashboard.

### Linux / macOS
Run:
```bash
chmod +x start_public.sh
./start_public.sh
```

## 🛠️ Infrastructure Details

- **Backend:** Flask binds to `0.0.0.0:5000` to allow tunnel traffic.
- **Frontend:** Automatically uses the dynamic `API_BASE_URL` provided by the tunnel.
- **Security:** HTTPS is provided automatically by Cloudflare. CORS is enabled to allow the tunnel domain to communicate with the backend.

## 📁 Key Files
- `start_public.bat`: Main execution script for Windows.
- `start_public.sh`: Main execution script for Linux/Mac.
- `app.py`: Updated to handle dynamic base URLs and CORS.
- `.env`: Automatically updated with the latest public URL on each run.

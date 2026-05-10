# 🚀 BPanel – Cloudflare‑Free Proxy on GitHub

> *Turn your free GitHub account into a personal proxy server – no VPS, no Cloudflare, no credit card.*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![GitHub Codespaces](https://img.shields.io/badge/GitHub-Codespaces-black?logo=github)](https://github.com/features/codespaces)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

**BPanel** gives you a working HTTP/HTTPS/SOCKS5 proxy in less than 30 seconds, using nothing but your free GitHub account.  
Perfect for regions with heavy internet censorship (Iran, China, Russia, etc.) where Cloudflare Workers are blocked.

✨ **No Cloudflare** – ✨ **No VPS** – ✨ **No monthly bills** – ✨ **Works from anywhere**

---

## 🔥 Why BPanel?

| Problem | BPanel Solution |
|---------|----------------|
| Cloudflare Workers blocked in Iran | ✅ Uses GitHub infrastructure (allowed) |
| VPS costs $5+/month | ✅ Completely free (60 hours/month) |
| Complex setup with domains, DNS | ✅ One‑click deploy from browser |
| DPI detects and blocks proxy protocols | ✅ Uses fragmented TLS + standard HTTP tunnels |

---

## ⚡ Quick Start (30 seconds)

1. **Click this badge** →  
   [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/yourusername/bpanel)

2. In the terminal that opens, paste:
   ```bash
   curl -sL https://raw.githubusercontent.com/yourusername/bpanel/main/start.sh | bash

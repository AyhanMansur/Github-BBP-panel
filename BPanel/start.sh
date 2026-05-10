#!/bin/bash

# BPanel – instant proxy using gost
# Runs HTTP proxy on port 8080

echo "🔧 Installing gost..."
curl -L https://github.com/ginuerzh/gost/releases/download/v2.11.5/gost-linux-amd64-2.11.5.gz | gunzip > gost
chmod +x gost

echo "🚀 Starting proxy on port 8080..."
./gost -L=:8080
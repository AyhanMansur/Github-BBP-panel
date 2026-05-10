import socket
import threading
import requests
import sys

LISTEN_PORT = 8888
# Change this to your actual Codespace public URL later
CODESPACE_URL = "https://github.com/codespaces/psychic-space-waddle-wrgw6765w465hg75j"

def handle(client):
    data = client.recv(8192)
    if not data:
        client.close()
        return
    try:
        request = data.decode('utf-8', errors='ignore')
        lines = request.split('\r\n')
        first = lines[0].split(' ')
        if len(first) < 2:
            client.close()
            return
        method = first[0]
        target = first[1]
        if not target.startswith('http'):
            target = 'http://' + target
        # Forward via Codespace
        proxy_url = CODESPACE_URL + "?url=" + target
        resp = requests.request(method, proxy_url, data=request.split('\r\n\r\n',1)[1] if '\r\n\r\n' in request else None, verify=False)
        client.send(f"HTTP/1.1 {resp.status_code}\r\n".encode())
        for k, v in resp.headers.items():
            if k.lower() != 'transfer-encoding':
                client.send(f"{k}: {v}\r\n".encode())
        client.send(b"\r\n")
        client.send(resp.content)
    except Exception as e:
        client.send(f"HTTP/1.1 500\r\n\r\n{str(e)}".encode())
    finally:
        client.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('127.0.0.1', LISTEN_PORT))
s.listen(5)
print(f"Local adapter running on 127.0.0.1:{LISTEN_PORT}")
while True:
    c, addr = s.accept()
    threading.Thread(target=handle, args=(c,)).start()
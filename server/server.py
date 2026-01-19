from flask import Flask, jsonify, request
import datetime
import socket
import os

app = Flask(__name__)


@app.route('/')
def get_endpoints():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps API Gateway</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif; max-width: 800px; margin: 50px auto; padding: 20px; background-color: #f8f9fa; color: #212529; }
            h1 { color: #212529; border-bottom: 2px solid #dee2e6; padding-bottom: 10px; font-weight: 600; }
            .pipeline { background: #fff; padding: 20px; border-radius: 8px; margin: 20px 0; border: 1px solid #dee2e6; box-shadow: 0 1px 3px rgba(0,0,0,0.08); }
            .stage { display: inline-block; background: #f1f3f4; padding: 10px 20px; margin: 5px; border-radius: 5px; border-left: 4px solid #495057; color: #495057; font-weight: 500; }
            a { color: #0066cc; text-decoration: none; }
            a:hover { text-decoration: underline; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; background: #fff; border-radius: 8px; overflow: hidden; border: 1px solid #dee2e6; }
            th, td { padding: 14px 16px; text-align: left; border-bottom: 1px solid #dee2e6; }
            th {  color: #212529; font-weight: 500; }
            tr:hover { background-color: #f8f9fa; }
            .tag { background: #6c757d; color: #fff; padding: 3px 10px; border-radius: 3px; font-size: 0.75em; font-weight: 500; }
        </style>
    </head>
    <body>
        <h1>DevOps API Gateway</h1>
        <div class="pipeline">
            <strong>CI/CD Pipeline</strong><br><br>
            <span class="stage">Build</span> &rarr; 
            <span class="stage">Test</span> &rarr; 
            <span class="stage">Push to GHCR</span> &rarr; 
            <span class="stage">Deploy to K8s</span>
        </div>
        <table>
            <tr><th>Endpoint</th><th>Description</th><th>Method</th></tr>
            <tr><td><a href="/hello">/hello</a></td><td>Service greeting response</td><td><span class="tag">GET</span></td></tr>
            <tr><td><a href="/health">/health</a></td><td>Health check</td><td><span class="tag">GET</span></td></tr>
        </table>
    </body>
    </html>
    '''


@app.route('/hello')
def helloPSL():
    hostname = socket.gethostname()
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Service Response</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f8f9fa; }}
            .container {{ background: #fff; padding: 40px 50px; border-radius: 8px; border: 1px solid #dee2e6; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
            h1 {{ color: #212529; margin: 0 0 24px 0; font-weight: 600; }}
            .info {{ color: #6c757d; font-size: 0.95em; margin: 8px 0; }}
            .label {{ color: #495057; font-weight: 500; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Hello PSL</h1>
            <p class="info"><span class="label">Served by:</span> Gunicorn + Flask</p>
            <p class="info"><span class="label">Orchestration:</span> Kubernetes</p>
        </div>
    </body>
    </html>
    '''


@app.route('/health')
def health():
    hostname = socket.gethostname()
    timestamp = datetime.datetime.now().isoformat()
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Check</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f8f9fa; }}
            .health-card {{ background: #fff; padding: 32px; border-radius: 8px; border: 1px solid #dee2e6; min-width: 400px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
            h2 {{ color: #212529; margin: 0 0 20px 0; border-bottom: 1px solid #dee2e6; padding-bottom: 12px; font-weight: 600; }}
            .status-row {{ display: flex; justify-content: space-between; padding: 10px 0; border-bottom: 1px solid #f1f3f4; }}
            .status-row:last-child {{ border-bottom: none; }}
            .label {{ color: #6c757d; }}
            .value {{ color: #212529; }}
            .status-ok {{ color: #198754; font-weight: 600; }}
            .indicator {{ width: 10px; height: 10px; background-color: #198754; border-radius: 50%; display: inline-block; margin-right: 10px; }}
        </style>
    </head>
    <body>
        <div class="health-card">
            <h2><span class="indicator"></span>Health Check</h2>
            <div class="status-row"><span class="label">Status</span><span class="status-ok">HEALTHY</span></div>
            <div class="status-row"><span class="label">Timestamp</span><span class="value">{timestamp}</span></div>
            <div class="status-row"><span class="label">Ready</span><span class="status-ok">True</span></div>
            <div class="status-row"><span class="label">App is up and running</span><span class="status-ok">True</span></div>
        </div>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True, port=5000)
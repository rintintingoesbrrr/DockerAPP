from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def get_endpoints():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>API Documentation</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
            h1 { color: #333; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
            table { width: 100%; border-collapse: collapse; margin-top: 20px; }
            th, td { padding: 12px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background-color: #007bff; color: white; }
            tr:hover { background-color: #f5f5f5; }
            a { color: #007bff; text-decoration: none; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <h1>API Endpoints</h1>
        <table>
            <tr><th>Endpoint</th><th>Description</th></tr>
            <tr><td><a href="/hello">/hello</a></td><td>Returns a greeting message</td></tr>
            <tr><td><a href="/health">/health</a></td><td>Returns the status of the application</td></tr>
        </table>
    </body>
    </html>
    '''


@app.route('/hello')
def helloPSL():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello</title>
        <style>
            body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background: linear-gradient(135deg, #007bff, #00d4ff); }
            h1 { color: white; font-size: 3em; text-shadow: 2px 2px 4px rgba(0,0,0,0.3); }
        </style>
    </head>
    <body>
        <h1>Hello PSL</h1>
    </body>
    </html>
    '''


@app.route('/health')
def health():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Health Status</title>
        <style>
            body { font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f0f0f0; }
            .status { text-align: center; padding: 40px; background: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
            .indicator { width: 20px; height: 20px; background-color: #28a745; border-radius: 50%; display: inline-block; margin-right: 10px; animation: pulse 2s infinite; }
            @keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: 0.5; } }
            h1 { color: #333; margin: 0; }
        </style>
    </head>
    <body>
        <div class="status">
            <h1><span class="indicator"></span>App is up and running</h1>
        </div>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True, port=5000)
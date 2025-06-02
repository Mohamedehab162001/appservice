from flask import Flask, request, render_template_string

app = Flask(__name__)

index_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Azure App</title>
</head>
<body>
    <h1>Welcome to My Azure Web App!</h1>
    <form action="/hello">
        <label>Enter your name:</label>
        <input type="text" name="name" required>
        <button type="submit">Say Hello</button>
    </form>
</body>
</html>
"""

hello_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>Hello, {{ name }}! 👋</h1>
    <a href="/">Back to Home</a>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(index_html)

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Azure User')
    return render_template_string(hello_html, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

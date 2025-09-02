from flask import Flask, render_template_string, request, url_for
import urllib.parse

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Happy Birthday!</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        h1 { color: #ff69b4; }
        input, button { padding: 10px; font-size: 16px; width: 80%; max-width: 300px; margin: 5px auto; display: block; }
        h2 { text-align: center; color: #4CAF50; }
        a { word-break: break-all; }
        @media (max-width: 600px) {
            body { margin-top: 20px; }
            h1 { font-size: 1.5em; }
            h2 { font-size: 1.2em; }
            input, button { font-size: 14px; }
        }
    </style>
</head>
<body>
    <h1>🎂 Happy Birthday Web 🎉</h1>
    <form method="post">
        <input type="text" name="name" placeholder="ใส่ชื่อของคุณ" required>
        <button type="submit">อวยพร!</button>
    </form>
    {% if name %}
        <h2>Happy Birthday {{ name }}!</h2>
        <p>
            <a href="{{ share_url }}" target="_blank">แชร์ลิงก์อวยพรให้ {{ name }}</a>
        </p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    name = None
    share_url = None
    if request.method == "POST":
        name = request.form.get("name")
        if name:
            share_url = url_for('wish', name=name, _external=True)
    return render_template_string(HTML, name=name, share_url=share_url)

@app.route("/wish/<name>", methods=["GET", "POST"])
def wish(name):
    name = urllib.parse.unquote(name)  # แก้ไขตรงนี้
    if request.method == "POST":
        return """
        <style>
        body, html {{
            height: 100%;
            margin: 0;
        }}
        .bg-text {{
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: 0;
            opacity: 0.07;
            font-size: 3em;
            color: #ff69b4;
            display: flex;
            flex-wrap: wrap;
            align-items: center;
            justify-content: center;
            pointer-events: none;
            overflow: hidden;
        }}
        .main-content {{
            position: relative;
            z-index: 1;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            padding: 10px;
        }}
        </style>
        <div class="bg-text">
            {names}
        </div>
        <div class="main-content">
            <img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3B1cTN0OGQ3Mnh4aGE0ejd2YnNybGt6cTZhYTBxNmNucHd1N21vYyZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/SwIMZUJE3ZPpHAfTC4/giphy.gif' alt='Happy Birthday' style='width:100%; max-width:300px; margin-bottom:20px;'/>
            <h1 style='text-align:center; font-size:2em; color:#ff69b4;'>🎉 สุขสันต์วันเกิด {0}! 🎂</h1>
            <p style='text-align:center; font-size:1.2em;'>ขอให้มีความสุขมาก ๆ นะ!</p>
            <p style='text-align:center; font-size:1em;'>สุขภาพร่างกายแข็งแรง ไม่เจ็บ ไม่จน น่า!</p>
        </div>
        """.format(
            name,
            names=" ".join([name] * 40)
        )
    else:
        return """
        <div style='display:flex; flex-direction:column; justify-content:center; align-items:center; height:100vh;'>
            <form method='post'>
                <button type='submit' style='padding:15px 30px; font-size:1.2em; background:#ff69b4; color:white; border:none; border-radius:8px; cursor:pointer;'>
                    ดูคำอวยพรวันเกิด 🎉
                </button>
            </form>
        </div>
        """
        
if __name__ == "__main__":
    app.run(debug=True)
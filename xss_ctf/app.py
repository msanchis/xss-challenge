from flask import Flask, request, render_template_string

app = Flask(__name__)

# Leemos el flag al inicio del script
with open("flag.txt") as f:
    FLAG = f.read().strip()

@app.route("/")
def index():
    return '''
    <h2>Busca algo:</h2>
    <form method="get" action="/search">
        <input type="text" name="q">
        <input type="submit" value="Buscar">
    </form>
    '''

@app.route("/search")
def search():
    query = request.args.get("q", "")
    html = f"""
    <h3>Resultados para: {query}</h3>
    <!-- contenido oculto DOM -->
    <div id="flag" style="display:none">{FLAG}</div>
    """
    return render_template_string(html)

@app.route("/flag")
def flag():
    return "No puedes acceder así 😏"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


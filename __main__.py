import logging

from quart import Quart, render_template, request

app = Quart(__name__)

logger = logging.getLogger(__name__)

@app.route("/")
async def main():
    return await render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
async def create_valentine():
    form = await request.form
    if request.method == "POST":
        name = form["name"]
        message = form["message"]
        print(f"Received Valentine's from {name}: {message}")
    
    return await render_template("create.html")

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
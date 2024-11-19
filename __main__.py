import logging

from quart import Quart, render_template

app = Quart(__name__)

logger = logging.getLogger(__name__)

@app.route("/")
async def hello():
    return await render_template("index.html")


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
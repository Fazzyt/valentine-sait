import logging

from quart import Quart, render_template, request

from .telegram_bot import send_valentine, init_valentine_bot
from .config import config

app = Quart(
    __name__,
    static_folder="../static",
    template_folder="../templates",
    )

logger = logging.getLogger(__name__)

@app.route("/")
async def main():
    return await render_template("index.html")

@app.route("/create", methods=["GET", "POST"])
async def create_valentine():
    if request.method == "POST":
        form = await request.form
        username = form.get("name", "").strip()
        message = form.get("message", "").strip()

        if not username.startswith("@"):
            username = f"@{username}"

        result = await send_valentine(username, message)
        
    
    return await render_template("create.html")

@app.before_serving
async def startup():
    await init_valentine_bot() 

if __name__ == "__main__":
    app.run(
        host= config.HOST,
        port= config.PORT,
        debug= config.DEBUG
    )
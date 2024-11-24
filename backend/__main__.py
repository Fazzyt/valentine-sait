import logging

from quart import Quart, render_template, request

from .telegram_bot import send_valentine, init_valentine_bot

from .database import (
    create_valentine, get_valentine,
    get_total_valentine_id_count, init_db,
    SessionLocal
    )

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
async def create_valentine_page():
    if request.method == "POST":
        form = await request.form
        username = form.get("name", "").strip()
        message = form.get("message", "").strip()
        
        async with SessionLocal() as db:
            new_valentine = await create_valentine(db, recipient=username, message= message)

        if not username.startswith("@"):
            username = f"@{username}"
            
        if config.USE_BOT:
            result = await send_valentine(username, new_valentine.uuid)
    
    return await render_template("create.html")

@app.route("/valentine/<uuid>", methods=["GET"])
async def view_valentine_page(uuid: str):
    valentine = await get_valentine(valentine_uuid= uuid)
    message = valentine.message
    
    return await render_template("valentine.html", message= message)



@app.before_serving
async def startup():
    await init_db()
    if config.USE_BOT:
        await init_valentine_bot() 

if __name__ == "__main__":
    app.run(
        host= config.HOST,
        port= config.PORT,
        debug= config.DEBUG
    )
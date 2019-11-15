import base64

import aiohttp
from aiohttp import web

import aiohttp_jinja2

from aiohttp_session import setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage

from cryptography import fernet

from itsdangerous import URLSafeSerializer

import jinja2

from . import settings
from .middlewares import setup_middlewares
from .routes import setup_routes


async def on_shutdown(app):
    await app["client_session"].close()


async def init_app():
    app = web.Application()
    app["client_session"] = aiohttp.ClientSession()
    app["deeplink_s"] = URLSafeSerializer(settings.DEEPLINK_SECRET_KEY)

    fernet_key = fernet.Fernet.generate_key()
    secret_key = base64.urlsafe_b64decode(fernet_key)
    setup(app, EncryptedCookieStorage(secret_key))

    # Setup Jinja2 template renderer
    aiohttp_jinja2.setup(app, loader=jinja2.PackageLoader("templates"))

    # Setup views and routes
    setup_routes(app)

    setup_middlewares(app)

    # Graceful shutdown
    app.on_shutdown.append(on_shutdown)

    return app

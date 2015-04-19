from settings import settings
from mlx_app import app

app.run(host=settings.LISTEN, port=settings.PORT,
        debug=settings.DEBUG)

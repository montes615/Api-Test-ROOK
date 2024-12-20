from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from app.tools import global_exception_handler, http_exception_handler, ServerRequestLog
from slowapi import Limiter
from slowapi.middleware import SlowAPIMiddleware


load_dotenv()


limiter = Limiter(key_func=lambda request: request.client.host, default_limits=['20/minute'])

app = FastAPI(
    title='API-TEST-ROOK',
    description='Welcome to **API-TEST-ROOK**, a project developed to demonstrate technical skills in integrating third-party APIs, working with databases, and creating unit tests',
    version='0.0.1',
    contact={
        'name': 'Joseph Alberto Juárez Silva',
        'email': 'josephsilvagg@gmail.com'
    },
    root_path='/api/v1',
    )
app.state.limiter = limiter


app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.add_middleware(ServerRequestLog)
app.add_middleware(SlowAPIMiddleware)

from app.db import init_db
init_db()

from app.modules import modules
[app.include_router(router=router) for router in modules]
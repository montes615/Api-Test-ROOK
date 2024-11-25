from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from app.tools import global_exception_handler, http_exception_handler

load_dotenv()
app = FastAPI(root_path='/api/v1')

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

from app.modules import modules
[app.include_router(router=router) for router in modules]
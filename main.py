from fastapi import APIRouter, FastAPI
from auth.auth import auth_router
from client.client import router_client,router_public




app = FastAPI(title='CogniJobs FREENLANCER', version='1.0.0')

router = APIRouter()


@router.get('/hello')
async def hello():
    return {'message': 'Hello, FastAPI!'}

app.include_router(router, prefix='/main')
app.include_router(auth_router, prefix='/auth')
app.include_router(router_client)
app.include_router(router_public)

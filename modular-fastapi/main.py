from fastapi_offline import FastAPIOffline
from routers.main import MAIN_ROUTER
from fastapi.middleware.cors import CORSMiddleware

# Create LoRA

# fast api init
app = FastAPIOffline()
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(MAIN_ROUTER)

from fastapi import FastAPI
from controllers.users import router as UsersRouter
from controllers.hoots import router as HootsRouter  # NEW

app = FastAPI(
    title="Hoot API",
    description="A blogging platform API built with FastAPI",
    version="1.0.0"
)

# Register routers
app.include_router(UsersRouter, prefix="/api", tags=["Users"])
app.include_router(HootsRouter, prefix="/api", tags=["Hoots"])  # NEW

@app.get('/')
def home():
    return {'message': 'Welcome to Hoot API! Visit /docs for API documentation.'}
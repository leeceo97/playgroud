import uvicorn
from fastapi import FastAPI

from app.common.config import conf


def create_app():
    c = conf()
    app = FastAPI()

    # 데이터 베이스 이니셜라이즈

    # 미들웨어 정의

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=conf().PROJ_RELOAD)

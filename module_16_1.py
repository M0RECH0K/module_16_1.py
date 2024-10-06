from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome() -> dict:
    return {'message': "Главная страница"}

@app.get('/user/admin')
async def admin() -> dict:
    return {'message': "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def id_(user_id: float) -> dict:
    return {f"Вы вошли как пользователь №": {user_id}}

@app.get('/user')
async def users(username: str = 'Dmitry', age: int = 25) -> dict:
    return {f"Информация о пользователе."
            f"Имя": {username}, 'Возраст': {age}}
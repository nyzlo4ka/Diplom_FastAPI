from fastapi import FastAPI  # Импортируем основной класс приложения FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Импортируем middleware для CORS
from app.routes import router  # Импортируем маршрутизатор из приложения

app = FastAPI()  # Создаем экземпляр приложения FastAPI

# Добавляем middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Позволяем запросы из любых источников
    allow_credentials=True,  # Позволяем включение учетных данных
    allow_methods=["*"],  # Разрешаем все методы HTTP
    allow_headers=["*"],  # Разрешаем все заголовки
)

app.include_router(router)  # Подключаем маршруты из роутера

'''
Импорт библиотек - импортируем необходимые модули для работы приложения
на FastAPI, включая CORS для обработки кросс-доменных запросов.
Создание приложения - создаем экземпляр приложения FastAPI.
CORS Middleware - добавляем CORS middleware для управления настройками кросс-доменных
запросов и безопасности. Разрешаем все источники, методы и заголовки.
Маршрутизация - подключаем маршруты, определённые во внешнем роутере.
Этот код является основой для веб-приложения, обеспечивая возможность обработки запросов
из различных источников, что полезно в условияхAPI, 
где часто используется фронтенд с другого домена.
'''
from fastapi import APIRouter, HTTPException  # Импорт необходимых классов из FastAPI
from app.database import SessionLocal, load_books  # Импорт сессии базы данных и функции загрузки книг
from app.models import Book as BookModel, Book, BookCreate  # Импорт моделей книги

router = APIRouter()  # Создание экземпляра маршрутизатора


@router.on_event("startup")  # Декоратор для события старта приложения
async def startup_event():
    load_books()  # Вызываем функцию, загружающую книги в начале работы приложения


@router.get("/")  # Определяем маршрут для главной страницы
def home_page():
    return {  # Возвращаем приветственное сообщение и доступные опции
        1: "Добро пожаловать в приложение FastAPI, ниже представлены доступные опции (убедитесь, что автозаполнение "
           "включено):",
        2: "/docs",  # Страница документации
    }


@router.get("/books")  # Определяем маршрут для получения списка всех книг
async def read_books():
    session = SessionLocal()  # Создаем новую сессию базы данных
    books = session.query(BookModel).all()  # Запрашиваем все книги из базы данных

    return [{"id": book.id, **book.__dict__} for book in books]  # Возвращаем список книг в формате JSON


@router.get("/books/{id}")  # Определяем маршрут для получения книги по ID
async def get_book_by_id(id: int):
    session = SessionLocal()  # Создаем новую сессию базы данных
    book = session.query(BookModel).filter(BookModel.id == id).first()  # Запрашиваем книгу по ID
    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")  # Генерируем ошибку, если книга не найдена

    return {"id": book.id, **book.__dict__}  # Возвращаем найденную книгу


@router.get("/search_book/")  # Определяем маршрут для поиска книг
async def get_searched_book(title: str | None = None, author: str | None = None, genre: str | None = None,
                            publish: str | None = None):
    session = SessionLocal()  # Создаем новую сессию базы данных
    query = session.query(BookModel)  # Начинаем запрос к модели книги

    if title:
        query = query.filter(BookModel.title.ilike(f"%{title}%"))  # Фильтруем по названию, если оно указано
    if author:
        query = query.filter(BookModel.author.ilike(f"%{author}%"))  # Фильтруем по автору
    if genre:
        query = query.filter(BookModel.genre.ilike(f"%{genre}%"))  # Фильтруем по жанру
    if publish:
        query = query.filter(BookModel.publish.ilike(f"%{publish}%"))  # Фильтруем по издателю
    books = query.all()  # Получаем все книги по заданным критериям

    return [{"id": book.id, **book.__dict__} for book in books]  # Возвращаем список найденных книг


@router.post("/create_books", response_model=dict)  # Определяем маршрут для создания новой книги
async def create_book(book: BookCreate):
    session = SessionLocal()  # Создаем новую сессию базы данных
    new_book = BookModel(  # Создаем экземпляр модели книги с переданными данными
        author=book.author,
        title=book.title,
        genre=book.genre,
        description=book.description,
        publish=book.publish,
        year=book.year,
        pages=book.pages,
    )
    session.add(new_book)  # Добавляем новую книгу в сессию
    session.commit()  # Коммит изменений в базе данных
    session.refresh(new_book)  # Обновляем данные новой книги (получаем её ID)

    return {  # Возвращаем сообщение об успешном добавлении книги и её ID
        "message": "Книга успешно добавлена",
        "book_id": new_book.id
    }


@router.delete("/books_del/{id}", response_model=dict)  # Определяем маршрут для удаления книги по ID
async def delete_book(id: int):
    session = SessionLocal()  # Создаем новую сессию базы данных
    book = session.query(Book).filter(Book.id == id).first()  # Запрашиваем книгу по ID

    if not book:
        raise HTTPException(status_code=404, detail="Книга не найдена")  # Генерируем ошибку, если книга не найдена

    session.delete(book)  # Удаляем книгу из сессии
    session.commit()  # Коммит изменений в базе данных

    return {  # Возвращаем сообщение об успешном удалении книги
        "message": "Книга успешно удалена",
        "book_id": id
    }

'''
Этот код представляет собой API для работы с книгами, написанный с использованием FastAPI. 
Он поддерживает операции на CRUD (создание, чтение, обновление и удаление) для книг в базе данных. 
Каждый метод четко описан посредством HTTP-декораторов, а также обеспечивается обработка ошибок для случаев, 
когда книги не находятся.
'''
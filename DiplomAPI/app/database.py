import json
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from app.models import Base, Book

# Создаем подключение к базе данных SQLite
engine = create_engine('sqlite:///list_books.db')  # Инициализируем движок базы данных с заданным URI
Base.metadata.create_all(engine)  # Создаем все таблицы, определенные в метаданных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  # Создаем класс сессии для работы с БД


def load_books():
    # Открываем JSON файл, содержащий данные о книгах
    with open('books.json', encoding='utf-8') as f:
        books_data = json.load(f)  # Загружаем данные из файла в переменную

    session = SessionLocal()  # Создаем новую сессию для работы с базой данных
    for book_data in books_data:  # Проходим по каждому элементу в списке книг
        book_id = book_data['id']  # Извлекаем идентификатор книги
        # Проверяем, существует ли уже книга с данным ID
        existing_book = session.execute(select(Book).where(Book.id == book_id)).first()  # Выполняем запрос поиска книги
        if not existing_book:  # Если книга с этим ID не найдена
            # Создаем новый объект книги с данными из JSON
            book = Book(
                id=book_id,
                author=book_data['автор'],
                title=book_data['название'],
                genre=book_data['жанр'],
                description=book_data['описание'],
                publish=book_data['издательство'],
                year=book_data['год публикации'],
                pages=book_data['Количество страниц'],
            )
            session.add(book)  # Добавляем книгу в сессию
    session.commit()  # Сохраняем изменения в базе данных


'''
В этом коде реализуем загрузку книг из файла JSON в базу данных SQLite. 
Сначала создаем подключение к базе данных, затем из файла извлекаем данные
и проверяем существование книги с данным ID, чтобы избежать дубликатов. 
Если книги не существует, она добавляется в базу данных.
'''
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()  # Создаем базовый класс для декларативной модели


class Book(Base):
    __tablename__ = 'books'  # Указываем название таблицы в базе данных
    id = Column(Integer, primary_key=True, index=True)  # pk = primary key, index = индекс, уникальность идентификатора
    author = Column(String)  # Хранит имя автора книги в строковом формате
    title = Column(String, index=True)  # Хранит название книги и индексируется для быстрого поиска
    genre = Column(String)  # Хранит жанр книги в строковом формате
    description = Column(String)  # Хранит текстовое описание содержания книги
    publish = Column(String)  # Хранит название издательства книги
    year = Column(Integer)  # Хранит год публикации книги в числовом формате
    pages = Column(Integer)  # Хранит общее количество страниц в книге


# Pydantic модель для валидации данных при создании книги
class BookCreate(BaseModel):
    author: str  # Имя автора книги
    title: str  # Название книги
    genre: str  # Жанр книги
    description: str  # Описание книги
    publish: str  # Название издательства
    year: int  # Год публикации
    pages: int  # Количество страниц книги


'''
Эта модель Book представляет собой структуру данных для книги в таблице books
в базе данных. Каждый ее атрибут (id, author, title и т.д.) соответствует колонке в базе данных, 
где id является уникальным идентификатором, а автор, название и другие атрибуты 
позволяют хранить и извлекать информацию о книге. Использование индексов 
(например, на колонке title) позволяет значительно ускорить поисковые операции.
Модель BookCreate используется для валидации данных при создании новых записей о книгах.
'''
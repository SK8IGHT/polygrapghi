from pydantic import BaseModel

class BaseModelModify(BaseModel):
    pass

class Author(BaseModelModify):
    id: int
    name: str
    bio: str

class Book(BaseModelModify):
    id: int
    title: str
    published: str
    author_id: int

class Magazine(BaseModelModify):
    id: int
    title: str
    issue_date: str

class Article(BaseModelModify):
    id: int
    title: str
    content: str
    magazine_id: int

class Publisher(BaseModelModify):
    id: int
    name: str

class PrintingHouse(BaseModelModify):
    id: int
    name: str
    location: str
    publisher_id: int

class Printer(BaseModelModify):
    id: int
    name: str
    printing_house_id: int

class PrintJob(BaseModelModify):
    id: int
    job_date: str
    printer_id: int
    publication_id: int = None
    magazine_id: int = None
    article_id: int = None

class Address(BaseModelModify):
    id: int
    street: str
    city: str
    state: str
    postal_code: str

class Customer(BaseModelModify):
    id: int
    name: str
    email: str
    phone: str
    address_id: int

class Order(BaseModelModify):
    id: int
    order_date: str
    customer_id: int
    print_job_id: int

# The rest of your existing code remains unchanged.

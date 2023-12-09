import peewee

db = peewee.SqliteDatabase('database.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Author(BaseModel):
    name = peewee.CharField(null=False, default='')
    bio = peewee.TextField(default='')


class Book(BaseModel):
    title = peewee.CharField(null=False, default='')
    published = peewee.DateField(default='1900-01-01')  # Default to a date like '1900-01-01'
    author = peewee.ForeignKeyField(Author, backref='books')


class Magazine(BaseModel):
    title = peewee.CharField(null=False, default='')
    issue_date = peewee.DateField(default='1900-01-01')  # Default to a date like '1900-01-01'


class Article(BaseModel):
    title = peewee.CharField(null=False, default='')
    content = peewee.TextField(default='')
    magazine = peewee.ForeignKeyField(Magazine, backref='articles')


class Publisher(BaseModel):
    name = peewee.CharField(null=False, default='')


class PrintingHouse(BaseModel):
    name = peewee.CharField(null=False, default='')
    location = peewee.CharField(null=False, default='')
    publisher = peewee.ForeignKeyField(Publisher, backref='printing_houses')


class Printer(BaseModel):
    name = peewee.CharField(null=False, default='')
    printing_house = peewee.ForeignKeyField(PrintingHouse, backref='printers')


class PrintJob(BaseModel):
    job_date = peewee.DateTimeField(default='1900-01-01T00:00:00')  # Default to a date like '1900-01-01T00:00:00'
    printer = peewee.ForeignKeyField(Printer, backref='print_jobs')
    publication = peewee.ForeignKeyField(Book, backref='print_jobs', null=True)
    magazine = peewee.ForeignKeyField(Magazine, backref='print_jobs', null=True)
    article = peewee.ForeignKeyField(Article, backref='print_jobs', null=True)


class Customer(BaseModel):
    name = peewee.CharField(null=False, default='')
    email = peewee.CharField(null=False, default='')
    phone = peewee.CharField(null=False, default='')
    login = peewee.CharField(null=False, default='')
    password = peewee.CharField(null=False, default='')


class Order(BaseModel):
    order_date = peewee.DateTimeField(default='1900-01-01T00:00:00')  # Default to a date like '1900-01-01T00:00:00'
    customer = peewee.ForeignKeyField(Customer, backref='orders')
    print_job = peewee.ForeignKeyField(PrintJob, backref='orders')


# The rest of your existing code remains unchanged.

db.create_tables([
    Author,
    Book,
    Magazine,
    Article,
    Publisher,
    PrintingHouse,
    Printer,
    PrintJob,
    Customer,
    Order
])

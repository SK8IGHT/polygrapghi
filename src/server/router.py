from src.server.database import models as database_models
from src.server.database import pydantic_models
from src.server.service import RouterManager

routers = (
    RouterManager(
        database_model=database_models.Author,
        pydantic_model=pydantic_models.Author,
        prefix='/author',
        tags=['Author']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Book,
        pydantic_model=pydantic_models.Book,
        prefix='/book',
        tags=['Book']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Magazine,
        pydantic_model=pydantic_models.Magazine,
        prefix='/magazine',
        tags=['Magazine']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Article,
        pydantic_model=pydantic_models.Article,
        prefix='/article',
        tags=['Article']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Publisher,
        pydantic_model=pydantic_models.Publisher,
        prefix='/publisher',
        tags=['Publisher']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.PrintingHouse,
        pydantic_model=pydantic_models.PrintingHouse,
        prefix='/printing_house',
        tags=['PrintingHouse']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Printer,
        pydantic_model=pydantic_models.Printer,
        prefix='/printer',
        tags=['Printer']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.PrintJob,
        pydantic_model=pydantic_models.PrintJob,
        prefix='/print_job',
        tags=['PrintJob']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Customer,
        pydantic_model=pydantic_models.Customer,
        prefix='/customer',
        tags=['Customer']
    ).fastapi_router,

    RouterManager(
        database_model=database_models.Order,
        pydantic_model=pydantic_models.Order,
        prefix='/order',
        tags=['Order']
    ).fastapi_router,
)
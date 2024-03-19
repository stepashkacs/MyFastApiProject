from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import ProductCreate, Product
from .dependecies import product_by_id


router = APIRouter(tags=['Products'])


@router.get("/", response_model=list[Product])
async def get_products(
    # session: AsyncSession = Depends(db_helper.session_dependency), можем использовать и так или с другой зависимостю
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)

@router.post('/', response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)

@router.get("/{product_id}/", response_model=Product)
async def get_product(
    product: Product = Depends(product_by_id),
):
    return product

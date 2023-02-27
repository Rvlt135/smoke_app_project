"""Обработчик запросов"""
from fastapi import APIRouter
from .categories import router as categories_list

router = APIRouter()
router.include_router(categories_list, )

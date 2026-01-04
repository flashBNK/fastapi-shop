from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.category import Category
from ..schemas.category import CategoryCreate

class CategoryRepository:
    def __init__(self, db: Session):
        self.db = db # инициализация сессионной базы данных

    def get_all(self) -> List[Category]:
        return self.db.query(Category).all() # вывод всех категорий

    def get_by_id(self, category_id: int) -> Optional[Category]: # вывод категории по id
        return self.db.query(Category).filter(Category.id == category_id).first()

    def get_by_slug(self, slug: str) -> Optional[Category]: # вывод категории по slug
        return self.db.query(Category).filter(Category.slug == slug).first()

    def create(self, category_data: CategoryCreate) -> Category: # создание категории по схеме
        db_category = Category(**category_data.model_dump()) # берём данные их схемы
        self.db.add(db_category) # вносим данные в базу
        self.db.commit() # коммитим изменения
        self.db.refresh(db_category)
        return db_category


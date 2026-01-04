from pydantic import BaseModel, Field


class CategoryBase(BaseModel): # общие поля для всех схем
    name: str = Field(..., min_length=4, max_length=100,
                      description="Category name")
    slug: str = Field(..., min_length=4, max_length=100,
                      description="URL-friendly category name")

class CategoryCreate(CategoryBase): # схема для создания объекта
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Unique category identifiee") # отсутствует в схеме создания, потому что создаётся автоматически

    class Config:
        from_attributes = True 
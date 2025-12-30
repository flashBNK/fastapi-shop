from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    description = Column(Text) # может быть пустым
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False) # продукт зависит от категории, но категория не зависит от продукта
    image_url = Column(String) # может быть пустым
    created_at = Column(DateTime, default=datetime.utcnow)

    category = relationship("Category", back_populates="products") # взаимосвязь категории и продукта

    def __repr__(self):
        return f"<Product(id={self.id}, name='{self.name}', price={self.price})>"
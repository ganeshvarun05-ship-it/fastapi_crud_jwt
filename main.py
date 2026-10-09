from fastapi import FastAPI 
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from database import Base, engine, get_db
from models import User, product, price
from schemas import (create_user,product_create)
from auth import get_current_user

Base.metadata.create_all(bind=engine)

app = FastAPI(tittle="JWT VARUN API")

@app.get("/")
def index():
    return{"message:wellcome to JTW"}

@app.get("/user")
def read_current_user(
    current_user: User = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }

@app.post("/products")
def create_product(
    product_data: product_create,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_product = product(
        title=product_data.title,
        description=product_data.description,
        owner_id=current_user.id
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@app.get("/products")
def get_products(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(product)
        .filter(product.owner_id == current_user.id)
        .all()
    )

@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    item = (
        db.query(product)
        .filter(
            product.id == product_id,
            product.owner_id == current_user.id,
        )
        .first()
    )

    if item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    db.delete(item)
    db.commit()

    return {"message": "Product deleted successfully"}
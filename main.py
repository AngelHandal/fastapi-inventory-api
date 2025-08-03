# main.py
from fastapi import FastAPI, Depends, Body, HTTPException
from database import engine, Base, SessionLocal
from schemas import ProductBody
from models import Product

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

app = FastAPI()

@app.get("/products/")
def all_products(db = Depends(get_db)):
    products = db.query(Product).all()
    return products

@app.post("/add/product/")
def add_product(db = Depends(get_db), payload: ProductBody = Body(...)):
    new_product = Product(
        name=payload.name,
        description=payload.description,
        price=payload.price,
        quantity=payload.quantity
    )
    if payload.price < 0:
        raise HTTPException(status_code=400, detail="Price must be a positive number")
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/products/{product_id}")
def get_product_by_id(db = Depends(get_db), product_id = int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    else:
        return {"product": product}

@app.put("/products/{product_id}")
def update_product_by_id(db = Depends(get_db), product_id = int, payload: ProductBody = Body(...)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    else:  
        product.name = payload.name
        product.description = payload.description
        product.price = payload.price
        product.quantity = payload.quantity
        db.commit()
        db.refresh(product)
        
    return product

@app.delete("/products/{product_id}")
def delete_product_by_id(db = Depends(get_db), product_id= int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    else: 
        db.delete(product)
        db.commit()
    return {"message": f"Deleted product {product_id}"}
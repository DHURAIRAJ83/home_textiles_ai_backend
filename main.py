from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper.amazon import scrape_amazon
from scraper.flipkart import scrape_flipkart
from scraper.alibaba import scrape_alibaba

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get_best_price")
async def get_best_price(product: str):
    return {
        "amazon": scrape_amazon(product),
        "flipkart": scrape_flipkart(product),
        "alibaba": scrape_alibaba(product)
    }

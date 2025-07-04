
from fastapi import FastAPI
from scraper.amazon import scrape_amazon
from scraper.flipkart import scrape_flipkart
from scraper.alibaba import scrape_alibaba

app = FastAPI()

@app.get("/get_best_price")
def get_best_price(product: str):
    return {
        "amazon": scrape_amazon(product),
        "flipkart": scrape_flipkart(product),
        "alibaba": scrape_alibaba(product)
    }


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper.amazon import scrape_amazon
from scraper.flipkart import scrape_flipkart
from scraper.alibaba import scrape_alibaba

app = FastAPI()

# ✅ Enable CORS (Browser Access Allowed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with ["https://your-frontend-domain.com"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ API Route to fetch best prices
@app.get("/get_best_price")
def get_best_price(product: str):
    return {
        "amazon": scrape_amazon(product),
        "flipkart": scrape_flipkart(product),
        "alibaba": scrape_alibaba(product)
    }


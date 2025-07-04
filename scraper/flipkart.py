def scrape_flipkart(product):
    return [
        {
            "product": f"{product} - Flipkart Combo Pack",
            "price": "₹230",
            "website": "Flipkart",
            "link": f"https://www.flipkart.com/search?q={product.replace(' ', '+')}"
        }
    ]

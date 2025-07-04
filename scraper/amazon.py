def scrape_amazon(product):
    return [
        {
            "product": f"{product} - Soft Cotton Amazon",
            "price": "₹250",
            "website": "Amazon",
            "link": f"https://www.amazon.in/s?k={product.replace(' ', '+')}"
        },
        {
            "product": f"{product} - Premium Towel Amazon",
            "price": "₹240",
            "website": "Amazon",
            "link": f"https://www.amazon.in/s?k={product.replace(' ', '+')}"
        }
    ]

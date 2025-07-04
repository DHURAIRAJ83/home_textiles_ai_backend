def scrape_alibaba(product):
    return [
        {
            "product": f"{product} - Alibaba Bulk Deal",
            "price": "$3",
            "website": "Alibaba",
            "link": f"https://www.alibaba.com/trade/search?SearchText={product.replace(' ', '+')}"
        }
    ]

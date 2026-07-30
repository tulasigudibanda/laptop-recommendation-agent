import os
import requests

EBAY_ACCESS_TOKEN = os.getenv("EBAY_ACCESS_TOKEN")


def sync_ebay_laptops(query="laptop"):

    url = "https://api.ebay.com/buy/browse/v1/item_summary/search"

    headers = {
        "Authorization": f"Bearer {EBAY_ACCESS_TOKEN}"
    }

    params = {
        "q": query,
        "limit": 20
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    response.raise_for_status()

    items = response.json().get("itemSummaries", [])

    brands = [
        "Lenovo",
        "Dell",
        "HP",
        "ASUS",
        "Acer",
        "Apple",
        "MSI"
    ]

    laptops = []

    for item in items:

        title = item.get("title","")

        brand = "Unknown"

        for b in brands:
            if b.lower() in title.lower():
                brand = b
                break

        laptops.append({

            "item_id": item.get("itemId"),

            "brand": brand,

            "model": title,

            "price": float(
                item.get("price",{}).get("value",0)
            )

        })

    return laptops
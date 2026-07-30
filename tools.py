from data import laptops
from langchain.tools import tool
from db import is_db_empty, insert_laptops, search_by_budget
from ebay import sync_ebay_laptops


@tool
def search_by_budget_mock(max_price: int):
    """Returns laptops under a given budget."""

    results = []

    for laptop in laptops:
        if laptop["price"] <= max_price:
            results.append(laptop)

    return results


@tool
def search_by_brand(brand: str) -> list:
    """
    Returns all laptops for the specified brand.
    Example brands: Lenovo, Dell, HP, ASUS.
    """
    return [laptop for laptop in laptops if laptop["brand"].lower() == brand.lower()]


@tool
def search_by_ram(ram: int) -> list:
    """
    Returns all laptops with at least the specified RAM (in GB).
    Example: 8, 16, 32.
    """
    return [laptop for laptop in laptops if laptop["ram"] >= ram]


####################################


def load_data_if_needed():

    if is_db_empty():

        print("Database empty. Downloading from eBay...")

        laptops = sync_ebay_laptops("laptop")

        insert_laptops(laptops)

        print(f"Inserted {len(laptops)} laptops.")

    else:

        print("Using cached SQLite data.")


@tool
def search_laptops_by_budget(max_price: int):
    """
    Search laptops whose price is less than or equal to the given budget.
    """
    return search_by_budget(max_price)

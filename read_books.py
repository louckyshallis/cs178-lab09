# read_books.py
# Reads all items from the DynamoDB SandersonBooks table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "SandersonBooks"


def get_table():
    """Return a reference to the DynamoDB SandersonBooks table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_book(movie):
    title = movie.get("Title", "Unknown Title")
    page = movie.get("PageCount", "Unknown Page Count")
    year = movie.get("ReleaseYear", "No Release Year")

    print(f"  Title  : {title}")
    print(f"  Page Count   : {page}")
    print(f"  Release Year: {year}")


def print_all_books():
    """Scan the entire SandersonBooks table and print each item."""
    table = get_table()
    
    # scan() retrieves ALL items in the table.
    # For large tables you'd use query() instead — but for our small
    # dataset, scan() is fine.
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No books found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} book(s):\n")
    for book in items:
        print_book(book)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_books()


if __name__ == "__main__":
    main()

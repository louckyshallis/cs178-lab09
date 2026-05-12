# read_movies.py
# Reads all items from the DynamoDB Movies table and prints them.
# Part of Lab 09 — feature/read-dynamo branch

import boto3
from boto3.dynamodb.conditions import Key

# -------------------------------------------------------
# Configuration — update REGION if your table is elsewhere
# -------------------------------------------------------
REGION = "us-east-1"
TABLE_NAME = "Movies"


def get_table():
    """Return a reference to the DynamoDB Movies table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)


def print_movie(movie):
    title = movie.get("Title", "Unknown Title")
    year = movie.get("Year", "Unknown Year")
    ratings = movie.get("Ratings", "No ratings")
    runtime = movie.get("RuntimeMinutes", "No Data")

    print(f"  Title  : {title}")
    print(f"  Year   : {year}")
    print(f"  Ratings: {ratings}")
    print(f"  Runtime: {runtime}")



def print_all_movies():
    """Scan the entire Movies table and print each item."""
    table = get_table()

    print("Connected table:", table.table_name)

    response = table.scan()

    print("RAW RESPONSE:")
    print(response)

    items = response.get("Items", [])

    if not items:
        print("No movies found. Make sure your DynamoDB table has data.")
        return

    print(f"Found {len(items)} movie(s):\n")
    for movie in items:
        print_movie(movie)


def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_movies()


if __name__ == "__main__":
    main()

import json
import connect
from models import Author

with open("authors.json", "r", encoding="utf-8") as f:
    authors = json.load(f)
    for author in authors:
        if Author.objects(fullname=author["fullname"]).first():
            continue
        else:
            author_obj = Author(fullname=author["fullname"],
                                born_date=author["born_date"],
                                born_location=author["born_location"],
                                description=author["description"])
            author_obj.save()
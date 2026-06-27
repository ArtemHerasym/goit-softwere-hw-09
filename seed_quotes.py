import json
import connect
from models import Author, Quote

with open("quotes.json", "r", encoding="utf-8") as f:
    quotes = json.load(f)
    for quote in quotes:
        author_obj = Author.objects(fullname=quote["author"]).first()
        if not author_obj:
           continue
        if Quote.objects(quote=quote["quote"]).first():
           continue

        quote_obj = Quote(tags=quote["tags"], author=author_obj, quote=quote["quote"])
        quote_obj.save()

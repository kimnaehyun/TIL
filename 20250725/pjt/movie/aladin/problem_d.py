import json
from pprint import pprint

def best_book(books):
    books_rank = 0
    first_book = ""
    for book in books :
        books_json = open(current_dir / 'data' / 'books' / f'{book["id"]}.json', encoding='utf-8')
        books_load = json.load(books_json)
        if books_rank < books_load['customerReviewRank'] :
            books_rank = books_load['customerReviewRank']
    for book in books :
        books_json = open(current_dir / 'data' / 'books' / f'{book["id"]}.json', encoding='utf-8')
        books_load = json.load(books_json)
        if books_rank == books_load['customerReviewRank'] :
            first_book = books_load['title'] 
    
    return first_book


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    pprint(best_book(books))

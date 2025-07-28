import json


def new_books(books):
    arr = []
    for book in books :
        books_json = open(current_dir / 'data' / 'books' / f'{book["id"]}.json', encoding='utf-8')
        books_load = json.load(books_json)
        if "2023" == books_load['pubDate'].split("-")[0] :
            arr += [books_load['title']]
    return arr


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    print(new_books(books))

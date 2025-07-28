import json
from pprint import pprint


def books_info(books, categories):
    book_arr = []
    
    for book in books :
        category_arr = []
        for book_category_id in book['categoryId'] :
            for category in categories :
                if category['id'] == book_category_id :
                    category_arr += [category['name']]  
        book_arr += [{'author' : book['author'],
        'categoryId' : category_arr,
        'cover' : book['cover'],
        'description' : book['description'],
        'id' : book['id'],
        'priceSales' : book['priceSales'],
        'title' : book['title'],
        }]
        
    return book_arr


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    books_json = open(current_dir / 'data' / 'books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open(
        current_dir / 'data' / 'categories.json', encoding='utf-8'
    )
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))

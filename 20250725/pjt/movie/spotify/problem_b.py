import json
from pprint import pprint


def artist_info(artist, genres):
    arr = []
    for artist_genres_id in artist['genres_ids'] :
        for genre in genres :
            if genre['id'] == artist_genres_id :
                arr += [genre['name']]    
    return {
 'genres_names': arr,
 'id': artist['id'],
 'images': artist['images'],
 'name': artist['name'],
 'type': artist['type'],}


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artist.json', encoding='utf-8')
    artist_dict = json.load(artist_json)

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artist_dict, genres_list))

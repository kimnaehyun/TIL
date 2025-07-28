import json
from pprint import pprint


def artist_info(artists, genres):
    artist_info_arr = []
    
    for artist in artists :
        genres_names_arr = []
        for genres_id in artist['genres_ids'] :
            for genre in genres :
                if genre['id'] == genres_id :
                    genres_names_arr += [genre['name']]  
        artist_info_arr += [{
 'genres_names': genres_names_arr,
 'id': artist['id'],
 'images': artist['images'],
 'name': artist['name'],
 'type': artist['type'],}]
        
    return artist_info_arr


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))

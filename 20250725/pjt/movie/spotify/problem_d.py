import json


def max_popularity(artists):
    artists_rank = 0
    first_artist = ""
    for artist in artists :
        artists_json = open(current_dir / 'data' / 'artists' / f'{artist["id"]}.json', encoding='utf-8')
        artists_load = json.load(artists_json)
        if artists_rank < artists_load['popularity'] :
            artists_rank = artists_load['popularity']
    for artist in artists :
        artists_json = open(current_dir / 'data' / 'artists' / f'{artist["id"]}.json', encoding='utf-8')
        artists_load = json.load(artists_json)
        if artists_rank == artists_load['popularity'] :
            first_artist = artists_load['name'] 
    
    return first_artist


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    print(max_popularity(artists_list))

import json
from pprint import pprint


def dec_artists(artists):
    arr = []
    for artist in artists :
        artists_json = open(current_dir / 'data' / 'artists' / f'{artist["id"]}.json', encoding='utf-8')
        artists_load = json.load(artists_json)
        if 10000000 <= artists_load['followers']['total'] :
            arr += [{'name' : artists_load['name'],
                    'uri-id' : artists_load['uri'].split(":")[2]
                    }]
    return arr


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    pprint(dec_artists(artists_list))

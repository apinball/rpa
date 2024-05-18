import requests
import base64
from dotenv import load_dotenv
import os

def load_environment():
    # 환경 변수 파일을 로드하고 Spotify 클라이언트 ID와 시크릿을 반환
    load_dotenv()
    client_id = os.getenv('SPOTIFY_CLIENT_ID')
    client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
    return client_id, client_secret

def get_access_token(client_id, client_secret):
    # Spotify API로부터 액세스 토큰을 얻기 위해 OAuth 인증을 수행
    auth_url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(auth_url, {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret,
    })
    auth_response_data = auth_response.json()
    return auth_response_data['access_token']

def get_playlist(playlist_id, access_token):
    # 주어진 플레이리스트 ID로부터 플레이리스트 정보를 가져옴
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    playlist_response = requests.get(playlist_url, headers=headers)
    return playlist_response.json()

def extract_song_titles_and_artists(playlist_data):
    # 플레이리스트 데이터로부터 노래 제목과 아티스트 이름을 추출하여 리스트로 반환
    songs = []
    for item in playlist_data['tracks']['items']:
        track = item['track']
        song_title = track['name']
        artist_names = ', '.join(artist['name'] for artist in track['artists'])
        songs.append(f"{song_title} - {artist_names}")
    return songs

def main():
    # 환경 설정을 로드하고, Spotify 플레이리스트의 노래 제목과 아티스트를 출력하는 테스트 코드
    client_id, client_secret = load_environment()
    access_token = get_access_token(client_id, client_secret)
    playlist_id = '37i9dQZF1DXcBWIGoYBM5M'  # Today's Top Hits
    playlist_data = get_playlist(playlist_id, access_token)
    songs = extract_song_titles_and_artists(playlist_data)
    # 노래 제목과 아티스트를 순위와 함께 출력
    for index, song in enumerate(songs, start=1):
        print(f"{index}. {song}")

if __name__ == "__main__":
    main()  # 스크립트가 직접 실행되면 main() 함수 호출

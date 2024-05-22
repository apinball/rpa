import requests, json, response

def kakaotalk_message(client_id,code):
    url="https://kauth.kakao.com/oauth/token"

    data={'grant_type':'authorization_code',
    'client_id': client_id,
    'redirect_uri':'https://localhost.com',
    'code':code}

    response=requests.post(url, data=data)

    if response.status_code !=200 :
        print('error : ', response.json())
    else:
        tokens=response.json()
        
    url='https://kapi.kakao.com/v2/api/talk/memo/default/send'

    headers={'Authorization': 'Bearer '+ tokens['access_token']}

    template={"object_type": "list",
            "header_title": "오늘의 첫번째 플레이 리스트",
            "header_link": {"web_url": "",
                            "mobile_web_url": ""},
            "contents": [
            ]
            }

    data={"template_object":json.dumps(template)}
    response=requests.post(url, headers=headers, data=data)
    if response.status_code !=200 :
        print('error : ', response.json())

    else:
        print('done')

if __name__ == "__main__":
    kakaotalk_message()
    
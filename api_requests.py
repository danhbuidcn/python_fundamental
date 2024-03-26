import requests
import pdb

BASE_URL = 'https://mochien-server-release.mochidemy.com'
USER_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoxODc0MTIyLCJ0b2tlbiI6IjY2Yjk2Nzk3MGI4MzEiLCJpcCI6IjExOC43MC41Mi4zOSIsImV4cCI6MTc1NDk2MjcxMX0.AdFv4pseKE00MiYVa-8-_KL2RVHQGTeazL5p0cBHNVo'

def fetch_data(params, request_type):
    # Define parameters
    course_id = '10'
    page = '1'
    offset = '350'
 
    # Query parameters
    params = {**params, 'page': page, 'offset': offset, 'user_token': USER_TOKEN}

    # Headers
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
        'Authorization': f'Bearer {USER_TOKEN}',
        'Connection': 'keep-alive',
        'Origin': 'https://learn.mochidemy.com',
        'PrivateKey': 'M0ch1M0ch1_En_$ecret_k3y',
        'Referer': 'https://learn.mochidemy.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"'
    }

    if (request_type == 'lesson'):
        url = f'{BASE_URL}/api/v5.0/lesson'
    else:
        url = f'{BASE_URL}/api/v5.0/lesson/words'

    try:
        # Send GET request with dynamic parameters
        response = requests.get(url, headers=headers, params=params)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json().get('data', [])
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

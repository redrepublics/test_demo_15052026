import requests

url = 'https://official-joke-api.appspot.com/random_joke'

#
# get, парсинг ответа, сравнение переменных, статус
# {"type":"general","setup":"How do you fix a damaged jack-o-lantern?","punchline":"You use a pumpkin patch.","id":123}
def test_one():
    response = requests.get(url)
    response_data = response.json()
    spec_data = response_data['type']
    assert response.status_code == 200
    assert spec_data == 'general'

    # print(response.text)


def test_two():
    response = requests.get(url)
    response_data = response.json()
    spec_data = response_data['id']
    assert spec_data != '123'

# OneList

再次特别感谢ONelist的原创作者，我这里只是添加我需要的功能部分，此版本修改为python2

## Installation

```bash
# apt install python-pip redis-server

git clone https://github.com/payne-huang/Onlist.git
cd Onlist

pip install -r requirements.txt
# Get auth_token --> Get refresh_token --> Setup config

gunicorn app:app -b 127.0.0.1:5000 -D --limit-request-line 8188
```

## Configuration

Create a config file named `config.json`

```json
{
  "token": "<refresh_token>",
  "location_path": "/",
  "start_directory": "/",
  "refresh_seconds": 720,
  "metadata_cached_seconds": 768,
  "structure_cached_seconds": 840
}
```

## Get auth_token

> https://login.microsoftonline.com/common/oauth2/authorize?response_type=code&client_id=ea2b36f6-b8ad-40be-bc0f-e5e4a4a7d4fa&redirect_uri=http://localhost/onedrive-login

## Get refresh_token

```bash
code="<auth_token>"
wget --no-check-certificate --post-data="client_id=ea2b36f6-b8ad-40be-bc0f-e5e4a4a7d4fa&client_secret=h27zG8pr8BNsLU0JbBh5AOznNS5Of5Y540l/koc7048=&grant_type=authorization_code&resource=https://api.office.com/discovery/&redirect_uri=http://localhost/onedrive-login&code=$code" 'https://login.microsoftonline.com/common/oauth2/token' -qO-
```

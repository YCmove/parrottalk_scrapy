COOKIES = '__utma=173579682.1846711591.1551106388.1551106388.1551106388.1; __utmz=173579682.1551106388.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); fbm_399939833405464=base_domain=.parrottalks.com; amplitude_id_03f1549bb309566c3700c5277b015081parrottalks.com=eyJkZXZpY2VJZCI6IjNjNDAxYmZjLWJiOTEtNGMyNy1hZTgzLWRiZWYwYTRiMDMwNVIiLCJ1c2VySWQiOiIxMTA3ODkiLCJvcHRPdXQiOmZhbHNlLCJzZXNzaW9uSWQiOjE1NTExMDYzODg5ODYsImxhc3RFdmVudFRpbWUiOjE1NTExMTAzODkxNDYsImV2ZW50SWQiOjI1LCJpZGVudGlmeUlkIjo1NSwic2VxdWVuY2VOdW1iZXIiOjgwfQ==; parrottalks=18e51eed9548f97c2ca57ca5f55e46874558de0b%2BUcop18uCr5tEReKGyl9Qq7wRMstuRoHHIJEhYSdM; session_payload=b66a8192e04425f8e5fb6f9dce5c8ae678de3e55%2B%2BvFs%2BRc%2BOrMiedd5l45CFuxRmiaQPJY3ZngFeo%2FayT9ymXLxpPtFoVUszAABkyV%2FsEWIhf7HcqzKR73Yyb1RXxHIP%2B0v%2Bh8uANpYZum8KyHU7cmfRTP5Y4QyUVVI9K64r1hI2XR5Bct7DyMTmVqYgsk8eu1cSrTjh5NIlHtiEHcBk7l812rOWBHFxFNUMwA9PeHsKzgcmPpZcjMUpeftMN3Lrsnb8MxtCSKkX8h7t%2FxxdxhhJ2HxaV%2Fj0ybO2gXMHKLIjHZM9arNwrU00I%2B2o81J1tO8uvaUnv80B2H9vCf4TMkwmOPsd4432%2BzxgR%2FqbMfIgYyOoxAlPc5Xkl6hCg%3D%3D; ajs_user_id=null; ajs_anonymous_id=%2282505b30-5b0c-491f-9c38-56c4cb39a37b%22; fbsr_399939833405464=hNxvaDz8PnhqjqBq4ue1Yw_kuXN8tIh008sB2hPJ4QU.eyJ1c2VyX2lkIjoiMjI2NzE1NTI4NjYzMzA1MyIsImNvZGUiOiJBUURGR2VVelFDRzZvWl9NX2ZUdkt4NkJWS2hDM2ltUWExVlJXRUxBVVJjUjBXZTZVQzJwWnNFM3ZVLUtlRUcybG9vWVE2SkUtQmg4WDBObDV6c0dtTmF5X3R2WnhfTm9wQTdDS3pDRTRwRTB3d0otN2dUV0Iyc0dxdHJwbF9VMVFqNGJlNnNtVEdZSFBSWmkxU1UwdGwyMVk4QVhEZ0dOeDFnVDNLXzBFbkZhU2ZFQ0VrRVNJR0FtOFlTUXFwUjR3MFJPM3E3SlE2Rk9MSUhtTkQ3RHBjWTJIMGlSbDFVT0g4Z2RVa1N5S2ZXTW5ab3ZjSDRMajgwNmZJN3BneUtZU0RaS3loQnpKU0hsaFNGTDJCa1RRZEZNQVpIaUVubGR6a0ZYeHNZRnF4SlVrZE1qTWpERlVWZTJMWWxRUkc4MjBXZFZ1REQxb3BiN2FQYTJwQTcxbE1QSCIsIm9hdXRoX3Rva2VuIjoiRUFBRnJ2alpCem9CZ0JBSk9sQVFDZnFraVZ1UHZiVGJaQjhqRWNoNmloYjAzSFh0dXBOWFpBZTlIa2F4T1Z0ck5mclUxRFIxWXlDcE1GRTRlN0xLTmVUUVY1WUFYMk9vdjlaQ0tPREx1dndtQUJvalNiOGlPV3hGWWZXUUx2MlpBR0hiMDRLdjNaQkRrTFpCb0VjUnRTWkE5cEoxYlpBWTE0Tm1Md0NDeGpMU0Qya0NOSlUzNUlJVXhHTHZiSzFPSmVQbE5aQ3BQdTNzWkE5NktBWkRaRCIsImFsZ29yaXRobSI6IkhNQUMtU0hBMjU2IiwiaXNzdWVkX2F0IjoxNTYyMzA3MTA3fQ'

def cookieChangeToDict(cookie):
    '''
    將cookie字串轉換成字典
    :param cookie: 登入後的cookie
    :return:字典
    '''
    cookieList = cookie.split(';')
    cookieDict = {}
    for cookie in cookieList:
        name = cookie.split('=', maxsplit=1)[0].strip()
        value = cookie.split('=', maxsplit=1)[1].strip()
        cookieDict[name] = value
    return cookieDict

print(cookieChangeToDict(COOKIES))
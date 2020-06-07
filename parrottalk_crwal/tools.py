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
    
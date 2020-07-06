import requests, urllib3

pythonanywhere_usernames_list = [
    'getagent',
    'getfw',
    'getletters',
    'getln',
    'getmyrta',
    'getprojekt',
    'getrs',
    'getrsdata',
    'getsc',
    'skfb',
    'getsola',
    'getuna',
    'getynsbase',
    'ynsight'
]

for pythonanywhere_username in pythonanywhere_usernames_list:
    URL_site =\
'http://%pythonanywhere_username%.pythonanywhere.com/'\
        .replace(
            '%pythonanywhere_username%',
            pythonanywhere_username
        )

    is_online = False

    try:
        request_result = requests.get(
            URL_site,
            # timeout=self._request_timeout
        )
        response_text = request_result.text

        if\
    not 'something went wrong :-(' in response_text\
and not 'Hello, World!' in response_text\
and not 'Coming Soon: PythonAnywhere' in response_text\
and not '<body class="yota-theme" hidden="">' in response_text\
and not '500 Internal Server Error' in response_text:
            is_online = True

    except requests.exceptions.Timeout as e:
        print(e)

    except urllib3.exceptions.MaxRetryError as e:
        print(e)

    except requests.exceptions.ConnectionError as e:
        print(e)

    is_online_all = is_online
    is_online_index = is_online

    report =\
'''%pythonanywhere_username%:
  URL_site: %URL_site%
  %is_online_all%\n'''\
        .replace('%pythonanywhere_username%', pythonanywhere_username)\
        .replace('%URL_site%', URL_site)\
        .replace('%is_online_all%', str(is_online_all))

    print(report)
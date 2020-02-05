import requests


# res = requests.post(
#     "https://datasend.webpython.graders.eldf.ru/submissions/1/",
#     headers={
#         'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'
#     }
# )


# {'password': 'ktotama', 'path': 'submissions/super/duper/secret/', 
# 'login': 'galchonok', 
# 'instructions': 'Сделайте PUT запрос на тот же хост, но на path указанный в этом документе c логином и паролем из этого документа. 
# Логин и пароль также передайте в заголовке Authorization.'}

res = requests.put(
    "https://datasend.webpython.graders.eldf.ru/submissions/super/duper/secret/",
    params={
        'password': 'ktotama',
        'login': 'galchonok',
    },
    auth=('galchonok', 'ktotama'),
    headers={
        'Authorization': 'Basic galchonokktotama'
    }
)
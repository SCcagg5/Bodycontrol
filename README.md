# Bodycontrol
Api designed to stimulate multiple point off the body trought hardware tech


`docker-compose up -d` from inside the dir launch the app


route | methods | params | desc |
 -|-|-|-|
/test/          |`['OPTIONS  'POST  'GET']` |`[]`
/login/         |`['OPTIONS  'POST']`       |`[pass]`
/infos/         |`['OPTIONS  'POST']`       |`[token, id]`
/create/     	  |`['OPTIONS  'POST']`       |`[token, id]`
/changepower/   |`['OPTIONS  'POST']`       |`[token, id, index, value]`
/changedata/    |`['OPTIONS  'POST']`       |`[token, id, index, value]`
/admin/infos/   |`['OPTIONS  'POST']`       |`[token]`

params | format | desc |
-|-|-|
pass | string | password set in server.py (env var)
token | string | returned by `/login/`
id | int | number of the device
index | string / int | name of the index you want to interact width
value | string / int | value you want to set on the selected index

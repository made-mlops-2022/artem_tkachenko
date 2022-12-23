### Переменная окружения
```
    export FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
```

### Запуск:
```
    docker compose up --build
```

### Скриншоты

Папка ./pics
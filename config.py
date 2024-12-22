# Версія додатку
app_version = '1.0.0 Release' # Версія бота

# Telegram API налаштування
API_TID = "12345678" # ID API для Telegram
API_HASH = "123456789adcdefghijklmnopqrstuvwxyz" # Hash API для Telegram
PHONE_NUMBER = "+1234567890" # Номер телефону для авторизації в Telegram

# Префікси для команд
PREFIXES = "$"

# Шляхи до моделей та бінарних файлів
FFMPEG_PATH = "packages/ffmpeg/bin/ffmpeg.exe" # Шлях до бінарного файлу FFMPEG (НЕ МОЖЕТЬ БУТИ ЗМІНЕНИЙ)

THE_CAT_API_KEY = "live_ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" # Ключ для доступу до сервісу The Cat API

# Налаштування Whisper для STT
whisper_presets = 'accurate' # Підтримується: accurate, fast, normal, custom
beam_size = 10 # Використовується для керування кількістю варіантів, які Whisper буде розглядати    
best_of = 10 # Використовується для керування кількістю варіантів, які Whisper буде розглядати
temperature = 0.2 # Використовується для керування випадковістю результату
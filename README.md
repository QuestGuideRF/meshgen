# meshgen

`meshgen` — Blender add-on для генерации и анализа 3D-мешей с помощью AI. Аддон добавляет в `VIEW_3D` панель `MeshGen`, где можно отправлять запросы агенту, подключать локальные GGUF-модели или удалённые провайдеры и получать результат прямо в сцене Blender.

## ✨ Особенности

- Интегрируется в Blender как add-on с собственной панелью в боковой панели 3D View.
- Поддерживает локальный и удалённый backend.
- Для удалённого режима умеет работать с Hugging Face, Ollama, Anthropic и OpenAI.
- Для локального режима умеет загружать GGUF-модели из Hugging Face.
- Использует `CodeAgent` и набор инструментов для операций над объектами Blender.
- Поддерживает LLaMA-Mesh для генерации и описания low-poly мешей.
- Опционально включает Hyper3D для генерации 3D-ассетов и импорта результата в сцену.
- Ведёт историю шагов и лог в текстовом блоке `meshgen log`.

## 🚀 Быстрый старт

### Требования

- Blender 4.2+

### Установка

1. Установите аддон из исходников или упакованного архива через Blender.
2. Включите `meshgen` в настройках аддонов.
3. Откройте настройки аддона и выберите backend:
   - `Local` — локальная GGUF-модель.
   - `Remote` — Hugging Face, Ollama, Anthropic или OpenAI.

### Базовый сценарий

1. Перейдите в `3D View` → боковая панель → вкладка `MeshGen`.
2. Введите запрос, например `Create a cube`.
3. Нажмите `Submit`.
4. При необходимости откройте лог кнопкой с иконкой текста.

## 📁 Структура проекта

- `__init__.py` — регистрация и перезагрузка модулей аддона.
- `blender_manifest.toml` — метаданные расширения Blender.
- `backend.py` — загрузка модели и запуск AI-агента.
- `operators.py` — операторы Blender для чата, отмены, загрузки моделей и логов.
- `preferences.py` — настройки backend, моделей и интеграций.
- `properties.py` — состояние запроса и история событий.
- `tools.py` — инструменты агента для работы с объектами Blender, LLaMA-Mesh и Hyper3D.
- `ui.py` — панель интерфейса в Blender.
- `utils.py` — вспомогательные классы и функции.
- `models/` — локальные модели.
- `requirements/` — варианты зависимостей для CPU/CUDA окружений.

## 🛠 Использование

Поддерживаемые режимы:

- `Local` — используется локальная GGUF-модель через `llama_cpp_python`.
- `Remote` — используется API Hugging Face, Ollama, Anthropic или OpenAI.

Что можно делать через инструменты:

- создавать базовые меш-объекты в сцене;
- анализировать существующие mesh-объекты;
- генерировать low-resolution меш через LLaMA-Mesh;
- вызывать Hyper3D и импортировать полученный объект в Blender.

Ключевые настройки из Preferences:

- `backend_type`
- `current_model`
- `llm_provider`
- `temperature`
- `context_length`
- `enable_hyper3d`

## 🧪 Технологии

- Python
- Blender Python API
- `smolagents`
- `huggingface_hub`
- `liteLLM`
- `llama_cpp_python`
- Hyper3D API

Подпись относится к текущей версии проекта.

---

Автор: legenda  
Telegram: [@LEGENDA_SD](https://t.me/LEGENDA_SD)

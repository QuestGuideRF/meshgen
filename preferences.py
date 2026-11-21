import bpy
from .backend import Backend
from .tools import LlamaMeshModelManager
from .utils import get_available_models
def get_downloaded_models (self ,context ):
    items =[]
    for model in get_available_models ():
        items .append ((model ,model ,f"Use {model } for local inference"))
    if not items :
        items .append (("","Модели не загружены","Сначала скачайте модель"))
    return items
def reset_backend (self ,context ):
    backend =Backend .instance ()
    backend .reset ()
    props =bpy .context .scene .meshgen_props
    props .state ="READY"
    props .history .clear ()
    for window in bpy .context .window_manager .windows :
        for area in window .screen .areas :
            if area .type in ["PREFERENCES","VIEW_3D"]:
                area .tag_redraw ()
class MeshGenPreferences (bpy .types .AddonPreferences ):
    bl_idname =__package__
    __annotations__ ={
    "backend_type":bpy .props .EnumProperty (
    name ="Тип серверной части",
    description ="Выберите тип серверной части, который будет использоваться для генерации.",
    items =[
    (
    "LOCAL",
    "Local",
    "Используйте локальный интегрированный бэкэнд llama_cpp_python для вывода.",
    ),
    (
    "REMOTE",
    "Remote",
    "Use a remote API for inference (Ollama, OpenAI, etc.)",
    ),
    ],
    default ="REMOTE",
    update =reset_backend ,
    ),
    "current_model":bpy .props .EnumProperty (
    name ="Текущая модель",
    description ="Выберите модель для локального вывода",
    items =get_downloaded_models ,
    update =reset_backend ,
    ),
    "download_repo_id":bpy .props .StringProperty (
    name ="Идентификатор репозитория",
    description ="Идентификатор репозитория Hugging Face для модели",
    default ="bartowski/Meta-Llama-3.1-8B-Instruct-GGUF",
    ),
    "download_filename":bpy .props .StringProperty (
    name ="Filename",
    description ="Имя файла модели для скачивания",
    default ="Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
    ),
    "llm_provider":bpy .props .EnumProperty (
    name ="Provider",
    description ="Выберите поставщика, который будет использоваться для удаленного вывода.",
    items =[
    (
    "huggingface",
    "Обнимающее лицо",
    "Используйте API Hugging Face для вывода",
    ),
    ("ollama","Ollama","Используйте сервер Ollama для вывода"),
    ("anthropic","Anthropic","Используйте Anthropic API для вывода"),
    ("openai","OpenAI","Используйте API OpenAI для вывода"),
    ],
    default ="huggingface",
    update =reset_backend ,
    ),
    "huggingface_model_id":bpy .props .StringProperty (
    name ="Идентификатор модели",
    description ="Идентификатор модели, которую нужно использовать",
    default ="meta-llama/Llama-3.3-70B-Instruct",
    update =reset_backend ,
    ),
    "huggingface_api_key":bpy .props .StringProperty (
    name ="API-ключ",
    description ="Ключ API обнимающего лица",
    default ="",
    subtype ="PASSWORD",
    update =reset_backend ,
    ),
    "ollama_endpoint":bpy .props .StringProperty (
    name ="Endpoint",
    description ="Базовый URL-адрес сервера Ollama",
    default ="http://localhost:11434",
    update =reset_backend ,
    ),
    "ollama_model_name":bpy .props .StringProperty (
    name ="Название модели",
    description ="Название используемой модели",
    default ="gemma3",
    update =reset_backend ,
    ),
    "ollama_api_key":bpy .props .StringProperty (
    name ="Ключ API (необязательно)",
    description ="Ollama API key (optional, used for private models)",
    default ="",
    subtype ="PASSWORD",
    update =reset_backend ,
    ),
    "anthropic_model_id":bpy .props .StringProperty (
    name ="Идентификатор модели",
    description ="Идентификатор модели, которую нужно использовать",
    default ="claude-3-5-sonnet-latest",
    update =reset_backend ,
    ),
    "anthropic_api_key":bpy .props .StringProperty (
    name ="API-ключ",
    description ="Антропный API-ключ",
    default ="",
    subtype ="PASSWORD",
    update =reset_backend ,
    ),
    "openai_model_id":bpy .props .StringProperty (
    name ="Идентификатор модели",
    description ="Идентификатор модели, которую нужно использовать",
    default ="gpt-4o",
    update =reset_backend ,
    ),
    "openai_api_key":bpy .props .StringProperty (
    name ="API-ключ",
    description ="API-ключ OpenAI",
    default ="",
    subtype ="PASSWORD",
    update =reset_backend ,
    ),
    "downloading":bpy .props .BoolProperty (default =False ),
    "download_progress":bpy .props .FloatProperty (
    subtype ="PERCENTAGE",
    min =0.0 ,
    max =100.0 ,
    precision =0 ,
    ),
    "show_generation_settings":bpy .props .BoolProperty (
    name ="Показать настройки генерации",
    description ="Показать или скрыть настройки генерации",
    default =False ,
    ),
    "temperature":bpy .props .FloatProperty (
    name ="Temperature",
    description ="Управляет случайностью генерации (выше = более креативно, ниже = более предсказуемо)",
    default =0.7 ,
    min =0.0 ,
    max =1.0 ,
    ),
    "context_length":bpy .props .IntProperty (
    name ="Длина контекста",
    description ="Управляет максимальным количеством токенов в контекстном окне.",
    default =32768 ,
    min =1024 ,
    max =65536 ,
    ),
    "show_integrations_settings":bpy .props .BoolProperty (
    name ="Показать настройки интеграции",
    description ="Показать или скрыть настройки интеграции",
    default =False ,
    ),
    "enable_hyper3d":bpy .props .BoolProperty (
    name ="Включить Hyper3D",
    description ="Включить Hyper3D для создания сетки",
    default =False ,
    ),
    "hyper3d_api_key":bpy .props .StringProperty (
    name ="API-ключ",
    description ="Ключ API Hyper3D",
    default ="awesomemcp",
    subtype ="PASSWORD",
    ),
    }
    def draw (self ,context ):
        layout =self .layout
        backend_box =layout .box ()
        backend_box .label (text ="Backend",icon ="SETTINGS")
        backend_box .prop (self ,"backend_type",expand =True )
        if self .backend_type =="LOCAL":
            info_box =backend_box .box ()
            info_box .label (text ="Запускайте модели прямо в Blender.",icon ="INFO")
            col =info_box .column (align =True )
            col .label (text ="Требуется не менее 8 ГБ видеопамяти.")
            col .label (text ="Небольшие локальные модели могут иметь проблемы с агентным поведением.")
            local_box =layout .box ()
            header =local_box .row (align =True )
            header .label (text ="Скачанные модели",icon ="PACKAGE")
            header .operator ("meshgen.open_models_folder",text ="",icon ="FILE_FOLDER")
            models =get_available_models ()
            if models :
                local_box .prop (self ,"current_model")
            elif not self .downloading :
                local_box .label (text ="Ни одна модель не загружена.",icon ="INFO")
                op =local_box .operator (
                "meshgen.download_model",
                text ="Скачать рекомендуемую модель",
                icon ="IMPORT",
                )
                op .repo_id =self .download_repo_id
                op .filename =self .download_filename
            if self .downloading :
                row =local_box .row (align =True )
                row .label (text ="Downloading...")
                row .prop (self ,"download_progress",slider =True ,text ="")
        else :
            remote_box =layout .box ()
            remote_box .prop (self ,"llm_provider")
            remote_box .separator ()
            if self .llm_provider =="ollama":
                info_box =remote_box .box ()
                info_box .label (
                text ="Запускайте модели на локальном сервере Ollama.",icon ="INFO"
                )
                col =info_box .column (align =True )
                col .label (text ="1. Загрузите и установите Ollama с сайта ollama.com.")
                col .label (text ="2. Запустите `ollama serve` в терминале.")
                remote_box .separator ()
                remote_box .prop (self ,"ollama_endpoint")
                remote_box .prop (self ,"ollama_model_name")
                remote_box .prop (self ,"ollama_api_key")
            elif self .llm_provider =="huggingface":
                info_box =remote_box .box ()
                info_box .label (
                text ="Запускайте модели с помощью Hugging Face API.",icon ="INFO"
                )
                col =info_box .column (align =True )
                col .label (text ="1. Создайте учетную запись на hf.co.")
                col .label (text ="2. Перейдите на страницу hf.co/settings/tokens и создайте новый токен.")
                col .label (text ="3. Вставьте токен в поле ключа API.")
                remote_box .separator ()
                remote_box .prop (self ,"huggingface_model_id")
                remote_box .prop (self ,"huggingface_api_key")
            elif self .llm_provider =="anthropic":
                info_box =remote_box .box ()
                info_box .label (text ="Запускайте модели с помощью Anthropic API.",icon ="INFO")
                col =info_box .column (align =True )
                col .label (text ="1. Создайте учетную запись на console.anthropic.com.")
                col .label (
                text ="2. Go to console.anthropic.com/settings/keys and create a key"
                )
                col .label (text ="3. Вставьте ключ в поле ключа API.")
                remote_box .separator ()
                remote_box .prop (self ,"anthropic_model_id")
                remote_box .prop (self ,"anthropic_api_key")
            elif self .llm_provider =="openai":
                info_box =remote_box .box ()
                info_box .label (text ="Запускайте модели с помощью OpenAI API.",icon ="INFO")
                col =info_box .column (align =True )
                col .label (text ="1. Создайте учетную запись на платформе.openai.com.")
                col .label (
                text ="2. Go to platform.openai.com/api-keys and create a new secret key"
                )
                col .label (text ="3. Вставьте секретный ключ в поле ключа API.")
                remote_box .separator ()
                remote_box .prop (self ,"openai_model_id")
                remote_box .prop (self ,"openai_api_key")
        options_box =layout .box ()
        header =options_box .row (align =True )
        header .prop (
        self ,
        "show_generation_settings",
        icon ="TRIA_DOWN"if self .show_generation_settings else "TRIA_RIGHT",
        icon_only =True ,
        emboss =False ,
        )
        header .label (text ="Настройки генерации")
        if self .show_generation_settings :
            options_box .prop (self ,"temperature",slider =True )
            options_box .prop (self ,"context_length",slider =True )
        plugin_box =layout .box ()
        header =plugin_box .row (align =True )
        header .prop (
        self ,
        "show_integrations_settings",
        icon ="TRIA_DOWN"if self .show_integrations_settings else "TRIA_RIGHT",
        icon_only =True ,
        emboss =False ,
        )
        header .label (text ="Integrations")
        if self .show_integrations_settings :
            llama_mesh_box =plugin_box .box ()
            llama_mesh_box .label (text ="LLaMA-Mesh",icon ="PACKAGE")
            llama_mesh_box .label (
            text ="Используйте LLaMA-Mesh для создания и понимания локальной сетки.",
            )
            if LlamaMeshModelManager .instance ().is_loaded :
                llama_mesh_box .label (text ="LLaMA-Mesh загружен",icon ="CHECKBOX_HLT")
                llama_mesh_box .operator (
                "meshgen.unload_llama_mesh",text ="Выгрузить LLaMA-Mesh",icon ="X"
                )
            else :
                if self .backend_type =="LOCAL":
                    llama_mesh_box .label (
                    text ="Требуется 5 ГБ дополнительной видеопамяти. Не рекомендуется использовать локальный сервер.",
                    icon ="ERROR",
                    )
                llama_mesh_box .operator (
                "meshgen.load_llama_mesh",text ="Загрузить LLaMA-Mesh",icon ="IMPORT"
                )
            hyper3d_box =plugin_box .box ()
            hyper3d_box .label (text ="Hyper3D",icon ="PACKAGE")
            hyper3d_box .label (
            text ="Use Hyper3D (Rodin) API for mesh generation.",
            )
            hyper3d_box .prop (self ,"enable_hyper3d")
            if self .enable_hyper3d :
                hyper3d_box .prop (self ,"hyper3d_api_key")
def register ():
    bpy .utils .register_class (MeshGenPreferences )
def unregister ():
    bpy .utils .unregister_class (MeshGenPreferences )
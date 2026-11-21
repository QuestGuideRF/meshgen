import bpy
class MeshGenEvent (bpy .types .PropertyGroup ):
    __annotations__ ={
    "type":bpy .props .EnumProperty (
    name ="Type",
    description ="Тип мероприятия",
    items =[
    ("THINKING","Thinking","Агент думает"),
    ("STEP","Step","Шаг в мыслительном процессе агента"),
    ("ERROR","Error","Произошла ошибка"),
    ("CANCELED","Canceled","Операция отменена пользователем"),
    ("SUCCESS","Result","Результат операции"),
    ("LOADING","Loading","Модель загружается"),
    ("LOADING_SUCCESS","Loaded","Модель успешно загрузилась"),
    ("LOADING_ERROR","Error","Модель не удалось загрузить"),
    ],
    ),
    "content":bpy .props .StringProperty (
    name ="Content",
    description ="Содержание мероприятия",
    default ="",
    ),
    }
class MeshGenProperties (bpy .types .PropertyGroup ):
    __annotations__ ={
    "prompt":bpy .props .StringProperty (
    name ="Prompt",
    description ="Введите запрос на AI-агента",
    default ="Создать куб",
    ),
    "state":bpy .props .EnumProperty (
    name ="State",
    description ="Текущее состояние агента",
    items =[
    ("READY","Ready","Агент готов обработать запрос"),
    ("LOADING","Loading","Агент загружается"),
    ("RUNNING","Running","Агент работает"),
    ("CANCELED","Canceled","Операция помечена для отмены"),
    ],
    default ="READY",
    ),
    "history":bpy .props .CollectionProperty (type =MeshGenEvent ),
    }
def register ():
    bpy .utils .register_class (MeshGenEvent )
    bpy .utils .register_class (MeshGenProperties )
    bpy .types .Scene .meshgen_props =bpy .props .PointerProperty (type =MeshGenProperties )
def unregister ():
    bpy .utils .unregister_class (MeshGenEvent )
    bpy .utils .unregister_class (MeshGenProperties )


PURCHASE_UNITARY_LIMIT = 250.80
MAX_COLUMS = 6

CARD = 0
CHEQUE = 1
URL = 'http://automationpractice.com/index.php'
SEARCH = "//input[@class='search_query form-control ac_input' and @id='search_query_top']"
LOGIN_BUTTON = "//a[@class='login' and contains(text(),'Sign in')]"
EMAIL_CREATE = "//input[@class='is_required validate account_input form-control' and @id='email_create']"
EMAIL_CREATE_BUTTON = "//button[@class='btn btn-default button button-medium exclusive' and @id='SubmitCreate']"
NAME_INPUT = "//input[@class = 'is_required validate form-control' and @id='customer_firstname']"
APELLIDO_INPUT = "//input[@class = 'is_required validate form-control' and @id='customer_lastname']"
PASSWORD_INPUT = "//input[@class = 'is_required validate form-control' and @id='passwd']"
ADDRESS_INPUT="//input[@class='form-control' and @id='address1']"
CITY_INPUT= "//input[@class='form-control' and @id='city']"
SELECT_STATE_INPUT= "//div[@id='uniform-id_state']"
SELECT_OPTIONS = './select/option'
POST_CODE_INPUT = "//input[@class='form-control uniform-input text' and @id='postcode']"
NUMBER_INPUT = "//input[@class='form-control' and @id='phone_mobile']"
ALIAS_INPUT =" //input[@class='form-control' and @id='alias']"
SUBMIT_CREATE_ACCOUNT = "//button[@class='btn btn-default button button-medium' and @id='submitAccount']"


EMAIL_INPUT = "//input[@class='is_required validate account_input form-control' and @id='email']"

PASSWORD_ACCOUNT_INPUT = "//input[@class='is_required validate account_input form-control' and @id='passwd']"
SUBMIT_LOGIN = "//button[@class='button btn btn-default button-medium' and @id='SubmitLogin']"

SEARCH_BUTTON = "//button[@class='btn btn-default button-search' and @name='submit_search']"

SEARCH_PRODUCT_LISTING = "//h1[contains(@class,'product-listing')]//span[@class='heading-counter']"
NOT_RESULT = 0
SEARCH_PRODUCTS_RESULTS = "//ul[@class='product_list grid row']//li//a[@class='product-name']"

MODEL_PRODUCT = "//span[@class='editable' and contains(text(),'demo')]"

PRICE_PRODUCT ="//p[@class='our_price_display']//span[@id='our_price_display']"


ICON_PLUS = "//i[@class='icon-plus']"

ADD_TO_CART = "//button[@class='exclusive' and @type='submit']"

TAKE_QUANTITY= "//div[@class='layer_cart_product_info']//div//span[@id='layer_cart_product_quantity']"

EXIT_EMERGETN_WINDOW = "//span[@class='continue btn btn-default button exclusive-medium']"


GO_CART = "//a[@title='View my shopping cart']//b"

NEXT_STEP = "//a[@class = 'button btn btn-default standard-checkout button-medium']"

NEXT_STEP_II = "//button[@class = 'button btn btn-default button-medium']"

ACCEPT_TERMS_AND_CONDITIONS = "//div[@class='checker' and @id='uniform-cgv']//span"
NEXT_STEP_III = "//button[@class = 'button btn btn-default standard-checkout button-medium']"

CARD_SELECTION_BUTTON ="//a[@class='bankwire']" 

CONFIRM_ORDER_WITH_CARD = "//button[@class='button btn btn-default button-medium']"

CHEQUE_SELECTION_BUTTON = "//a[@class='cheque']" 

CONFIRM_ORDER_WITH_CHECK = "//button[@class='button btn btn-default button-medium']"


GO_TO_PURCHARSE_ORDERS = "//a[@class='button-exclusive btn btn-default']"
TOTAL_SHIPPING = "//tr[@class='cart_total_delivery']//td[@class='price' and @id='total_shipping']"
PURCHARSE_ORDER = "//a[1][@class='color-myaccount']" 

GO_BACK_RESULTS = 'window.history.go(-1)'

ARCHIVO_STORE = './files/productos.xlsx'

NAME_ELEMENT = 'NOMBRE'
COLOR = 'COLOR'
SEPARATE_COLOR = 'color-'
MODEL = 'MODELO' 
UNIT_PRICE = 'PRECIO UNITARIO'
AMOUNT = 'CANTIDAD'
PURCHARSE_GENERATED_ORDER = 'ORDEN GENERADA'
ORDERED = 'ORDENADOS'
TOTALS = 'TOTALES'

TOTAL_C_SHIPPING = 'TOTAL CON ENVIO'
TOTAL_S_SHIPPING = 'TOTAL SIN ENVIO'
COST_SHIPPING = 'ENVIO'
DATE_PURCHASE = 'ORDEN DE COMPRA'

YES = 'si'
NO  = 'no'




##########################################3

CALYX_LOG = 'CalyxBotBills'
OPEN_ICON = './calyx location/calyx_logo.png'
MAIN_ID = './calyx location/id.png'
NUM_FIELDS = 5
ADD_ITEM = './calyx location/add_item.png'
PREPARE_TO_WRTIE ='./calyx location/access_to_write.png'
INTER_OF_CLICK = 0.2
INTER_OF_WRITE = 0.2
PAGE_DOWN = 'pagedown'
RIGHT = 'right'
SAVE = './calyx location/save.png'
ENTER = 'enter'
APP_OPTION = './calyx location/app.png'
EXIT = './calyx location/exit.png'
MAX = 30

BILLS_FILE =  './files/facturas.xlsx' 
BILLS_COLUMNS = 6
NAME_MAIN_ID = 'Informes'

NUMBER_KEY= 'numero'
IDENTITY = 'identificacion'
BUYER = 'comprador'
UNIT_AMOUNT = 'monto unitario'
PARTIAL_AMOUNT = 'cantidad'



############################################33


MESSAGE_ELEMENT_NOT_CLICKED = 'Couldnt clicked on element with path:' 
MESSAGE_ELEMENT_NOT_SENT_KEYS = 'Couldnt sent keys to element with path:' 
MESSAGE_ELEMENT_NOT_FOUND = 'Couldnt found element with path:' 
MESSAGE_INPUT_SEARCH_NOT_SET = 'Couldnt set the search input'
MESSAGE_OPTION_NOT_SELECTED = 'Couldnt found options of element with path:' 
MESSAGE_STORE_PAGE_NOT_OPEN = 'Couldnt opened the store page with link:' 
MESSAGE_REGISTER_NOT_DONE = 'Couldnt done new user registry'
MESSAGE_LOGIN_NOT_DONE = 'Couldnt done the login for the user'
MESSAGE_PRODUCT_NOT_SEARCHED = 'Couldnt searched the product:' 
MESSAGE_MODEL_NOT_SEARCHED = 'Couldnt searched the model:' 
MESSAGE_NOT_ADDED_TO_CART = 'Couldnt added the product to the cart'
MESSAGE_PURCHASE_NOT_DONE = 'Couldnt done the purchase'
MESSAGE_UNEXPECTED_ERROR = 'There was an unexpected error in the program excecution'
MESSAGE_CANNOT_ORDER_PRODUCT = 'Couldnt order product:' 


CANNOT_LOCATE_SCREEN = 'Couldnt locate and click center on screen :' 

SYSTEMLOG = 'MystroreSystemlogs'
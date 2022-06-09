
from excel.excel import Excel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

import web_store_const as st
import settings.settings as config
import time

from logs.sistem_log import MySystemLogs

class MyStore:

    def __init__(self):

        self.__url = st.URL
        self.__total = 0
        self.__max_amount_buy = st.PURCHASE_UNITARY_LIMIT

        try:

            self.__wd = webdriver.Chrome()
            self.__log = MySystemLogs(st.SYSTEMLOG)
            self.__wd.get(self.__url)
            self.__wd.maximize_window()
            self.__wd.implicitly_wait(10)

        except Exception as e:
            # Revisar esto
            message = st.MESSAGE_STORE_PAGE_NOT_OPEN + \
                self.__url + f':{ str(e)}'
            self.__log.LogCritical(message)
            raise Exception(e)

    def __element_to_be_clickable(self,xpath):
        try:
            element = WebDriverWait(self.__wd, 10).until(
                Ec.element_to_be_clickable((By.XPATH, xpath)))
        except Exception as e:
            raise Exception(e)

        return element
    
    def __element_to_be_clickable_select(self, xpath, xpath_option, option):

        try:
            select_options = self.__element_to_be_clickable(xpath)
            select_options.click()
            time.sleep(1)
            options_available = select_options.find_elements(
                By.XPATH, xpath_option)
            found = False
            for option_available in options_available:
                if option_available.text == option:
                    option_available.click()
                    found = True
                    break
            if not found:
                options_available[0].click()

            select_options.click()

        except Exception as e:

            message = st.MESSAGE_OPTION_NOT_SELECTED + \
                xpath + xpath_option + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __search_element(self, name_element):

        try:
            search = self.__element_to_be_clickable(st.SEARCH)
            search.clear()
            search.send_keys(name_element)
            self.__element_to_be_clickable(st.SEARCH_BUTTON).click()

        except Exception as e:
            message = st.MESSAGE_PRODUCT_NOT_SEARCHED + \
                name_element + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __find_model(self, model, color):

        try:

            find = self.__element_to_be_clickable(st.SEARCH_PRODUCT_LISTING)
            find = (find.text)[0]
            if find == st.NOT_RESULT:
                self.__set_search()
                return None
            results = self.__wd.find_elements(by=By.XPATH, value=st.SEARCH_PRODUCTS_RESULTS)

            for i in range(len(results)):

                results[i].click()
                model_dress = self.__element_to_be_clickable(st.MODEL_PRODUCT)

                model_dress = model_dress.text
                if model_dress == model:

                    self.__element_to_be_clickable(f"//ul[@class='clearfix']//li//a[contains(@name,'{color}')]").click()
                    unit_price = self.__element_to_be_clickable(st.PRICE_PRODUCT)
                    unit_price = ((unit_price.text).split('$'))[
                        1].replace(',', '.')

                    return float(unit_price)
                
                self.__wd.execute_script(st.GO_BACK_RESULTS )
                results = self.__wd.find_elements(by=By.XPATH, value=st.SEARCH_PRODUCTS_RESULTS)

            return None
        except Exception as e:

            message = st.MESSAGE_MODEL_NOT_SEARCHED + model + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __add_to_cart(self, quantity):
        try:

            for _ in range(1, quantity):
                self.__element_to_be_clickable(st.ICON_PLUS).click()

            self.__element_to_be_clickable(st.ADD_TO_CART).click()

            real_quantity = self.__element_to_be_clickable(st.TAKE_QUANTITY)
            real_quantity = int(real_quantity.text)

            self.__element_to_be_clickable(st.EXIT_EMERGETN_WINDOW).click()

            return real_quantity

        except Exception as e:
            message = st.MESSAGE_NOT_ADDED_TO_CART + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def register_user(self):

        try:
            self.__element_to_be_clickable(st.LOGIN_BUTTON).click()
            self.__element_to_be_clickable(
                st.EMAIL_CREATE).send_keys(config.EMAIL_USER)
            self.__element_to_be_clickable(st.EMAIL_CREATE_BUTTON).click()

            # ---------form register --------------

            self.__element_to_be_clickable(st.NAME_INPUT).send_keys(config.NAME_USER)
            self.__element_to_be_clickable(st.APELLIDO_INPUT).send_keys(config.SURNAME_USER)
            self.__element_to_be_clickable(st.PASSWORD_INPUT).send_keys(config.PASSWORD_USER)
            self.__element_to_be_clickable(st.ADDRESS_INPUT).send_keys(config.ADDRESS_USER)
            self.__element_to_be_clickable(st.CITY_INPUT).send_keys(config.CITY_USER)
            self.__element_to_be_clickable_select(st.SELECT_STATE_INPUT, st.SELECT_OPTIONS, config.STATE_USER)
            self.__element_to_be_clickable(st.POST_CODE_INPUT).send_keys(config.POST_CODE_USER)
            self.__element_to_be_clickable(st.NUMBER_INPUT).send_keys(config.NUMBER_USER)

            alias_user = self.__element_to_be_clickable(st.ALIAS_INPUT)
            alias_user.clear()
            alias_user.send_keys(config.ALIAS_USER)

            self.__element_to_be_clickable(st.SUBMIT_CREATE_ACCOUNT).click()

        except Exception as e:

            message = st.MESSAGE_REGISTER_NOT_DONE + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def login_user(self, user, password):

        try:

            self.__element_to_be_clickable(st.LOGIN_BUTTON).click()
            self.__element_to_be_clickable(st.EMAIL_INPUT).send_keys(user)
            self.__element_to_be_clickable(st.PASSWORD_ACCOUNT_INPUT).send_keys(password)
            self.__element_to_be_clickable(st.SUBMIT_LOGIN).click()

        except Exception as e:

            message = st.MESSAGE_LOGIN_NOT_DONE + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def buy_elements(self, type_of_payment=st.CARD):

        try:
       
            self.__element_to_be_clickable(st.GO_CART).click()

            total_shipping = self.__element_to_be_clickable(st.TOTAL_SHIPPING)
            total_shipping = ((total_shipping.text).split('$'))[
                1].replace(',', '.')
            total_shipping = float(total_shipping)

            self.__element_to_be_clickable(st.NEXT_STEP).click()
            self.__element_to_be_clickable(st.NEXT_STEP_II).click()
            self.__element_to_be_clickable(st.ACCEPT_TERMS_AND_CONDITIONS).click()
            self.__element_to_be_clickable(st.NEXT_STEP_III).click()

            if type_of_payment == st.CARD:
                self.__element_to_be_clickable(st.CARD_SELECTION_BUTTON).click()
                self.__element_to_be_clickable(st.CONFIRM_ORDER_WITH_CARD).click()

            else:
                self.__element_to_be_clickable(st.CHEQUE_SELECTION_BUTTON).click()
                self.__element_to_be_clickable(st.CONFIRM_ORDER_WITH_CHECK).click()

            self.__element_to_be_clickable(st.GO_TO_PURCHARSE_ORDERS).click()

            purchase_order_element = self.__element_to_be_clickable(st.PURCHARSE_ORDER)
            purchase_order = purchase_order_element.text

            return {st.COST_SHIPPING: total_shipping,
                    st.DATE_PURCHASE: purchase_order}

        except Exception as e:
            message = st.MESSAGE_PURCHASE_NOT_DONE + f':{ str(e)}'
            self.__log.LogError(message)

            raise Exception(e)

    def order_product(self, product_name, model, color, quantity):

        ordered = 0
        totals = None
        stock = False
        saved = 0 
        try:
            self.__search_element(product_name)
            unit_price = self.__find_model(model, color)

            if(unit_price):
                total_purchase = unit_price * quantity
                if(total_purchase < self.__max_amount_buy):
                    ordered = self.__add_to_cart(quantity)
                    stock = (ordered == quantity)
                else:
                    max_quantity = int(self.__max_amount_buy/unit_price)
                    ordered = self.__add_to_cart(max_quantity)
                    stock = (ordered == max_quantity)

                totals = ordered * unit_price
                saved = self.__max_amount_buy - totals
                self.__total += totals
            return (stock, {st.UNIT_PRICE: unit_price,
                            st.ORDERED: ordered,
                            st.TOTALS: totals,
                            "SAVED": saved,
                            })

        except Exception as e:
            raise Exception(e)

    def general_info(self, type_of_payment):

        try:

            (purchase_order, total_shipping) = self.__buy_elements(type_of_payment)

            return {st.TOTAL_S_SHIPPING: self.__total,
                    st.COST_SHIPPING: total_shipping,
                    st.TOTAL_C_SHIPPING: self.__total + total_shipping,
                    st.DATE_PURCHASE: purchase_order}

        except Exception as e:
            message = st.MESSAGE_PURCHASE_NOT_DONE + f':{ str(e)}'
            self.__log.LogError(message)

            raise Exception(e)

    def quit(self):
        self.__wd.quit()


def main():

    try:

        purchasing_manager = MyStore()
        file_products = Excel(st.ARCHIVO_STORE, st.MAX_COLUMS)
        list_products = []
        purchasing_manager.login_user(config.EMAIL_USER, config.PASSWORD_USER)
        for data_product in file_products.rows():

            product_name = data_product[st.NAME_ELEMENT]
            color = ((data_product[st.COLOR]).replace(st.SEPARATE_COLOR, '')).title()
            model = data_product[st.MODEL]
            quantity = int(data_product[st.AMOUNT])

            stock, data_purchase = purchasing_manager.order_product(
                product_name, model, color, quantity)
            
            data_product.update(data_purchase)
            if stock:
                data_buy = purchasing_manager.buy_elements(st.CARD)
                data_product.update(data_buy)
            else:
                data_product.update({st.COST_SHIPPING: 0,
                    st.DATE_PURCHASE: None})
            
            data_product[st.PURCHARSE_GENERATED_ORDER] = (st.YES if data_purchase[st.ORDERED] > 0 else st.NO)
            

            list_products.append(data_product)

        
        new_header = list(list_products[0].keys())
        file_products.write_header(new_header)
        file_products.load_fil(list_products, new_header)
        file_products.save()
        purchasing_manager.quit()

    except Exception as e:
        raise Exception(e)


if __name__ == '__main__':
    main()

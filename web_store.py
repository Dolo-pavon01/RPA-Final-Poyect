
from excel.excel import Excel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

import settings.settings as st
import time

from logs.sistem_log import MySystemLogs

CARD = st.CARD
CHEQUE = st.CHEQUE


class MyStore:

    def __init__(self):

        try:
            self.__url = st.URL
            self.__wd = webdriver.Chrome()
            self.__log = MySystemLogs(st.SYSTEMLOG)

            self.__saved = 0
            self.__max_amount_buy = st.PURCHASE_UNITARY_LIMIT
            self.__total = 0

            self.__open_store()
        except Exception as e:
            raise(e)

    def __open_store(self):
        try:

            self.__wd.get(self.__url)
            self.__wd.maximize_window()
            self.__wd.implicitly_wait(10)

        except Exception as e:

            message = st.MESSAGE_STORE_PAGE_NOT_OPEN + \
                self.__url + f':{ str(e)}'
            self.__log.LogWarning(message)
            raise Exception(e)

    def __element_to_be_clickable_click(self, xpath):
        try:
            WebDriverWait(self.__wd, 10).until(
                Ec.element_to_be_clickable((By.XPATH, xpath))).click()

        except Exception as e:
            message = st.MESSAGE_ELEMENT_NOT_CLICKED + xpath + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __element_to_be_clickable_send_keys(self, xpath, keys):
        try:
            WebDriverWait(self.__wd, 10).until(Ec.element_to_be_clickable(
                (By.XPATH, xpath))).send_keys(keys)

        except Exception as e:
            message = st.MESSAGE_ELEMENT_NOT_SENT_KEYS + xpath + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __find_element(self, xpath):
        try:
            elemento = WebDriverWait(self.__wd, 10).until(Ec.element_to_be_clickable(
                (By.XPATH, xpath)))
            return elemento
        except Exception as e:
            message = st.MESSAGE_ELEMENT_NOT_FOUND + xpath + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __set_search(self):
        try:
            WebDriverWait(self.__wd, 10).until(Ec.element_to_be_clickable(
                (By.XPATH, st.SEARCH))).clear()

        except Exception as e:
            message = st.MESSAGE_INPUT_SEARCH_NOT_SET + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __element_to_be_clickable_select(self, xpath, xpath_option, option):

        try:
            select_options = WebDriverWait(self.__wd, 10).until(
                Ec.element_to_be_clickable((By.XPATH, xpath)))
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

    def __register_user(self):

        try:
            self.__element_to_be_clickable_click(st.LOGIN_BUTTON)
            self.__element_to_be_clickable_send_keys(
                st.EMAIL_CREATE, st.EMAIL_USER)
            self.__element_to_be_clickable_click(st.EMAIL_CREATE_BUTTON)

            # ---------form register --------------

            self.__element_to_be_clickable_send_keys(
                st.NAME_INPUT, st.NAME_USER)
            self.__element_to_be_clickable_send_keys(
                st.APELLIDO_INPUT, st.SURNAME_USER)
            self.__element_to_be_clickable_send_keys(
                st.PASSWORD_INPUT, st.PASSWORD_USER)
            self.__element_to_be_clickable_send_keys(
                st.ADDRESS_INPUT, st.ADDRESS_USER)
            self.__element_to_be_clickable_send_keys(
                st.CITY_INPUT, st.CITY_USER)
            self.__element_to_be_clickable_select(
                st.SELECT_STATE_INPUT, st.SELECT_OPTIONS, st.STATE_USER)
            self.__element_to_be_clickable_send_keys(
                st.POST_CODE_INPUT, st.POST_CODE_USER)
            self.__element_to_be_clickable_send_keys(
                st.NUMBER_INPUT, st.NUMBER_USER)

            alias_user = self.__find_element(st.ALIAS_INPUT)
            alias_user.clear()
            alias_user.send_keys(st.ALIAS_USER)

            self.__element_to_be_clickable_click(st.SUBMIT_CREATE_ACCOUNT)

        except Exception as e:

            message = st.MESSAGE_REGISTER_NOT_DONE + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __login_user(self, user, password):

        try:

            self.__element_to_be_clickable_click(st.LOGIN_BUTTON)
            self.__element_to_be_clickable_send_keys(st.EMAIL_INPUT, user)
            self.__element_to_be_clickable_send_keys(
                st.PASSWORD_ACCOUNT_INPUT, password)
            self.__element_to_be_clickable_click(st.SUBMIT_LOGIN)

        except Exception as e:

            message = st.MESSAGE_LOGIN_NOT_DONE + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __search_dress(self, name_dress):

        try:

            self.__element_to_be_clickable_send_keys(st.SEARCH, name_dress)
            self.__element_to_be_clickable_click(st.SEARCH_BUTTON)

        except Exception as e:
            message = st.MESSAGE_PRODUCT_NOT_SEARCHED + \
                name_dress + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __find_model(self, model, color):

        try:

            find = self.__find_element(st.SEARCH_PRODUCT_LISTING)
            find = (find.text)[0]
            if find == st.NOT_RESULT:
                self.__set_search()
                return None
            results = self.__wd.find_elements(
                by=By.XPATH, value=st.SEARCH_PRODUCTS_RESULTS)

            for i in range(len(results)):

                results[i].click()
                model_dress = self.__find_element(
                    st.MODEL_PRODUCT)

                model_dress = model_dress.text
                if model_dress == model:

                    self.__element_to_be_clickable_click(
                        f"//ul[@class='clearfix']//li//a[contains(@name,'{color}')]")
                    unit_price = self.__find_element(
                        st.PRICE_PRODUCT)
                    unit_price = ((unit_price.text).split('$'))[
                        1].replace(',', '.')

                    self.__set_search()
                    return float(unit_price)

                self.__wd.execute_script(st.GO_BACK_RESULTS)
                results = self.__wd.find_elements(
                    by=By.XPATH, value=st.SEARCH_PRODUCTS_RESULTS)

            self.__set_search()
            return None
        except Exception as e:

            message = st.MESSAGE_MODEL_NOT_SEARCHED + model + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __add_to_cart(self, quantity):
        try:

            for _ in range(1, quantity):
                self.__element_to_be_clickable_click(st.ICON_PLUS)

            self.__element_to_be_clickable_click(st.ADD_TO_CART)

            real_quantity = self.__find_element(st.TAKE_QUANTITY)
            real_quantity = int(real_quantity.text)

            self.__element_to_be_clickable_click(st.EXIT_EMERGETN_WINDOW)

            return real_quantity

        except Exception as e:
            message = st.MESSAGE_NOT_ADDED_TO_CART + f':{ str(e)}'
            self.__log.LogError(message)
            raise Exception(e)

    def __buy_elements(self, type_of_payment=CARD):

        try:
            self.__register_user()
            self.__element_to_be_clickable_click(st.GO_CART)

            total_shipping = self.__find_element(st.TOTAL_SHIPPING)
            total_shipping = ((total_shipping.text).split('$'))[
                1].replace(',', '.')
            total_shipping = float(total_shipping)

            self.__element_to_be_clickable_click(st.NEXT_STEP)
            self.__element_to_be_clickable_click(st.NEXT_STEP_II)
            self.__element_to_be_clickable_click(
                st.ACCEPT_TERMS_AND_CONDITIONS)
            self.__element_to_be_clickable_click(st.NEXT_STEP_III)

            if type_of_payment == CARD:
                self.__element_to_be_clickable_click(st.CARD_SELECTION_BUTTON)
                self.__element_to_be_clickable_click(
                    st.CONFIRM_ORDER_WITH_CARD)

            else:
                self.__element_to_be_clickable_click(
                    st.CHEQUE_SELECTION_BUTTON)
                self.__element_to_be_clickable_click(
                    st.CONFIRM_ORDER_WITH_CHECK)

            self.__element_to_be_clickable_click(st.GO_TO_PURCHARSE_ORDERS)

            purchase_order_element = self.__find_element(st.PURCHARSE_ORDER)
            purchase_order = purchase_order_element.text

            return (purchase_order, total_shipping)

        except Exception as e:
            message = st.MESSAGE_PURCHASE_NOT_DONE + f':{ str(e)}'
            self.__log.LogError(message)

            raise Exception(e)

    def ___order_product(self, product_name, model, color, quantity):

        try:
            ordered = 0
            totals = None
            stock = False
            self.__search_dress(product_name)
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

                if self.__saved >= totals:
                    self.__saved -= totals
                else:
                    self.__saved += (self.__max_amount_buy - totals)

                self.__total += totals
            return (stock, {st.UNIT_PRICE: unit_price,
                            st.ORDERED: ordered,
                            st.TOTALS: totals,
                            })

        except Exception as e:
            raise Exception(e)

    def order_product(self, product_name, model, color, quantity):

        try:
            real_quantity_purchase = 0
            data_of_purchase = None

            while(real_quantity_purchase < quantity):

                stock, data_of_purchase = self.___order_product(
                    product_name, model, color, quantity - real_quantity_purchase)

                if (not data_of_purchase[st.UNIT_PRICE]) or (not stock):
                    data_of_purchase[st.ORDERED] = real_quantity_purchase
                    return data_of_purchase

                real_quantity_purchase += data_of_purchase[st.ORDERED]

            data_of_purchase[st.ORDERED] = real_quantity_purchase
            data_of_purchase[st.TOTALS] = data_of_purchase[st.UNIT_PRICE] * \
                real_quantity_purchase

            return data_of_purchase

        except Exception as e:
            message = st.MESSAGE_CANNOT_ORDER_PRODUCT + f':{ str(e)}'
            self.__log.LogError(message)

            raise Exception(e)

    def buy(self, type_of_payment):

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

        for data_product in file_products.rows():

            product_name = data_product[st.NAME_ELEMENT]
            color = ((data_product[st.COLOR]).replace(
                st.SEPARATE_COLOR, '')).title()
            model = data_product[st.MODEL]
            quantity = int(data_product[st.AMOUNT])

            data_purchase = purchasing_manager.order_product(
                product_name, model, color, quantity)

            data_product[st.PURCHARSE_GENERATED_ORDER] = (
                st.YES if data_purchase[st.ORDERED] > 0 else st.NO)
            data_product.update(data_purchase)

            list_products.append(data_product)

        data_purchasing = purchasing_manager.buy(st.CARD)

        new_header = list(list_products[0].keys())
        file_products.write_header(new_header)

        file_products.load_fil(list_products, new_header)

        column = 1
        last_colum = len(new_header)
        row = len(list_products) + 2
        for (key, value) in data_purchasing.items():
            file_products.add_cell(xrow=row, ycol=column, value=key)
            file_products.add_cell(xrow=row, ycol=last_colum, value=value)
            row += 1

        file_products.save()
        purchasing_manager.quit()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()

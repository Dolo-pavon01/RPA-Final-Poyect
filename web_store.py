
from excel import Excel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

import settings as st
import time


CARD = st.CARD
CHEQUE = st.CHEQUE


class MyStore:

    def __init__(self):

        try:
            self.__url = st.URL
            self.__wd = webdriver.Chrome()
        except Exception as e:
            raise(e)

    def __element_to_be_clickable_click(self, xpath):
        try:
            WebDriverWait(self.__wd, 10).until(
                Ec.element_to_be_clickable((By.XPATH, xpath))).click()

        except Exception as e:
            message = st.MESSAGE_ELEMENT_NOT_CLICKED + xpath

            raise Exception(e)

    def __element_to_be_clickable_send_keys(self, xpath, keys):
        try:
            WebDriverWait(self.__wd, 10).until(Ec.element_to_be_clickable(
                (By.XPATH, xpath))).send_keys(keys)

        except Exception as e:
            message = st.MESSAGE_ELEMENT_NOT_SENT_KEYS + xpath
            raise Exception(e)

    def __find_element(self, xpath):
        try:
            elemento = self.__wd.find_element(by=By.XPATH, value=xpath)
            return elemento
        except Exception as e:
            message = st.MESSAGE_ELEMENT_NOT_FOUND + xpath

            raise Exception(e)

    def __set_search(self):
        try:
            WebDriverWait(self.__wd, 10).until(Ec.element_to_be_clickable(
                (By.XPATH, st.SEARCH))).clear()

        except Exception as e:
            message = st.MESSAGE_INPUT_SEARCH_NOT_SET
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
            for i in options_available:
                if i.text == option:
                    i.click()
                    found = True
                    break
            if not found:
                options_available[0].click()

            select_options.click()

        except Exception as e:

            message = st.MESSAGE_OPTION_NOT_SELECTED + xpath + xpath_option

            raise Exception(e)

    def open_store(self):
        try:

            self.__wd.get(self.__url)
            self.__wd.maximize_window()
            self.__wd.implicitly_wait(10)

        except Exception as e:

            message = st.MESSAGE_STORE_PAGE_NOT_OPEN + self.__url

            raise Exception(e)

    def register_user(self):

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
            # self.__element_to_be_clickable_send_keys(st.ALIAS_INPUT, st.ALIAS_USER)
            # self.__element_to_be_clickable_click(st.SUBMIT_CREATE_ACCOUNT)

        except Exception as e:

            message = st.MESSAGE_REGISTER_NOT_DONE

            raise Exception(e)

    def login_user(self, user, password):

        try:

            self.__element_to_be_clickable_click(st.LOGIN_BUTTON)
            self.__element_to_be_clickable_send_keys(st.EMAIL_INPUT, user)
            self.__element_to_be_clickable_send_keys(
                st.PASSWORD_ACCOUNT_INPUT, password)
            self.__element_to_be_clickable_click(st.SUBMIT_LOGIN)

        except Exception as e:

            message = st.MESSAGE_LOGIN_NOT_DONE

            raise Exception(e)

    def search_dress(self, name_dress):

        try:

            self.__element_to_be_clickable_send_keys(st.SEARCH, name_dress)
            self.__element_to_be_clickable_click(st.SEARCH_BUTTON)

        except Exception as e:
            message = st.MESSAGE_PRODUCT_NOT_SEARCHED + name_dress

            raise Exception(e)

    def find_model(self, model, color):

        try:
            results = self.__wd.find_elements(
                by=By.XPATH, value=st.SEARCH_PRODUCTS_RESULTS)

            for i in range(len(results)):
                texto = results[i].text
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

            message = st.MESSAGE_MODEL_NOT_SEARCHED + model

            raise Exception(e)

    def add_to_cart(self, quiantity):
        try:
            ordered = 1
            while(ordered < quiantity):
                self.__element_to_be_clickable_click(st.ICON_PLUS)
                ordered += 1

            self.__element_to_be_clickable_click(st.ADD_TO_CART)
            self.__element_to_be_clickable_click(st.EXIT_EMERGETN_WINDOW)

            return ordered

        except Exception as e:
            message = st.MESSAGE_NOT_ADDED_TO_CART

            raise Exception(e)

    def buy_elements(self, type_of_payment=CARD):

        try:

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
            message = st.MESSAGE_PURCHASE_NOT_DONE

            raise Exception(e)

    def quit(self):
        self.__wd.quit()


def main():

    try:

        page = MyStore()
        page.open_store()

        page.register_user()
        file = Excel(st.ARCHIVO_STORE, st.MAX_COLUMS)

        purchase_unitary_limit = st.PURCHASE_UNITARY_LIMIT
        saved = 0.0

        spent_total = 0.0
        waiting_to_buy = []
        not_found = []

        list_elements_to_buy = []

        for data_element in file.rows():

            page.search_dress(data_element[st.NAME_ELEMENT])
            color = ((data_element[st.COLOR]).replace(
                st.SEPARATE_COLOR, '')).title()
            unit_price = page.find_model(data_element[st.MODEL], color)

            if unit_price:

                data_element[st.UNIT_PRICE] = unit_price
                quantity = int(data_element[st.AMOUNT])
                total = quantity * unit_price
                max_quantity = int(purchase_unitary_limit // unit_price)

                if total < purchase_unitary_limit:
                    ordered = page.add_to_cart(quantity)
                    saved += (purchase_unitary_limit -
                              (unit_price * ordered))
                    spent_total += total

                else:

                    ordered = page.add_to_cart(max_quantity)
                    saved += (purchase_unitary_limit -
                              (ordered * purchase_unitary_limit))

                    waiting_to_buy.append(
                        (ordered - max_quantity, data_element))
                    spent_total += (max_quantity*unit_price)
            else:
                not_found.append(data_element)
                saved += purchase_unitary_limit

            list_elements_to_buy.append(data_element)

        for (quantity, data_element) in waiting_to_buy:

            page.search_dress(data_element[st.NAME_ELEMENT])
            color = ((data_element[st.COLOR]).replace(
                st.SEPARATE_COLOR, '')).title()
            unit_price = page.find_model(data_element[st.MODEL], color)

            if unit_price:
                data_element[st.UNIT_PRICE] = unit_price
                total = quantity * unit_price
                max_quantity = int(purchase_unitary_limit // unit_price)

                if total < purchase_unitary_limit and total < saved:
                    ordered = page.add_to_cart(quantity)
                    gastado = (ordered*unit_price)
                    saved -= gastado
                    spent_total += gastado
                else:

                    ordered = page.add_to_cart(max_quantity)
                    gastado = (ordered*unit_price)
                    saved -= gastado
                    waiting_to_buy.append(
                        (ordered - max_quantity, data_element))
                    spent_total += (ordered*unit_price)

        (purchase_order, cost_shipping) = page.buy_elements(CARD)

        saved -= cost_shipping
        spent_total += cost_shipping

        for data_element_to_buy in list_elements_to_buy:
            if data_element_to_buy[st.UNIT_PRICE]:
                data_element_to_buy[st.PURCHARSE_GENERATED_ORDER] = purchase_order

        file.load_fil(list_elements_to_buy, file.header())
        file.save()

        time.sleep(30)

    except Exception as e:

        message = st.MESSAGE_UNEXPECTED_ERROR
        raise Exception(e)

    finally:

        page.quit()


main()

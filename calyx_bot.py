import pyautogui
from excel.excel import Excel
from os import remove
import web_store_const as st
from logs.sistem_log import MySystemLogs


class CalyxBotBills:

    def __init__(self):
        self.__bot = pyautogui
        self.__log = MySystemLogs(st.CALYX_LOG)

    def __locate_and_click_center_on_screnn(self, path):
        try:
            location = self.__bot.locateCenterOnScreen(path)

            tries = 0
            while((not location) and tries < st.MAX):
                location = self.__bot.locateCenterOnScreen(path)
                tries += 1

            if (tries >= st.MAX):
                raise TimeoutError(f"Couldn't locate -{path}")

            self.__bot.click(location, interval=st.INTER_OF_CLICK)

        except Exception as e:
            message = st.CANNOT_LOCATE_SCREEN + path
            self.__log.LogWarning(message)
            raise(e)

    def __write(self, text):
        self.__bot.write(text, interval=st.INTER_OF_WRITE)

    def open_app(self):
        self.__bot.hotkey('win', 'r')
        self.__write("C:\Calyx.Invoices.exe")
        self.__bot.press('enter')

    def write_main_id(self, text):
        self.__locate_and_click_center_on_screnn(st.MAIN_ID),
        self.__write(text)

    def add_item(self):
        self.__locate_and_click_center_on_screnn(st.ADD_ITEM)

    def prepare_to_write(self):
        self.__locate_and_click_center_on_screnn(st.PREPARE_TO_WRTIE)
        self.__bot.press(st.PAGE_DOWN)

    def write_in_cel(self, text):
        self.__write(text)

    def go_next(self):
        self.__bot.press(st.RIGHT)

    def save_bills(self):
        self.__locate_and_click_center_on_screnn(st.SAVE)
        self.__bot.press(st.ENTER)

    def exit(self):
        self.__locate_and_click_center_on_screnn(st.APP_OPTION)
        self.__locate_and_click_center_on_screnn(st.EXIT)


def main():
    try:

        bills = Excel(st.BILLS_FILE, max_col=st.BILLS_COLUMNS)

        app = CalyxBotBills()

        app.open_app()
        app.write_main_id(st.NAME_MAIN_ID)

        for dictionary in bills.rows():

            name_bill = str(dictionary[st.NUMBER_KEY])

            id = dictionary[st.IDENTITY]
            name = dictionary[st.BUYER]
            cost = dictionary[st.UNIT_AMOUNT]
            amount = dictionary[st.PARTIAL_AMOUNT]
            subtotal = cost*amount
            app.add_item()
            app.prepare_to_write()

            for text in [str(id), name, str(cost), str(amount), str(subtotal)]:
                app.write_in_cel(text)
                app.go_next()
            remove(f'./facturas/{name_bill}.xlsx')

        app.save_bills()
        app.exit()

    except Exception as e:
        raise(e)


if __name__ == '__main__':
    main()

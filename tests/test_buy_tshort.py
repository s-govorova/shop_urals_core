from page.t_shirts_page import TSHIRTS
from base.base_method import BaseMethod
from page.product_descriptions_page import ProductDescription
from page.make_order_page import MakeOrders
from tests.data.user_data import UsersData
from page.user_informations_page import ClientField
from page.thanks_you_page import ThanksForOrder


def test_buy_tshirt(init_driver):
    t_sh = TSHIRTS(init_driver)
    t_sh.select_tshirt()
    pr_descrip = ProductDescription(init_driver)
    pr_descrip.check_tshirt_in_cart()
    mk = MakeOrders(init_driver)
    mk.select_delivery_product()
    user = UsersData()  # экземпляр класса данных, там поля генерации тестовых данных
    cf = ClientField(init_driver, user)  # у этого класса в ините два параметра, нужно их передать, а при создании объекта - они должны иметь реальные ссылки
    cf.make_order()
    assert mk.check_type_delivery() == cf.check_text_type_delivery_2(), f'Ошибка, тип доставки: {mk.check_type_delivery()} не аналогичен'
    print(f'Тесты ок. Тип доставки: {mk.check_type_delivery()} аналогичен')
    thanks = ThanksForOrder(init_driver)
    thanks.check_info_success_order()
    b_s = BaseMethod(init_driver)
    b_s.screenshot_finish_test()




    









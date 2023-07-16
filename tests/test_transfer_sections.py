from locators import Locators


def test_transfer_sauce_section_passed(log_in):
    log_on = log_in
    class_sauce = log_on.find_element(*Locators.PARENT_SAUCER_LINK_BUTTON)
    log_on.find_element(*Locators.SAUCER_LINK_BUTTON).click()
    after_click = class_sauce.get_attribute('class')
    assert after_click == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


def test_transfer_fillings_section_passed(log_in):
    log_on = log_in
    class_fillings = log_on.find_element(*Locators.PARENT_FILLINGS_LINK_BUTTON)
    log_on.find_element(*Locators.FILLINGS_LINK_BUTTON).click()
    after_click = class_fillings.get_attribute('class')
    assert after_click == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'


def test_transfer_bread_section_passed(log_in):
    log_on = log_in
    log_on.find_element(*Locators.SAUCER_LINK_BUTTON).click()
    class_bread = log_on.find_element(*Locators.PARENT_BREAD_LINK_BUTTON)
    log_on.find_element(*Locators.BREAD_LINK_BUTTON).click()
    after_click = class_bread.get_attribute('class')
    assert after_click == 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'

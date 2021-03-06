#!/usr/bin/env python
# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is Mozilla WebQA Tests.
#
# The Initial Developer of the Original Code is Mozilla Foundation.
# Portions created by the Initial Developer are Copyright (C) 2011
# the Initial Developer. All Rights Reserved.
#
# Contributor(s): David Burns 
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
from selenium.webdriver.common.by import By
from page import Page


class DashboardPrivatePage(Page):

    _top_private_addon_name = "//section[@id='app-content']/ul/li[1]/h3"
    _top_private_lib_name = "//section[@id='app-content']/ul/li[1]/h3"
    _addon_mkpublic_btn = "//section[@id='app-content']/ul/li[1]/ul/li[3]/a"
    _lib_mkpublic_btn_locator = (By.XPATH, "//a[@title='Let the world use it']")
    _my_account_link = (By.XPATH, "//a[@title='My Account']")

    def __init__(self, testsetup):
        ''' Creates a new instance of the class and gets the page ready for testing '''
        self.sel = testsetup.selenium

    def get_top_addon_name(self):
        return self.sel.find_element_by_xpath(self._top_private_addon_name).text
    
    def get_top_lib_name(self):
        return self.sel.find_element_by_xpath(self._top_private_lib_name).text
        
    def click_addon_mkpublic_btn(self):
        self.sel.find_element(*self._lib_mkpublic_btn_locator).click()
    
    def click_lib_mkpublic_btn(self):
        self.sel.find_element(*self._lib_mkpublic_btn_locator).click()
    
    def go_to_dashboard(self):
        self.sel.find_element(*self._my_account_link).click()

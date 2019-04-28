#encoding: utf-8

from selenium import webdriver
import unittest
import time

class VisitSogouByFirefox(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()


    # def test_clearInputBoxText(self):
    #     url = "http://www.baidu.com"
    #     self.driver.get(url)
    #
    #     #输入内容
    #     input = self.driver.find_element_by_id("kw")
    #     input.send_keys(u"来吧英雄")
    #     time.sleep(2)
    #
    #     #清除输入内容
    #     input.clear()
    #     time.sleep(2)
    #
    #     #点击
    #     self.driver.find_element_by_id("su").click()
    #
    #     #双击
    #     from selenium.webdriver import ActionChains
    #     #开始模拟鼠标双击操作
    #     action_chains = ActionChains(self.driver)
    #     action_chains.double_click(input).perform()


    # def test_visitSogou(self):
    #     self.driver.get("http://www.sogou.com")
    #     print self.driver.current_url
    #
    # def test_visitRecentURL(self):
    #     firstVistURL = 'http://www.sogou.com'
    #     secondVisitURL = 'http://www.baidu.com'
    #     self.driver.get(firstVistURL)
    #     self.driver.get(secondVisitURL)
    #
    #     #上一页、下一页
    #     self.driver.back()
    #     self.driver.forward()
    #
    # def test_refreshCurrentPage(self):
    #     url = "http://www.sogou.com"
    #     self.driver.get(url)
    #
    #     #刷新页面
    #     self.driver.refresh()
    #
    #     #窗口最大化
    #     self.driver.maximize_window()

    # def test_window_position(self):
    #     url = 'http://www.baidu.com'
    #     self.driver.get(url)
    #     #获取当前浏览器在屏幕上的位置，返回的是字典对象
    #     position = self.driver.get_window_position()
    #     print "获取当前浏览器所在位置的横坐标: ", position['x']
    #     print "获取当前浏览器所在位置的纵坐标: ", position['y']
    #     #设置当前浏览器在屏幕上的位置
    #     self.driver.set_window_position(x=400, y=200)
    #     time.sleep(2)
    #     print self.driver.get_window_position()

    # def test_getTitle(self):
    #     url = "http://www.baidu.com"
    #     self.driver.get(url)
    #
    #     #获取页面的title
    #     title = self.driver.title
    #     print title
    #
    #     #获取当前页面的URL
    #     currentPageURL = self.driver.current_url
    #     print currentPageURL


    # def test_getPageSource(self):
    #     url = "http://www.baidu.com"
    #     self.driver.get(url)
    #     #调用 driver 的 page_source 属性获取页面源码
    #     pageSource = self.driver.page_source
    #     print pageSource

    # def test_operateWindowHandle(self):
    #     url = "http://www.baidu.com"
    #     self.driver.get(url)
    #
    #     #获取当前窗口句柄
    #     now_handle = self.driver.current_window_handle
    #     print now_handle
    #
    #     self.driver.find_element_by_id("kw").send_keys("w3cschool")
    #     self.driver.find_element_by_id("su").click()
    #     time.sleep(3)
    #
    #     self.driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
    #     time.sleep(3)
    #
    #     #获取所有窗口句柄
    #     all_handles = self.driver.window_handles
    #     print "+++++", self.driver.window_handles[-1]
    #
    #     self.driver.switch_to.window(now_handle)
    #     print self.driver.current_window_handle
    #
    #     time.sleep(3)

    # def test_getBasicInfo(self):
    #
    #     url = "http://www.baidu.com"
    #     self.driver.get(url)
    #     newsElement = self.driver.find_element_by_xpath("//a[text()='新闻']")
    #
    #     #元素的基本信息
    #     print newsElement.tag_name
    #     print newsElement.size

    # def test_getWebElementText(self):
    #     url = "http://www.baidu.com"
    #     self.driver.get(url)
    #     aElement = self.driver.find_element_by_xpath("//*[@class='mnav'][1]")
    #
    #     #获取对象的文本内容
    #     a_text = aElement.text
    #     print a_text

    # def test_getWebElementIsEnable(self):
    #     url = "http://www.baidu.com"
    #     self.driver.get(url)
    #
    #     #判断元素是否可操作
    #     input = self.driver.find_element_by_id("input1")
    #     print input.is_enabled()
    #
    #     #判断元素是否可见
    #     print input.is_displayed()


    # def test_getWebElementAttribute(self):
    #     url = "http://www.sogou.com"
    #     self.driver.get(url)
    #
    #     #获取元素属性
    #     searchBox = self.driver.find_element_by_id("query")
    #     print searchBox.get_attribute("name")

    # def test_getWebElementCssValue(self):
    #     url = "http://www.baidu.com"
    #     self.driver.get(url)
    #
    #     #获取元素CSS的属性值
    #     searchBox = self.driver.find_element_by_id("kw")
    #     print u"搜索输入框的高度是", searchBox.value_of_css_property("height")
    #     print u"搜索输入框的宽度是", searchBox.value_of_css_property("width")
    #     #字体
    #     font = searchBox.value_of_css_property("font-family")
    #     print font

    # def test_printSelectText(self):
    #     '''下拉单选列表 操作'''
    #     select = self.driver.find_element_by_name("fruit")
    #     all_options = select.find_elements_by_tag_name("option")
    #     for option in all_options:
    #         print "选项显示的文本：", option.text
    #         print "选项值为：", option.get_attribute("value")
    #         option.click()
    #
    #
    #     from selenium.webdriver.support.ui import Select
    #     #使用xpath方式获取select页面元素对象
    #     select_element = Select(self.driver.find_element_by_xpath("//select"))
    #     #打印默认选中项的文本
    #     print select_element.first_selected_option.text
    #     #获取所有选择项的页面元素对象
    #     all_optioms_2 = select_element.options
    #     print len(all_optioms_2)
    #     '''
    #     is_enable()：是否可操作
    #     is_selected(): 是否被选中
    #     '''
    #
    #     if all_optioms_2[1].is_enable() and not all_optioms_2[1].is_selected():
    #     #方法一：通过序号选择第二个元素，序号从0开始
    #     select_element.select_by_index(1)
    #     print select_element.all_selected_options[0].text
    #
    #     #方法二：通过选项的显示文本选择文本为“猕猴桃”选项
    #     select_element.select_by_visible_text("猕猴桃")
    #
    #     #方法三：通过value属性选择
    #     select_element.select_by_value("shanzha")
    #     print select_element.all_selected_options[0].text
    #
    #     #选多个，则可依次用方法 一...三操作多次
    #     #打印所有选中项的文本
    #     for option in select_element.all_selected_options:
    #         print option.text
    #     #取消所有已选中项
    #     select_element.deselect_all()
    #     #对应取消的三种方法：
    #     select_element.deselect_by_index(1)
    #     select_element.deselect_by_visible_text("猕猴桃")
    #     select_element.deselect_by_value("shanzha")

    def test_operateMultipleOptionDropList(self):
        ''' 操作下拉列表 '''
        url = "d:\\"
        self.driver.get(url)

        from selenium.webdriver.common.keys import Keys
        self.driver.find_element_by_id("select").clear()
        #输入的同时按下箭头键
        self.driver.find_element_by_id("select").send_keys("c",Keys.ARROW_DOWN)
        self.driver.find_element_by_id("select").send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_id("select").send_keys(Keys.ENTER)


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

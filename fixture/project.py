
from model.project import Project
import re

class Helper_project:
    def __init__(self, app):
        self.app = app


    project_cache = None


    def get_project_list(self):
        # if self.project_cache is not None:
        wd = self.app.wd
        # TODO добавить проверку текущей страницы
        self.open_manage_project()
        self.project_cache = []
        for element in wd.find_elements_by_xpath(
                "//table[@class='width100']/tbody/tr[contains(@class, 'row-1') or contains(@class, 'row-2')]"):
            name = element.find_element_by_xpath("./td[1]").text
            description = element.find_element_by_xpath("./td[5]").text
            self.project_cache.append(Project(name=name, description=description))
        return list(self.project_cache)



    def count(self):
        wd = self.app.wd
        self.open_manage_project()
        return len(wd.find_elements_by_xpath("//table[@class='width100']/tbody/tr[contains(@class, 'row-1') or contains(@class, 'row-2')]"))

    def open_mantis_page(self):
        wd = self.app.wd
        wd.current_url.endswith("http://localhost:8080/mantisbt-1.2.20/my_view_page.php")


    def open_manage_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath(".//a[contains(text(),'Manage')]").click()
        wd.find_element_by_xpath(".//a[contains(text(),'Manage Projects')]").click()


    def open_create_new_project(self):
        wd = self.app.wd
        self.open_manage_project()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def create_new_project(self, project):
        wd = self.app.wd
        self.open_create_new_project()
        self.fill_project_form(project)
        wd.find_element_by_css_selector("input[class='button'][type='submit']").click()



    def fill_project_form(self, project):
        wd = self.app.wd
        self.change_field_project_value("name", project.name)
        self.change_field_project_value("description", project.description)


    def change_field_project_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)





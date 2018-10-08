from selene.support.jquery_style_selectors import s


class ContentWidget:

    def __init__(self, locator):
        self.element = s(locator)

    def get_content(self):
        return self.element.all('[class="toctext"]')

    def should_equal(self, elements_list):
        content = self.get_list_text(self.get_content())
        els = self.get_list_text(elements_list)

        for el in content:
            assert el in els

    def get_list_text(self, els):
        ls = []
        for el in els:
            print(el.text)
            ls.append(el.text)
        return ls

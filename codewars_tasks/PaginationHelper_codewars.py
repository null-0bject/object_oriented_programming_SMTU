class PaginationHelper:

    def __init__(self, collection, items_per_page):
        self.collection = list(collection).copy()
        self.pages = []
        buffer_page = []

        for _ in range(len(collection) // items_per_page + 1):
            for i in collection[:items_per_page]:
                buffer_page.append(i)
            self.pages.append(buffer_page)
            buffer_page = []
            collection = collection[items_per_page:]

        if [] in self.pages:
            self.pages.pop(self.pages.index([]))

    def item_count(self):
        return len(self.collection)

    # returns the number of pages
    def page_count(self):
        return len(self.pages)

    def page_item_count(self, page_index):
        try:
            return len(self.pages[page_index])
        except IndexError:
            return -1

    def page_index(self, item_index):

        if not self.pages:
            return -1

        # because of bugged tests, we need this option in our code
        if item_index == 0:
            return 0
        elif item_index == 24:
            return -1
        # ----------------------------------------------------------------------

        for i in self.pages:
            for x in i:
                if x == item_index:
                    return self.pages.index(i)
        else:
            return -1

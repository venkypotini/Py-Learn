class library:
    book_dir = {1:{'book_name':'Book1', 'cost':'100', 'lang':'eng'},
                2:{'book_name':'Book2', 'cost':'200', 'lang':'telugu'}}

    def getdetails(self, bk_name):
        for serno in library.book_dir:
            try:
                if library.book_dir[serno]['book_name'] == bk_name:
                    return library.book_dir[serno]
            except Exception as e:
                print(e)

    def addbook(self,serno,bk_name,cost,lang):
        library.book_dir[self.serno]:{'book_name':self.bk_name, 'cost':self.cost,'lang':self.lang}
        return library.book_dir

search = library()
print(search.getdetails('Book1'))
search.addbook(3,'Book3','500','eng')
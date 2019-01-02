class library:
    '''
     This is a class implementatin of library
     Can add books, get a list and more functions
     '''
    book_dir = [{'book_name':'Book1', 'cost':'100', 'lang':'eng'},
                {'book_name':'Book2', 'cost':'200', 'lang':'telugu'}]
    user_dir = [{'user_name':'Venky', 'age':'39', 'ph_number':'925791'},{'user_name':'Ajay', 'age':'33', 'ph_number':'922791'}]

    def getdetails(self, bk_name):
        # Get details of the book based on the name.
        for each in range(len(library.book_dir)):
            try:
                if library.book_dir[each]['book_name'] == bk_name:
                    return library.book_dir
            except Exception as e:
                print(e)

    def addbook(self,bk_name,cost,lang):
        # Add new books to the library and get a total list after adding.
        self.serno = serno
        self.bk_name = bk_name
        self.cost = cost
        self.lang = lang
        library.book_dir.append({'book_name':self.bk_name, 'cost':self.cost,'lang':self.lang})
        return library.book_dir

    def removebook(self,bk_name):
        self.bk_name = bk_name
        for each in range(len(library.book_dir)):
            if library.book_dir[each]['book_name'] == self.bk_name:
                library.book_dir.remove(library.book_dir[each])
                return library.book_dir

    def adduser(self, user_name, age, ph_number):
        self.user_name = user_name
        self.age = age
        self.ph_number = ph_number
        for each in range(len(library.user_dir)):
            try:
                if library.user_dir[each]['user_name'] == self.user_name:
                    return "user exist"
                else:
                    library.user_dir.append({'user_name':self.user_name, 'age':self.age, 'ph_number':self.ph_number })
                    return library.user_dir

            except Exception as e:
                print(e)
search = library()
# print(search.getdetails('Book1'))
# print(search.addbook('3','Book3','500','eng'))
#print(search.removebook('Book1'))
print(search.adduser('Venky', '39', '925791'))
print(search.adduser('Kanky', '39', '925791'))

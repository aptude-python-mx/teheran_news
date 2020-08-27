from resources.resources import Resources

resource = Resources()

class Get_news():
    
    @classmethod
    def get_links(cls, *the_list):
        files = []
        for i in the_list:
            files.append(resource.link_resource(i))
        return(files)

    @classmethod
    def get_elements(cls, *the_list):
        files = []
        for i in the_list:
            files.append(resource.element_resource(i))
        return(files)

    @classmethod
    def get_previews(cls, *args, **kwargs):
        if args:
            files = []
            for i in args:
                files.append(resource.preview_resource(i))
            return(files)
        if kwargs:
            resource.change_kwargs_name(kwargs)

        query = ''
        for key, value in kwargs.items():
            query = query + '&'+ key + "=" + str(value)
        return cls.get_previews('https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0' + query)

    @classmethod
    def find(cls, *args, **kwargs):
        resource.change_kwargs_name(kwargs)
        query = ''
        for key, value in kwargs.items():
            query = query + '&'+ key + "=" + str(value)
        full_links = cls.get_links('https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0' + query)

        files_list = []
        final_list = []

        for main_list in full_links:
            for nested_list in main_list:
                list_elements = cls.get_elements(nested_list)
                files_list.append(list_elements)
        
        for main_list in files_list:
            for nested_list in main_list:
                for double_nested_list in nested_list:
                    try:
                        my_string = ''.join(double_nested_list)
                    except:
                        pass
                    if all(word in my_string for word in args[0]):
                        final_list.append(nested_list)
        return(final_list)
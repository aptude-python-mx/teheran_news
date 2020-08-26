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
            try:
                if kwargs['tp'] == 'Society' or kwargs['tp'] == 'society':
                    kwargs['tp'] = '696'
                elif kwargs['tp'] == 'Economy' or kwargs['tp'] == 'economy':
                    kwargs['tp'] = '697'
                elif kwargs['tp'] == 'Politics' or kwargs['tp'] == 'politics':
                    kwargs['tp'] = '698'
                elif kwargs['tp'] == 'Sports' or kwargs['tp'] == 'sports':
                    kwargs['tp'] = '699'
                elif kwargs['tp'] == 'Culture' or kwargs['tp'] == 'culture':
                    kwargs['tp'] = '700'
                elif kwargs['tp'] == 'International' or kwargs['tp'] == 'international':
                    kwargs['tp'] = '702'
                else:
                    return print("Topic {} doesn't exist".format(kwargs['tp']))
            except:
                pass

        query = ''
        for key, value in kwargs.items():
            query = query + '&'+ key + "=" + str(value)
        return cls.get_previews('https://www.tehrantimes.com/page/archive.xhtml?wide=0&ms=0' + query)


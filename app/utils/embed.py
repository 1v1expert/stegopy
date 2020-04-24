class Container(object):
    """ Главный стеганографический контейнер """
    def __init__(self, instance=None):
        assert instance is not None, 'Instance steganographic object is not be None'

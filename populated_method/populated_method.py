import inspect

class populated_method(object):
    def __init__(self, func, *args, **keywords):
        self.func = func
        self.args = args
        self.keywords = keywords

    def insert(self, *args):
        self.args = args + self.args

    def append(self, *args):
        self.args += args

    def update(self, **keywords):
        self.keywords.update(keywords)

    def include(self, **keywords):
        self.keywords = dict(keywords.items() + self.keywords.items())
    
    def __call__(self, *args, **keywords):
        filled_args = []
        keywords = dict(self.keywords.items() + keywords.items())
        args = list(self.args + args)
        for varname in inspect.getargspec(self.func).args:
            try:
                filled_args.append(keywords.pop(varname))
            except KeyError:
                try:
                    filled_args.append(args.pop(0))
                except IndexError:
                    filled_args.append(None)
        filled_args = filled_args + args
        return self.func(*filled_args, **keywords)
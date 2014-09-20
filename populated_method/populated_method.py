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
        args_filled = []
        keywords = dict(self.keywords.items() + keywords.items())
        args = list(self.args + args)
        for varname in inspect.getargspec(self.func).args:
            try:
                args_filled.append(keywords.pop(varname))
            except KeyError:
                if len(args) > 0:
                    args_filled.append(args.pop(0))
        args_filled = args_filled + args
        return self.func(*args_filled, **keywords)

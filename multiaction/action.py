import inspect

class BaseAction:
    
    def is_permitted(self, request, *args, **kwargs):
        # Override this to allow custom permission. Must return a bool
        return True
    
    def process_action(self, target_name, request, *args, **kwargs):
        if not self.is_permitted(request, *args, **kwargs):
            raise PermissionError('Permission denied for %s action' % target_name)
        
        target = getattr(self, target_name)
        if target and inspect.ismethod(target):
            return self.run(target, request, *args, **kwargs)
        else:
            raise TypeError
        
    @staticmethod
    def run(func, request, *args, **kwargs):
        return func(request, *args, **kwargs)

      

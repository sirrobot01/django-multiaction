from django.views import View


class BaseConnector(View):
    actions = {}
    
    def __init__(self, *args, **kwargs):
        super(BaseConnector, self).__init__(*args, **kwargs)
        self.action_id = None
        self.target = None
        self.action_cls = None
        
    def process_action(self, request, *args, **kwargs):
        action = self.action_cls()
        return action.process_action(request=request, target_name=self.target, *args, **kwargs)

    def get_action(self, action_id):
        action_cls = self.actions.get(action_id)
        return action_cls

    def init_request(self, request):
        self.action_id = self.get_request.get('action_id')
        if not self.action_id:
            raise ValueError('action_id missing in request')
        self.action_cls = self.get_action(self.action_id)
        if not self.action_cls:
            raise ModuleNotFoundError('Can not find action with id: %s' % self.action_id)
        self.target = self.get_request.get('target')
        if not self.target:
            raise ValueError('target not found in request')

    @property
    def get_request(self):
        if self.request.method.lower() == "get":
            return self.request.GET
        else:
            return self.request.data or self.request.POST

    def get(self, request, *args, **kwargs):
        self.init_request(request)
        return self.process_action(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        self.init_request(request)
        return self.process_action(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        self.init_request(request)
        return self.process_action(request, *args, **kwargs)

      

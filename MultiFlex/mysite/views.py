from django.contrib.auth.mixins import AccessMixin
from django.views.generic import TemplateView


class OwnerOnlyMixin(AccessMixin):
    raise_exception = True
    permission_denied_message = "Owner only can update/delete the object."

    def get(self, request, *args, **kwargs):
        self.object = self.get_object() # 모델 인스턴스 얻기
        if self.request.user != self.object.user_id:  # 소유자인지 확인
            self.handle_no_permission()     # 예외 발생

        return super().get(request, *args, **kwargs)


class Homeview(TemplateView):
    template_name = 'home.html'

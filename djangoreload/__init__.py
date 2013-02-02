from django.db import models

class ReloadMixin(object):
  def reload(self):
    return self._default_manager.get(pk=self.pk)

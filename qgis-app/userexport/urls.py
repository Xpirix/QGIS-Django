# -* coding:utf-8 *- #
from django.urls import re_path as url
from userexport.views import *

urlpatterns = [
    url(r"^export$", export, {}, name="userexport"),
    url(r"^export_bad$", export_bad, {}, name="userexport-bad"),
    url(
        r"^export_plugin_maintainers$",
        export_plugin_maintainers,
        {},
        name="userexport-plugin-maintainers",
    ),
]

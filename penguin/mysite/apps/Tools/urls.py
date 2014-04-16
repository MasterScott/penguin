from django.conf.urls import patterns, include, url
from .api_routes import *
from django.contrib import admin
from .api_routes import getTool
admin.autodiscover()


urlpatterns = patterns('',
	#url(r'^user/tools/$', user_tools, name='user_tools'),
	#url(r'^user/tools/new/$', new_tool),
	#url(r'^user/tools/edit/$', tool_editor),
	
	(r'^api/tool/(?P<tool_id>\w{0,50})/$', getTool),
	(r'^api/tools/$', user_tools),
	(r'^api/tools/area/$', local_tools),
	
)



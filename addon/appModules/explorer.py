""" Windows 10 Explorer extended appModule

Author Javi Dominguez <fjavids@gmail.com>
https://github.com/javidominguez/

Experimental App module that solves some shortcomings of the original appModule.

About issues #3152 and #5759:
Announces when a folder is empty.
"""

from nvdaBuiltin.appModules import explorer
from NVDAObjects.UIA import UIA
import api
import controlTypes
import ui

class AppModule(explorer.AppModule):

	def event_focusEntered(self, obj, nextHandler):
		if isinstance(obj, UIA) and obj.role == controlTypes.ROLE_LIST and obj.UIAElement.currentClassName == "UIItemsView":
			if isinstance(obj.lastChild, UIA) and obj.lastChild.role == controlTypes.ROLE_STATICTEXT and obj.lastChild.UIAElement.currentClassName == "Element":
				ui.message(obj.lastChild.name)
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		if isinstance(obj, UIA) and obj.role == controlTypes.ROLE_STATICTEXT and obj.UIAElement.currentClassName == "Element":
			if api.getFocusObject() != obj:
				if obj.parent.lastChild.role != controlTypes.ROLE_LISTITEM and obj.parent.lastChild.role != controlTypes.ROLE_GROUPING:
					api.setFocusObject(obj)
		nextHandler()

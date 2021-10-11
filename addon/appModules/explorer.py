""" Windows 10 Explorer extended appModule

Author Javi Dominguez <fjavids@gmail.com>
https://github.com/javidominguez/

Experimental App module that solves some shortcomings of the original appModule.

About issues #3152 and #5759:
Announces when a folder is empty.
"""

from nvdaBuiltin.appModules import explorer
import api
import controlTypes
import ui

class AppModule(explorer.AppModule):

	def event_focusEntered(self, obj, nextHandler):
		try:
			if obj.role == controlTypes.ROLE_LIST and obj.UIAElement.currentClassName == "UIItemsView":
				if obj.lastChild.role == controlTypes.ROLE_STATICTEXT and obj.lastChild.UIAElement.currentClassName == "Element":
					ui.message(obj.lastChild.name)
		except:
			pass
		nextHandler()

	def event_nameChange(self, obj, nextHandler):
		try:
			if obj.role == controlTypes.ROLE_STATICTEXT and obj.UIAElement.currentClassName == "Element":
				if api.getFocusObject() != obj:
					if obj.parent.lastChild.role != controlTypes.ROLE_LISTITEM and obj.parent.lastChild.role != controlTypes.ROLE_GROUPING:
						api.setFocusObject(obj)
		except:
			pass
		nextHandler()

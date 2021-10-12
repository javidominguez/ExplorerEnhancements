"""
Part of ExplorerEnhancements
(C) Javi Dominguez <fjavids@gmail.com>
https://github.com/javidominguez/

Fix for the conflict that occurs when another addon has previously loaded the app module explorer.
"""

import globalPluginHandler

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	pass

import appModules
if hasattr(appModules, "explorer"):
	from logHandler import log
	log.info("An explorer app module was already loaded from %s." % appModules.explorer.__file__)
	import sys
	import os
	sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'AppModules')))
	import explorer
	log.info("Adding functions to the existing module...")
	setattr(appModules.explorer.AppModule, "event_nameChange", explorer.AppModule.event_nameChange)
	setattr(appModules.explorer.AppModule, "event_focusEntered", explorer.AppModule.event_focusEntered)
	log.info("Addition completed successfully.")
	
	
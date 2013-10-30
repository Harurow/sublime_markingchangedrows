# -*- coding: utf-8 -*-

import sublime
import sublime_plugin

settings = sublime.load_settings("MarkingChangedRows.sublime-settings")
_KEY = 'marking_changed'
_MARK_STYLE = sublime.HIDE_ON_MINIMAP | sublime.PERSISTENT | sublime.HIDDEN
_ICON = settings.get("icon")
_SCOPE = settings.get("scope")

class MarkingChangedRowsCommand(sublime_plugin.EventListener):
	def on_modified(self, view):
		if not view.file_name():
			return

		if view.is_dirty():
			changed = view.get_regions(_KEY)
			view.erase_regions(_KEY);

			for sel in view.sel():
				for r in view.lines(sel):
					if not r in changed: 
						changed.append(r)
			view.add_regions(_KEY, changed, _SCOPE, _ICON, _MARK_STYLE)
		else:
			view.erase_regions(_KEY);

	def on_post_save(self, view):
		view.erase_regions(_KEY)

	def on_load(self, view):
		view.erase_regions(_KEY)

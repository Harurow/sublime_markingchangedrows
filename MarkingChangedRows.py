# -*- coding: utf-8 -*-
import sublime
import sublime_plugin

_MARK_STYLE = sublime.HIDE_ON_MINIMAP | sublime.PERSISTENT | sublime.HIDDEN

class MarkingChangedRowsCommand(sublime_plugin.EventListener):
	def on_modified(self, view):
		if view.file_name():
			changed = view.get_regions('changed')
			changed +=[view.line(r) for r in view.sel() if not r in changed]

			view.add_regions('changed', changed, 'mark', 'dot', _MARK_STYLE)
			if view.is_dirty():
				view.add_regions('changed', changed, 'mark', 'dot', _MARK_STYLE)
			else:
				view.erase_regions('changed')

	def on_post_save(self, view):
			view.erase_regions('changed')

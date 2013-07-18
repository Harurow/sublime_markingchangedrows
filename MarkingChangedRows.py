# -*- coding: utf-8 -*-
import sublime
import sublime_plugin

_MARK_STYLE = sublime.HIDE_ON_MINIMAP | sublime.PERSISTENT | sublime.HIDDEN

class MarkingChangedRowsCommand(sublime_plugin.EventListener):
	def on_modified(self, view):
		changed = view.get_regions('changed')
		changed +=[view.line(r) for r in view.sel()]
		view.add_regions('changed', changed, 'mark', 'dot', _MARK_STYLE)
		print (changed)

	def on_post_save(self, view):
		settings = sublime.load_settings('MarkingChangedRows.sublime-settings')

		if not settings.get('clear_on_saved'):
			tmp = view.get_regions('changed')
			tmp += view.get_regions('saved')

			view.erase_regions('changed')
			view.erase_regions('saved')

			if not settings.get('clear_on_saved'):
				view.add_regions('saved', tmp, 'comment', 'dot', _MARK_STYLE)
		else:
			view.erase_regions('changed')
			view.erase_regions('saved')


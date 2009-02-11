#!/usr/bin/python

import pygtk
import gtk
import gtk.glade
import string
import os
import gobject

class gui:
	
	def __init__(self):
		self.wTree=gtk.glade.XML('itoaster.glade')
		dic = {	"on_cancel": (gtk.main_quit) }
		self.wTree.signal_autoconnect(dic)
		self.count = 0
		self.win = self.wTree.get_widget("window1")
		self.win.connect("delete_event", self.on_delete_event)
		self.win.maximize()
		self.win.show()
	
	
	def on_delete_event(self, widget, event):
		self.win.set_sensitive(False)
	        dialog = gtk.MessageDialog(self.win,
	        	gtk.DIALOG_MODAL | gtk.DIALOG_DESTROY_WITH_PARENT,
	        	gtk.MESSAGE_INFO, gtk.BUTTONS_YES_NO, None)
	        dialog.set_markup('<big><b>Are you sure you want to quit?</b></big>')
	        dialog.connect("destroy", lambda w: self.win.set_sensitive(True))
	        answer = dialog.run()
		if answer == -8:
			dialog.destroy()
			return False

		if answer == -9:
			dialog.destroy()
			return True

app = gui()
gtk.main()

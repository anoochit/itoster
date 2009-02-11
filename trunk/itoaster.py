#!/usr/bin/python

import pygtk
import gtk
import gtk.glade
import string
import os
import gobject
import pickle

try:  
	import pygtk  
	pygtk.require("2.0")  
except:  
	pass  
try:  
	import gtk  
	import gtk.glade  
except:  
	print("GTK Not Availible")
	sys.exit(1)


class gui:
	
	iso_file = {}
	
	def __init__(self):
		
		# Read a file
		file = open("distrolist.txt")
		self.index=1
		for line in file.readlines():
			line_str=line.split('|')
			self.dictname=self.index;
			gui.iso_file[self.dictname]=line_str[1]
			self.index=self.index+1
		file.close()
		print gui.iso_file
				
		
		# Load GUI
		self.wTree=gtk.glade.XML('itoaster.glade')
		dic = {	"on_cancel": (gtk.main_quit),
						"on_burn": self.on_burn
					}
		self.wTree.signal_autoconnect(dic)
		self.count = 0
		self.win = self.wTree.get_widget("window1")
		self.win.connect("delete_event", self.on_delete_event)
		self.win.maximize()
		self.win.show()

	def on_burn(self, widget):
		self.name= widget.name
		self.file_index= int((self.name.split('button')[1]))
		print gui.iso_file[self.file_index]
		
		
	
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

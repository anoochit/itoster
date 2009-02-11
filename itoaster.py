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
	iso_title = {}
	
	def __init__(self):
		
		# FIXME: you can use sqlite to store cd data
		# Read a file
		file = open("distrolist.txt")
		self.index=1
		for line in file.readlines():
			# make dict for iso_file
			line_str=line.split('|')
			self.dictname=self.index;
			
			# FIXME: fix total button = 26 and label must not null
			if (self.index < 26) and (line_str[0]!="") :
			  gui.iso_file[self.dictname]=line_str[1]
			  gui.iso_title[self.dictname]=line_str[0]
			
			self.index=self.index+1	
		file.close()
		
		# show dict
		print gui.iso_file
		print gui.iso_title
				
		
		# Load GUI
		self.wTree=gtk.glade.XML('itoaster.glade')
		dic = {	"on_cancel": (gtk.main_quit),
						"on_burn": self.on_burn
					}
					
		self.wTree.signal_autoconnect(dic)		
		self.win = self.wTree.get_widget("window1")
		self.win.connect("delete_event", self.on_delete_event)
		self.win.maximize()
		
		# set button label
		for index,filename in gui.iso_file.iteritems():
		  self.button_name="button" + str(index)		  
		  self.button = self.wTree.get_widget(self.button_name)
		  self.button.set_label(gui.iso_title[index])		
   	     
   	    
		self.win.show()

	def on_burn(self, widget):
		self.name= widget.name
		self.file_index= int((self.name.split('button')[1]))
		
		# print iso filename
		print gui.iso_file[self.file_index]	
		
		# FIXME: I didn't check for file exist
		self.isofile="nautilus-cd-burner --source-iso=iso/"+gui.iso_file[self.file_index]
		print self.isofile
		
		# run nautilus cd burner with selected iso image
		os.system(self.isofile)		
		
	
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

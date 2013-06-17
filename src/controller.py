# -*- coding: utf-8 -*-
from crypt import Crypt

import base64
from gi.repository import Gtk
import ntpath


class Controller:

    def __init__(self):
        self.text_tabs = {'None(0)': 'Sin nombre'}
        self.tabs = {0: 'None(0)'}

    def base64_encode(self, gui):
        textview = self.get_current_textview(gui)
        textbuffer = Gtk.TextBuffer()
        textbuffer = textview.get_buffer()
        texto = textbuffer.get_text(textbuffer.get_start_iter(),
            textbuffer.get_end_iter(), True)
        texto_encoded = base64.b64encode(texto)
        textbuffer.set_text(texto_encoded)
        textview.set_buffer(textbuffer)

    def base64_decode(self, gui):
        textview = self.get_current_textview(gui)
        textbuffer = Gtk.TextBuffer()
        textbuffer = textview.get_buffer()
        buffer_start = textbuffer.get_start_iter()
        buffer_end = textbuffer.get_end_iter()
        texto = textbuffer.get_text(buffer_start, buffer_end, True)
        try:
            texto_encoded = base64.b64decode(texto)
        except TypeError:
            print('Type Error')
            texto_encoded = texto
        textbuffer.set_text(texto_encoded)
        textview.set_buffer(textbuffer)

    def new_file(self, gui):
        scrolled = Gtk.ScrolledWindow()
        textview = Gtk.TextView()
        textview.set_wrap_mode(1)
        scrolled.add(textview)
        self.new_tab(gui, scrolled)
        print((self.text_tabs))

    def open_file(self, gui, file_dialog):
        textview = Gtk.TextView()
        textview.set_wrap_mode(1)
        scrolled = Gtk.ScrolledWindow()
        filename = file_dialog.get_filename()
        try:
            f = open(filename, 'r')
            content = f.read()
        except IOError:
            print('I/O Error')
        text_buffer = Gtk.TextBuffer()
        text_buffer.set_text(content)
        textview.set_buffer(text_buffer)
        scrolled.add(textview)
        gui.current_textview = textview
        justname = ntpath.basename(filename)
        self.new_tab(gui, scrolled, filename, justname)
        file_dialog.hide()

    def save_file(self, gui, file_dialog):
        textview = self.get_current_textview(gui)
        notebook = gui.builder.get_object('notebook')
        scrolled = gui.builder.get_object('scrolledwindow1')
        textbuffer = Gtk.TextBuffer()
        textbuffer = textview.get_buffer()
        buffer_start = textbuffer.get_start_iter()
        buffer_end = textbuffer.get_end_iter()
        content = textbuffer.get_text(buffer_start, buffer_end, True)
        filename = file_dialog.get_filename()
        try:
            f = open(filename, 'w')
            f.write(content)
        except IOError:
            print ('I/O Error')
        justname = ntpath.basename(filename)
        notebook.set_tab_label_text(scrolled, justname)
        file_dialog.hide()
        del self.text_tabs[filename]

    def encrypt_text(self, gui, password_entry):
        textentry = self.get_current_textview(gui)
        password = password_entry.get_text()
        textbuffer = Gtk.TextBuffer()
        textbuffer = textentry.get_buffer()
        buffer_start = textbuffer.get_start_iter()
        buffer_end = textbuffer.get_end_iter()
        content = textbuffer.get_text(buffer_start, buffer_end, True)
        key = password
        Cipher = Crypt()
        content_crypted = Cipher.encrypt(key, content)
        try:
            textbuffer.set_text(content_crypted)
            textentry.set_buffer(textbuffer)
        except TypeError:
            print("Type Error")

    def decrypt_text(self, gui, password_entry):
        textentry = self.get_current_textview(gui)
        password = password_entry.get_text()
        textbuffer = Gtk.TextBuffer()
        textbuffer = textentry.get_buffer()
        buffer_start = textbuffer.get_start_iter()
        buffer_end = textbuffer.get_end_iter()
        content = textbuffer.get_text(buffer_start, buffer_end, True)
        key = password
        Cipher = Crypt()
        content_decrypted = Cipher.decrypt(key, content)
        try:
            textbuffer.set_text(content_decrypted)
            textentry.set_buffer(textbuffer)
        except TypeError:
            print("Type Error")

    def get_current_textview(self, gui):
        notebook = gui.builder.get_object('notebook')
        page = notebook.get_current_page()
        scrolled = notebook.get_nth_page(page)
        children = scrolled.get_children()
        textview = children[0]
        return textview

    def new_tab(self, gui, child, filename='None', name='Sin nombre'):
        notebook = gui.builder.get_object('notebook')
        notebook.append_page(child, None)
        notebook.set_tab_label_text(child, name)
        notebook.show_all()
        notebook.set_current_page(-1)
        page = notebook.get_current_page()
        if filename == 'None':
            filename = 'None(' + str(page) + ')'
        if filename in self.text_tabs:
            filename = 'None(' + str(page + page) + ')'
        self.text_tabs[filename] = name
        self.tabs[page] = filename

    def close_file_tab(self, gui):
        notebook = gui.builder.get_object('notebook')
        page = notebook.get_current_page()
        notebook.remove_page(page)

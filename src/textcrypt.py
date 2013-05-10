#!/usr/bin/python
# -*- Mode: Python; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-
#
# main.py
# Copyright (C) 2013 Vladimir Zurita <vladzur@gmail.com>
#
# TextCrypt is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# TextCrypt is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk, GdkPixbuf, Gdk
import os, sys, base64


#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "src/textcrypt.ui"
#UI_FILE = "/usr/local/share/textcrypt/ui/textcrypt.ui"


class GUI:
    def __init__(self):

        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)

        window = self.builder.get_object('window')

        window.show_all()

    def open_clicked(self, window):
        filechooser = window.builder.get_object('filechooserdialog1')
        filechooser.show_all()

    def on_button1_cancel_clicked(window, self):
        self.hide()

    def on_button1_ok_clicked(window, self):
        textarea = window.builder.get_object('textentry')
        filename = self.get_filename()
        f = open(filename, 'r')
        content = f.read()
        text_buffer = Gtk.TextBuffer()
        text_buffer.set_text(content)
        textarea.set_buffer(text_buffer)
        self.hide()

    def on_menubase64_encode_activate(self, window):
        textbuffer = Gtk.TextBuffer()
        textbuffer = self.get_buffer()
        texto = textbuffer.get_text(textbuffer.get_start_iter(),
            textbuffer.get_end_iter(), True)
        texto_encoded = base64.b64encode(texto)
        textbuffer.set_text(texto_encoded)
        self.set_buffer(textbuffer)

    def on_menubase64_decode_activate(self, window):
        textbuffer = Gtk.TextBuffer()
        textbuffer = self.get_buffer()
        buffer_start = textbuffer.get_start_iter()
        buffer_end = textbuffer.get_end_iter()
        texto = textbuffer.get_text(buffer_start, buffer_end, True)
        texto_encoded = base64.b64decode(texto)
        textbuffer.set_text(texto_encoded)
        self.set_buffer(textbuffer)

    def on_menuitem_save_activate(self, window):
        filechoosersave = window.builder.get_object('filechooserdialogsave')
        filechoosersave.show_all()

    def on_filedialogsave_buttoncancel_clicked(self, window):
        self.hide()

    def on_filedialogsave_buttonsave_clicked(self, window):
        textarea = window.builder.get_object('textentry')
        textbuffer = Gtk.TextBuffer()
        textbuffer = textarea.get_buffer()
        buffer_start = textbuffer.get_start_iter()
        buffer_end = textbuffer.get_end_iter()
        content = textbuffer.get_text(buffer_start, buffer_end, True)

        filename = self.get_filename()
        f = open(filename, 'w')
        f.write(content)
        self.hide()

    def destroy(self, window):
        Gtk.main_quit()

    def quit_clicked(self, window):
        Gtk.main_quit()

    def on_menuitem_about_activate(self, window):
        about = window.builder.get_object('aboutdialog1')
        about.run()
        about.hide()


def main():
    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())

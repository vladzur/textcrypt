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

from gi.repository import Gtk
from controller import Controller
import sys


#Comment the first line and uncomment the second before installing
#or making the tarball (alternatively, use project variables)
UI_FILE = "textcrypt.ui"
#UI_FILE = "/usr/local/share/textcrypt/ui/textcrypt.ui"


class GUI:
    def __init__(self):
        self.controller = Controller()
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)
        self.current_textview = None
        window = self.builder.get_object('window')
        window.show_all()
        print('Initialized')

    def open_clicked(self, window):
        filechooser = self.builder.get_object('filechooserdialog1')
        filechooser.show_all()

    def on_button1_cancel_clicked(self, file_dialog_open):
        file_dialog_open.hide()

    def on_button1_ok_clicked(self, file_dialog_open):
        self.controller.open_file(self, file_dialog_open)

    def on_menubase64_encode_activate(self, textview):
        self.controller.base64_encode(self)

    def on_menubase64_decode_activate(self, textview):
        self.controller.base64_decode(self)

    def on_menuitem_save_activate(self, window):
        filechoosersave = self.builder.get_object('filechooserdialogsave')
        filechoosersave.show_all()

    def on_filedialogsave_buttoncancel_clicked(self, file_dialog_save):
        file_dialog_save.hide()

    def on_menuitem_new_activate(self, textentry):
        self.controller.new_file(self)

    def on_filedialogsave_buttonsave_clicked(self, file_dialog):
        self.controller.save_file(self, file_dialog)

    def on_encrypt_menuitem_activate(self, textentry):
        dialog = self.builder.get_object('dialog_password_encrypt')
        dialog.run()
        dialog.hide()

    def on_button_password_encrypt_ok_clicked(self, password_entry):
        self.controller.encrypt_text(self, password_entry)

    def on_decrypt_menuitem_activate(self, textentry):
        dialog = self.builder.get_object('dialog_password_decrypt')
        dialog.run()
        dialog.hide()

    def on_button_password_decrypt_ok_clicked(self, password_entry):
        self.controller.decrypt_text(self, password_entry)

    def destroy(self, window):
        print('Terminated')
        Gtk.main_quit()

    def quit_clicked(self, window):
        print('Terminated')
        Gtk.main_quit()

    def on_menuitem_about_activate(self, window):
        about = self.builder.get_object('aboutdialog1')
        about.run()
        about.hide()

    def on_menuitem_close_file_activate(self, window):
        self.controller.close_file_tab(self)


def main():
    app = GUI()
    Gtk.main()

if __name__ == "__main__":
    sys.exit(main())

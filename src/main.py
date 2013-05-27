#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
from textcrypt import GUI


def main():
    app = GUI()
    Gtk.main()
    return(app)

if __name__ == '__main__':
    main()


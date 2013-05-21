# -*- coding: utf-8 -*-
import sqlite3


class DB:

    def __init__(self):
        self.conn = sqlite3.connect('config.db')
        self.cursor = self.conn.cursor()

    def set_file(self, data):
        pass

    def get_file(self, data):
        pass

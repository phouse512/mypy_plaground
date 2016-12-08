#!/usr/bin/env pythonn
# -*- coding: utf-8 -*-

import mimetypes

print(mimetypes.guess_type(u"test☃.xml"))

#print(mimetypes.guess_type(u"test☃.xml".encode("utf-8")))


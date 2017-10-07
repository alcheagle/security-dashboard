# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import os

class scanner:

    def scan (scn_type, domains):
        for domain in domains:
            "./scan "+domain+" --scan="+scn_type+" > "+domain+".txt"

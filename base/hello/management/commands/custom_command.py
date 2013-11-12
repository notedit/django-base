# -*- coding:utf-8 -*-


from django.core.management.base import BaseCommand, CommandError

"""
custom command

"""

class Command(BaseCommand):
    args = 'xxxxx'
    help = 'helpxxxxxxxxxx'

    def handle(self,*args,**options):
        self.stdout.write('yes custom command')

import os 
import datetime
import time
from os import path

def check_notes_path():
  path = os.getcwd() 
  return path

def get_current_date():
  return str(datetime.date.today())

def get_month():
  month = datetime.datetime.now()
  return month.strftime('%b').lower()

def touch_md_file(name):
  return time.strftime('%m-%d-%Y')

def mkdir(month):
  path_to_notes = os.getcwd() + '/notes/' + month
  if not path.exists(path_to_notes):
    os.makedirs(path_to_notes)
  return path_to_notes

def header(date):
  return '### Notes ' + date + '\n========================'

def note():
  date = get_current_date()
  path = mkdir(get_month())
  path_to_note = path + '/'
  filename = date + '.md'
  title = header(date)
  with open(os.path.join(path, filename), 'wb') as note:
    note.write(title)
note()
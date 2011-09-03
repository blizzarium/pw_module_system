import string
from module_info import *
from module_map_icons import *

from process_common import *
from process_operations import *

import module_sounds

def save_map_icons(variable_list,variable_uses,tag_uses,quick_strings):
  ofile = open(export_dir + "map_icons.txt","w")
  ofile.write("map_icons_file version 1\n")
  ofile.write("%d\n"%len(map_icons))
  for map_icon in map_icons:
    triggers = []
    sound_id = find_str_id(module_sounds.sounds, map_icon[4], tag_sound)
    if (len(map_icon) >= 8):
      ofile.write("%s %d %s %f %d %f %f %f "%(map_icon[0],map_icon[1],map_icon[2],map_icon[3],sound_id,map_icon[5],map_icon[6],map_icon[7]))
      if (len(map_icon) == 9):
        triggers = map_icon[8]
    else:
      ofile.write("%s %d %s %f %d 0 0 0 "%(map_icon[0],map_icon[1],map_icon[2],map_icon[3],sound_id))
      if (len(map_icon) == 6):
        triggers = map_icon[5]
    save_simple_triggers(ofile,triggers, variable_list,variable_uses,tag_uses,quick_strings)
    ofile.write("\n")
  ofile.close()

def save_python_header():
  ofile = open("./ID_map_icons.py","w")
  for i, map_icon in enumerate(map_icons):
    ofile.write("icon_%s = %d\n"%(map_icon[0], i))
  ofile.close()

print "Exporting map icons..."
save_python_header()
variable_uses = []
variables = load_variables(export_dir,variable_uses)
tag_uses = []
quick_strings = load_quick_strings(export_dir)
save_map_icons(variables,variable_uses,tag_uses,quick_strings)
save_variables(export_dir,variables,variable_uses)
save_quick_strings(export_dir,quick_strings)

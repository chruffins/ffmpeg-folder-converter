import sys
import os

fstr = """ffmpeg -i "{0}" -ab 320k -map_metadata 0 -id3v2_version 3 "{1}" """

def full_name(folder, file, ftype):
    # file here is implied to not have the extension attached.
    return folder + "\\" + file + "." + ftype

def convert_audio_file(folder, file, from_type, to_type, out_folder):
    # file has ext attached and needs to be removed.
    code = 2 # meaning "Did Not Execute" b/c it wasn't supposed to be done
    fname = file.split('.')[0]
    if file.split('.')[1] == from_type:
        code = os.system(fstr.format(full_name(folder,fname,from_type),
                              full_name(out_folder,fname,to_type)))
        """print(fstr.format(full_name(folder,fname,from_type),
                              full_name(out_folder,fname,to_type)))"""
    print(file + " conversion: " + str(code))

def convert_audio_folder(input_folder, from_type, to_type, output_folder=""):
    # don't bother checking for valid types.
    assert from_type != to_type and os.path.exists(input_folder)
    output_folder = (output_folder == "" and input_folder) or output_folder
    
    for x in os.scandir(input_folder):
        convert_audio_file(input_folder, x.name, from_type, to_type, output_folder)
    

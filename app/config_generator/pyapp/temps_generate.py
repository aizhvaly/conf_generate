# -*- coding: utf-8 -*-

import os
from jinja2 import Environment, FileSystemLoader

def temps_generate(data):

    '''
    DOCSTRING
    '''

    curr_dir = os.path.dirname(os.path.abspath(__file__)) + '/configs/' + data['path']
    env = Environment(loader=FileSystemLoader(curr_dir),\
                      trim_blocks=True,	lstrip_blocks=True)
    backpath = os.getcwd()
    dir = 'storage/' + data['path']
    try:
        os.chdir(dir)
    except:
        os.system('mkdir -p ' + dir)
        os.chdir(dir)

    template = env.get_template('template.txt')
    file_name = data['net_details']['net_details_ip']+'.cfg'

    with open(file_name, 'w+') as file:
        file.write(template.render(data))
        req = dir + file_name

    os.chdir(backpath)
    return req



def main():
    pass
if __name__ == '__main__':
    main()


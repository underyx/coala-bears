from Constants import classifiers, imports, encoding, requirements,
from Constants import setup_constants


filename = "setup.py"

bearOption = input("What bear do you want to upload?\n")
#bearName = bearOption + ".py"
#print(bearName)

setup = open(filename, "w")

# set env
setup.write('#!/usr/bin/env python3\n\n')

# write imports
setup.write(imports + '\n\n')

# encoding UTF-8
setup.write(encoding + '\n\n')

# requirements
setup.write(requirements +'\n\n')

# setuptools
setup.write('if __name__== "__main__":\n')
setup.write('\tsetup(name=' + bearOption + "',\n")
setup.write('\t\t  version=Constants.VERSION,\n')
setup.write("\t\t  description='The " + bearOption +" bear for coala (Code")
setup.write(" Analysis Application)',\n")
setup.write('\t\t  classifiers=' + classifiers + ')')

 # close the file
setup.close()

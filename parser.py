import os
import sys

# Find out the file location within the sources tree
this_module_dir_path = os.path.abspath(
    os.path.dirname(sys.modules[__name__].__file__))
# Add pygccxml package to Python path
sys.path.append(os.path.join(this_module_dir_path, '..', '..'))


from pygccxml import parser  # nopep8
from pygccxml import declarations  # nopep8
from pygccxml import utils  # nopep8

# Find out the xml generator (gccxml or castxml)
generator_path, generator_name = utils.find_xml_generator()

# Configure the xml generator
config = parser.xml_generator_configuration_t(
    xml_generator_path=generator_path,
    xml_generator=generator_name,
    compiler="gcc")

# Parsing source file
decls = parser.parse([this_module_dir_path + '/bech32.h'], config)
global_ns = declarations.get_global_namespace(decls)

# Get object that describes unittests namespace
unittests = global_ns.namespace('bech32')

#print('"unittests" declarations: \n')
#:withindeclarations.print_declarations(unittests)

# Print all base and derived class names
for class_ in unittests.classes():
    print('class "%s" hierarchy information:' % class_.name)
    print('\tbase classes   : ', repr([
        base.related_class.name for base in class_.bases]))
    print('\tderived classes: ', repr([
        derive.related_class.name for derive in class_.derived]))
    print('\n')



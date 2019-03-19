import sys
import os
import time
from xml.etree.ElementTree import iterparse
from xml.etree import ElementTree



# /universe
def handle_open_universe(node):
    pass

# /universe/namespace
def handle_open_namespace(node):
    schema_name = node.attrib['id']

    print('DROP DATABASE IF EXISTS {};'.format(schema_name))
    print()
    print('CREATE DATABASE {};'.format(schema_name))
    print()
    print('USE {};'.format(schema_name))
    print()

# /universe/namespace/tables
def handle_open_tables(node):
    pass

# /universe/namespace/tables/table
def handle_open_table(node):
    print('CREATE TABLE {}'.format(node.attrib['id']))
    print('(')
    print('    id   BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,')

# /universe/namespace/tables/table/columns
def handle_open_columns(node):
    pass

# /universe/namespace/tables/table/columns/column
def handle_open_column(node):
    print('    {}'.format(node.attrib['id']), end=' ')

# /universe/namespace/tables/table/columns/column/datatype
def handle_open_datatype(node):
    print(' {}'.format(node.text), end=' ')

# '/universe/namespace/tables/table/columns/column/datatype'
def handle_closed_datatype(node):
    pass


# /universe/namespace/tables/table/columns/column
def handle_closed_column(node):
    print()

# /universe/namespace/tables/table/columns/column/nullable
def handle_open_nullable(node):
    pass

# /universe/namespace/tables/table/columns/column/default
def handle_open_default(node):
    pass

# '/universe/namespace/tables/table/columns/column/default'
def handle_closed_default(node):
    pass

# /universe/namespace/tables/table/columns
def handle_closed_columns(node):
    pass

# /universe/namespace/tables/table
def handle_closed_table(node):
    print(')')
    print('ENGINE =INNODB;')
    print()

# /universe/namespace/tables
def handle_closed_tables(node):
    pass

# '/universe/namespace/tables/table/columns/column/nullable'
def handle_closed_nullable(node):
    pass

# /universe/namespace
def handle_closed_namespace(node):
    pass

# /universe
def handle_closed_universe(node):
    pass

def get_indention_str(size):
    # print(size)
    indent = ''
    for i in range(0, size):
        indent += indent.join('-')
        # print(indent)
    return indent

def pathalize_list(list):
    return "/" + "/".join(list)

def traverse_xml(xml_filename):

    NODES = []

    PATH_STACK = []

    EVENT_NAMES = ['start', 'end', 'start-ns', 'end-ns']

    for (event, node) in iterparse(xml_filename, EVENT_NAMES):
        if event == 'end':
            PATH_STACK.pop()
            IDENT = get_indention_str(len(PATH_STACK))
            # print(IDENT + node.tag)
            path = pathalize_list(PATH_STACK)

            if path == '/universe':
                handle_closed_universe(node)
            elif path == '/universe/namespace':
                handle_closed_namespace(node)
            elif path == '/universe/namespace/tables':
                handle_closed_tables(node)
            elif path == '/universe/namespace/tables/table':
                handle_closed_table(node)
            elif path == '/universe/namespace/tables/table/columns':
                handle_closed_columns(node)
            elif path == '/universe/namespace/tables/table/columns/column':
                handle_closed_column(node)
            elif path == '/universe/namespace/tables/table/columns/column':
                handle_closed_column(node)
            elif path == '/universe/namespace/tables/table/columns/column/default':
                handle_closed_default(node)
            elif path == '/universe/namespace/tables/table/columns/column/nullable':
                handle_closed_nullable(node)
            elif path == '/universe/namespace/tables/table/columns/column/datatype':
                handle_closed_datatype(node)


        if event == 'start':
            IDENT = get_indention_str(len(PATH_STACK))
            # print(IDENT + node.tag)
            PATH_STACK.append(node.tag)
            path = pathalize_list(PATH_STACK)

            if path == '/universe':
                handle_open_universe(node)
            elif path == '/universe/namespace':
                handle_open_namespace(node)
            elif path == '/universe/namespace/tables':
                handle_open_tables(node)
            elif path == '/universe/namespace/tables/table':
                handle_open_table(node)
            elif path == '/universe/namespace/tables/table/columns':
                handle_open_columns(node)
            elif path == '/universe/namespace/tables/table/columns/column':
                handle_open_column(node)
            elif path == '/universe/namespace/tables/table/columns/column':
                handle_open_column(node)
            elif path == '/universe/namespace/tables/table/columns/column/default':
                handle_open_default(node)
            elif path == '/universe/namespace/tables/table/columns/column/nullable':
                handle_open_nullable(node)
            elif path == '/universe/namespace/tables/table/columns/column/datatype':
                handle_open_datatype(node)


def main():
    xml_filename = '/home/abjax/pycharm_projects/2019-03-18/schema.xml'
    traverse_xml(xml_filename)

if __name__ == '__main__':
    main()

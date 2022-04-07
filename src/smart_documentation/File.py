import dir_ops as do
from dir_ops import Path, Dir
import py_starter as ps

import subprocess
import ParentClass
import html_support as html_sf 

class Files( ParentClass.ParentClass ):

    FOLDER = 'files'

    def __init__( self, Documentation ):

        ParentClass.ParentClass.__init__( self )

        self.Documentation = Documentation
        self.Dir = Dir( self.Documentation.Repo.pages_Dir.join( self.FOLDER ) )
        self.base_url = self.Documentation.Repo.pages_url + '/' + self.FOLDER

        self.Files = []
        self.get_Files()

    def print_imp_atts( self, print_off = True ):

        string = self.print_class_type( print_off = False ) + '\n'
        string += 'Files:\n'
        for File_inst in self:
            string += File_inst.print_one_line_atts( print_off = False ) + '\n'

        string = string[:-1]

        return self.print_string( string, print_off = print_off )

    def print_one_line_atts( self, **kwargs ):
        
        self.len_Files = len(self)
        return self._print_one_line_atts_helper( atts = ['type','len_Files'], **kwargs )

    def __len__( self ):

        return len( self.Files )

    def __iter__( self ):

        self.i = -1
        return self

    def __next__( self ):

        self.i += 1

        if self.i < len(self):
            return self.Files[ self.i ]
        else:
            raise StopIteration

    def _add_File( self, new_File ):

        self.Files.append( new_File )

    def make_File( self, *args, **kwargs ):

        new_File = File( self, *args, **kwargs )
        self._add_File( new_File )
        return new_File

    def get_Files( self ):

        # Check Git's output for the list of relative paths that are present for the Repo
        command_line_string = self.Documentation.Repo.git_command_line_string( 'ls-files' )
        print ('>>> ' + command_line_string)
        list_of_relative_paths = subprocess.check_output( command_line_string , shell=True).splitlines()

        for relative_path in list_of_relative_paths:
            relative_path = relative_path.decode( 'utf-8' )
            relative_Path = Path( relative_path )

            valid = True
            for folder in self.Documentation.FOLDERS_TO_SKIP:
                if folder in relative_Path.dirs:
                    valid = False
                    break

            if valid:
                file_Path = Path( self.Documentation.Repo.Dir.join( relative_Path.p ) )
                if file_Path.filename not in self.Documentation.FILENAMES_TO_SKIP and file_Path.ending not in self.Documentation.FILE_ENDINGS_TO_SKIP:
                    self.make_File( file_Path = file_Path )

        self.print_atts()

    def generate( self ):

        for File_inst in self:
            File_inst.generate()

    def export( self ):

        for File_inst in self:
            File_inst.export()



class File( ParentClass.ParentClass ):

    def __init__( self, Files, file_Path ):

        ParentClass.ParentClass.__init__( self )

        self.Files = Files
        self.Path = file_Path
        self.rel_Path = Path( do.remove_prefix_from_paths( self.Files.Documentation.Repo.Dir.p, [self.Path.p] )[0] )
        self.html_Path = Path( self.Files.Dir.join( self.rel_Path.p + '.html' ) )
        self.rel_html_Path =  Path( do.remove_prefix_from_paths( self.Files.Dir.p, [self.html_Path.p] )[0]  )

        self.level = len( self.rel_Path.dirs ) - 1
        self.pages_url = self.Files.base_url + '/' + self.rel_html_Path.p

        self.print_atts()

    def print_imp_atts( self, **kwargs ):

        return self._print_imp_atts_helper( atts = ['Path','rel_Path','html_Path','rel_html_Path','pages_url','level'], **kwargs )

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_line_atts_helper( atts = ['type','Path'], **kwargs )

    def generate( self ):

        try:
            string = self.Path.read()
        except:
            string = ''

        lines = string.split( '\n' )
        
        self.html_lines = [ html_sf.h1( self.rel_Path.p ) ]
        self.html_lines.append( 'This file has {n} lines'.format( n = len(lines) )  )

    def export( self ):

        self.html_Path.create_directories_before_download()
        self.html_Path.write( lines = self.html_lines )

import ParentClass
import markdown_support as md
import html_support as html_sf
import dir_ops as do
from dir_ops import Path, Dir
import py_starter as ps
import subprocess
import Repository
import File

class Documentation( ParentClass.ParentClass ):

    FOLDERS_TO_SKIP = ['docs']
    FILENAMES_TO_SKIP = [ '.gitignore','README.md' ]
    FILE_ENDINGS_TO_SKIP = [ 'docx','xlsx' ]

    def __init__( self, Doc_Repo, *args, user_profile = None, params = None, calling_Repo = None, **kwargs ):

        ParentClass.ParentClass.__init__( self )
        Doc_Repo.print_atts()
        self.Doc_Repo = Doc_Repo
        self.Repo = calling_Repo
        self.user_profile = user_profile
        self.params = params

        self.Files = File.Files( self )

    def print_imp_atts( self, print_off = True ):

        return self._print_imp_atts_helper( atts = ['Repo','Files'], print_off = print_off )

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_line_atts_helper( atts = ['type','Repo','Files'], **kwargs )

    def generate( self ):

        self.Files.generate()
        self.generate_README()
        self.generate_index()

    def export( self ):

        self.Files.export()

    def generate_README( self ):

        string = self.Repo.README_Path.read()
        lines = string.split( '\n' )
        
        pages_link = md.link( self.Repo.name + ' Pages', self.Repo.pages_url )
        if pages_link not in lines:
            lines.insert( 0, pages_link )

        self.Repo.README_Path.write( lines = lines )

    def generate_index( self ):

        lines = []
        lines.append( html_sf.h1( self.Repo.name ) )
        lines.append( html_sf.link( 'Repository Home', self.Repo.url ) )
        lines.append( html_sf.line_break() )
        lines.append( html_sf.h2( 'Git Tracked Files:' ) )
        lines.append( html_sf.line_break() )

        for File_inst in self.Files:
            link = html_sf.link( '  ' * File_inst.level + File_inst.rel_Path.p, File_inst.pages_url ) + html_sf.line_break()
            lines.append( link )

        self.Repo.html_index_Path.write( lines = lines )

    def run( self ):

        self.print_atts()
        self.generate()
        self.export()

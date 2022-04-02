import ParentClass
import markdown_support as md
import dir_ops as do
from dir_ops import Dir, Path
import py_starter as ps

class Page( ParentClass.ParentClass ):

    def __init__( self, Documentation, Path, contents = '' ):

        ParentClass.ParentClass.__init__( self )
        self.Documentation = Documentation
        self.Path = Path
        self.get_relative_Path()
        self.level = len( self.rel_Path.dirs ) - 1
        self.contents = contents

    def print_imp_atts( self, **kwargs ):

        return self._print_imp_atts_helper( atts = ['Path','rel_Path','level'], **kwargs )

    def print_one_line_atts( self, **kwargs ):

        return self._print_one_line_atts_helper( atts = ['type','Path'], **kwargs )

    def get_relative_Path( self ):

        self.rel_Path = Path( do.remove_prefix_from_paths( self.Documentation.Repo.Dir.p, [self.Path.p] )[0] )

    def generate( self ):

        pass
import pypi_builder
import os

class DocumentationGenerator( pypi_builder.PackageGenerator ):

    def __init__( self ):
        pypi_builder.PackageGenerator.__init__( self )

    def generate_sphinx( self ):
        os.system( self.cfg['sphinx_script_Path'].read() ) 

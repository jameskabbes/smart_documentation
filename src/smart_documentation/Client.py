import smart_documentation
import kabbes_client
import pypi_builder

class Client( smart_documentation.DocumentationGenerator ):

    _BASE_DICT = {}

    def __init__( self, dict={} ):

        d = {}
        d.update( Client._BASE_DICT )
        d.update( dict )

        self.Package = kabbes_client.Package( smart_documentation._Dir, dict=d )
        cfg_sd = self.Package.cfg
        cfg_pypi = pypi_builder.Client().cfg

        cfg_pypi.merge( cfg_sd )
        self.cfg = cfg_pypi

        smart_documentation.DocumentationGenerator.__init__( self )


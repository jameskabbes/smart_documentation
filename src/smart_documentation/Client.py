import smart_documentation
import pypi_builder
import kabbes_user_client
import py_starter as ps
import datetime

class Client( smart_documentation.DocumentationGenerator, pypi_builder.Client ):

    BASE_CONFIG_DICT = {
        "_Dir": smart_documentation._Dir
    }

    def __init__( self, dict={}, **kwargs ):

        pypi_builder.Client.__init__( self )
        dict = ps.merge_dicts( Client.BASE_CONFIG_DICT, dict )
        overwrite_cfg = kabbes_user_client.Client( dict=dict, **kwargs ).cfg
        self.cfg.merge(overwrite_cfg)

        smart_documentation.DocumentationGenerator.__init__( self )


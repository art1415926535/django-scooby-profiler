from .plugins.viewname import ViewNamePlugin
from .plugins.sql import SQLPlugin
from .plugins.processtime import ProcessTimePlugin

plugin_instances = [
    ViewNamePlugin(),
    ProcessTimePlugin(),
    SQLPlugin(),
]

def get_plugins():
    return plugin_instances

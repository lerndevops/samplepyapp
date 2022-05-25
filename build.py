from pybuilder.core import use_plugin, init, Author

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

name    = "spyapp"
version = "1.0"

summary = "Example PyBuilder / Git project"

description = """An example PyBuilder / Git project for project management
and file version control. See blog post at http://bit.ly/2QY65wO for a
more through explanation."""

authors      = ""
license      = "None"
default_task = "publish"

@init
def initialize(project):
    project.build_depends_on("mockito")

@init
def set_properties(project):
    pass

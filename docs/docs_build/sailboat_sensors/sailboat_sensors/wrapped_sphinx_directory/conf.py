## Generated by rosdoc2.verbs.build.builders.SphinxBuilder.
## This conf.py imports the user defined (or default if none was provided)
## conf.py, extends the settings to support Breathe and Exhale and to set up
## intersphinx mappings correctly, among other things.

import os
import sys

## exec the user's conf.py to bring all of their settings into this file.
exec(open("/home/ros2_user/ros2_ws/src/docs/docs_build/sailboat_sensors/sailboat_sensors/default_sphinx_project/conf.py").read())

def ensure_global(name, default):
    if name not in globals():
        globals()[name] = default

## Based on the rosdoc2 settings, do various things to the settings before
## letting Sphinx continue.

ensure_global('rosdoc2_settings', {})
ensure_global('extensions', [])
ensure_global('project', "sailboat_sensors")
ensure_global('author', """alber""")
ensure_global('release', "0.0.0")
ensure_global('version', "0.0")

if rosdoc2_settings.get('enable_autodoc', True):
    print('[rosdoc2] enabling autodoc', file=sys.stderr)
    extensions.append('sphinx.ext.autodoc')

    pkgs_to_mock = []
    import importlib
    for exec_depend in []:
        try:
            # Some python dependencies may be dist packages.
            exec_depend = exec_depend.split("python3-")[-1]
            importlib.import_module(exec_depend)
        except ImportError:
            pkgs_to_mock.append(exec_depend)
    # todo(YV): If users provide autodoc_mock_imports in their conf.py
    # it will be overwritten by those in exec_depends.
    # Consider appending to autodoc_mock_imports instead.
    autodoc_mock_imports = pkgs_to_mock

if rosdoc2_settings.get('enable_intersphinx', True):
    print('[rosdoc2] enabling intersphinx', file=sys.stderr)
    extensions.append('sphinx.ext.intersphinx')

build_type = 'ament_python'
always_run_doxygen = False
# By default, the `exhale`/`breathe` extensions should be added if `doxygen` was invoked
is_doxygen_invoked = False

if rosdoc2_settings.get('enable_breathe', is_doxygen_invoked):
    # Configure Breathe.
    # Breathe ingests the XML output from Doxygen and makes it accessible from Sphinx.
    print('[rosdoc2] enabling breathe', file=sys.stderr)
    # First check that doxygen would have been run
    if not is_doxygen_invoked:
        raise RuntimeError(
            "Cannot enable the 'breathe' extension if 'doxygen' is not invoked. "
            "Please enable 'always_run_doxygen' if the package is not an "
            "'ament_cmake' or 'cmake' package.")
    ensure_global('breathe_projects', {})
    breathe_projects.update({
    })
    if breathe_projects:
        # Enable Breathe and arbitrarily select the first project.
        extensions.append('breathe')
        breathe_default_project = next(iter(breathe_projects.keys()))

if rosdoc2_settings.get('enable_exhale', is_doxygen_invoked):
    # Configure Exhale.
    # Exhale uses the output of Doxygen and Breathe to create easier to browse pages
    # for classes and functions documented with Doxygen.
    # This is similar to the class hierarchies and namespace listing provided by
    # Doxygen out of the box.
    print('[rosdoc2] enabling exhale', file=sys.stderr)
    # First check that doxygen would have been run
    if not is_doxygen_invoked:
        raise RuntimeError(
            "Cannot enable the 'breathe' extension if 'doxygen' is not invoked. "
            "Please enable 'always_run_doxygen' if the package is not an "
            "'ament_cmake' or 'cmake' package.")
    extensions.append('exhale')
    ensure_global('exhale_args', {})

    default_exhale_specs_mapping = {
        'page': [':content-only:'],
        **dict.fromkeys(
            ['class', 'struct'],
            [':members:', ':protected-members:', ':undoc-members:']),
    }

    exhale_specs_mapping = rosdoc2_settings.get(
        'exhale_specs_mapping', default_exhale_specs_mapping)

    from exhale import utils
    exhale_args.update({
        # These arguments are required.
        "containmentFolder": "/home/ros2_user/ros2_ws/src/docs/docs_build/sailboat_sensors/sailboat_sensors/wrapped_sphinx_directory/generated",
        "rootFileName": "index.rst",
        "rootFileTitle": "C++ API",
        "doxygenStripFromPath": "..",
        # Suggested optional arguments.
        "createTreeView": True,
        "fullToctreeMaxDepth": 1,
        "unabridgedOrphanKinds": [],
        "fullApiSubSectionTitle": "Full C++ API",
        # TIP: if using the sphinx-bootstrap-theme, you need
        # "treeViewIsBootstrap": True,
        "exhaleExecutesDoxygen": False,
        # Maps markdown files to the "md" lexer, and not the "markdown" lexer
        # Pygments registers "md" as a valid markdown lexer, and not "markdown"
        "lexerMapping": {r".*\.(md|markdown)$": "md",},
        "customSpecificationsMapping": utils.makeCustomSpecificationsMapping(
            lambda kind: exhale_specs_mapping.get(kind, [])),
    })

if rosdoc2_settings.get('override_theme', True):
    extensions.append('sphinx_rtd_theme')
    html_theme = 'sphinx_rtd_theme'
    print(f"[rosdoc2] overriding theme to be '{html_theme}'", file=sys.stderr)

if rosdoc2_settings.get('automatically_extend_intersphinx_mapping', True):
    print(f"[rosdoc2] extending intersphinx mapping", file=sys.stderr)
    if 'sphinx.ext.intersphinx' not in extensions:
        raise RuntimeError(
            "Cannot extend intersphinx mapping if 'sphinx.ext.intersphinx' "
            "has not been added to the extensions")
    ensure_global('intersphinx_mapping', {
        'sailboat_launch': ('http://docs.ros.org/en/latest/p/sailboat_launch/', '/home/ros2_user/ros2_ws/src/docs/cross_reference/sailboat_launch/objects.inv')
    })

if rosdoc2_settings.get('support_markdown', True):
    print(f"[rosdoc2] adding markdown parser", file=sys.stderr)
    # The `myst_parser` is used specifically if there are markdown files
    # in the sphinx project
    extensions.append('myst_parser')

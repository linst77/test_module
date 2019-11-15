from pymel import mayautils
import maya.cmds as cmds


def init_plugin():

    # make sure all plugins loaded
    mgear_plugins = ["dynamicShelf"]
    loaded_plugins = cmds.pluginInfo(q=1, listPlugins=True)
    unloaded_plugins = [x for x in mgear_plugins if x not in loaded_plugins]

    for i in unloaded_plugins:
        cmds.loadPlugin( unloaded_plugins)

    # make UI for mGear
    menu_loader.mGear_menu_loader()

if not cmds.about(batch=True):
    mayautils.executeDeferred(init_plugin())

import sys
import os
import maya.mel
import pipelineTools

scriptsPath = os.environ.get('MAYA_SCRIPT_PATH', None)
dynamicShelfPath = os.environ.get('DYNAMIC_SHELF_PATH', None)
sys.path.append(scriptsPath)


def initializePlugin(mobject):
    maya.mel.eval('global string $gShelfTopLevel;')

    master_shelf_loader = 'MASTER'
    pipelineTools.loadDynamicShelf(master_shelf_loader)

    dynamic_shelves = [shelf.split('_dynamicShelfConf.yml')[0] for shelf in os.listdir(dynamicShelfPath)
                       if 'dynamicShelfConf.yml' in shelf and 'ShelfLoader' not in shelf]

    for dynamic_shelf in dynamic_shelves:
        pipelineTools.reloadDynamicShelf(dynamic_shelf)

def uninitializePlugin(mobject):
    dynamic_shelves = [shelf.split('_dynamicShelfConf.yml')[0] for shelf in os.listdir(dynamicShelfPath)
                       if 'dynamicShelfConf.yml' in shelf]
    for dynamic_shelf in dynamic_shelves:
        pipelineTools.removeDynamicShelf(dynamic_shelf)

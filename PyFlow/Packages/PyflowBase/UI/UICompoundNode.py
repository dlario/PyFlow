from Qt import QtWidgets

from PyFlow.UI.Canvas.UINodeBase import UINodeBase
from PyFlow.UI.Canvas.UINodeBase import getUINodeInstance
from PyFlow.UI.Utils.Settings import *
from PyFlow.UI import RESOURCES_DIR
from PyFlow.Core.Common import *


class UICompoundNode(UINodeBase):
    def __init__(self, raw_node):
        super(UICompoundNode, self).__init__(raw_node)
        self._rawNode.pinExposed.connect(self._createUIPinWrapper)
        self.headColorOverride = Colors.Gray
        self.color = Colors.DarkGray
        self.image = RESOURCES_DIR + "/gear.svg"

    def updateSize(self, name):
        self.updateNodeShape()

    def getGraph(self):
        return self._rawNode.rawGraph

    def mouseDoubleClickEvent(self, event):
        self._rawNode.graph().graphManager.selectGraph(self.name)
        event.accept()

    def kill(self, *args, **kwargs):
        super(UICompoundNode, self).kill()

    def onGraphNameChanged(self, newName):
        self.displayName = newName
        self.name = newName

    def postCreate(self, jsonTemplate=None):
        super(UICompoundNode, self).postCreate(jsonTemplate)
        self.canvasRef().createWrappersForGraph(self._rawNode.rawGraph)
        self._rawNode.rawGraph.nameChanged.connect(self.onGraphNameChanged)
        self.displayName = self._rawNode.name

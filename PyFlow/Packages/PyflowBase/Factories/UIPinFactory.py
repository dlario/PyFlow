from PyFlow.UI.Canvas.UIPinBase import UIPinBase
from PyFlow.Packages.PyflowBase.Pins.AnyPin import AnyPin
from PyFlow.Packages.PyflowBase.Pins.ExecPin import ExecPin
from PyFlow.Packages.PyflowBase.Pins.ListPin import ListPin

from PyFlow.Packages.PyflowBase.UI.UIAnyPin import UIAnyPin
from PyFlow.Packages.PyflowBase.UI.UIExecPin import UIExecPin
from PyFlow.Packages.PyflowBase.UI.UIListPin import UIListPin


def createUIPin(owningNode, raw_instance):
    if isinstance(raw_instance, AnyPin):
        return UIAnyPin(owningNode, raw_instance)
    elif isinstance(raw_instance, ExecPin):
        return UIExecPin(owningNode, raw_instance)
    elif isinstance(raw_instance, ListPin):
        return UIListPin(owningNode, raw_instance)
    else:
        return UIPinBase(owningNode, raw_instance)

from PyFlow.Core import NodeBase


class doN(NodeBase):
    def __init__(self, name):
        super(doN, self).__init__(name)
        self.enter = self.createInputPin('Enter', 'ExecPin', self.compute)
        self._N = self.createInputPin('N', 'IntPin')
        self._N.setData(10)
        self.reset = self.createInputPin('Reset', 'ExecPin', self.OnReset)

        self.completed = self.createOutputPin('Exit', 'ExecPin')
        self.counter = self.createOutputPin('Counter', 'IntPin')
        self.bClosed = False
        self._numCalls = 0

    def OnReset(self):
        self.bClosed = False
        self._numCalls = 0

    @staticmethod
    def pinTypeHints():
        return {'inputs': ['ExecPin', 'IntPin'], 'outputs': ['ExecPin', 'IntPin']}

    @staticmethod
    def category():
        return 'FlowControl'

    @staticmethod
    def keywords():
        return []

    @staticmethod
    def description():
        return 'The DoN node will fire off an execution pin N times. After the limit has been reached,\
        it will cease all outgoing execution until a pulse is sent into its Reset input.'

    def compute(self, *args, **kwargs):
        maxCalls = self._N.getData()
        if not self.bClosed and self._numCalls <= maxCalls:
            self._numCalls += 1
            self.counter.setData(self._numCalls)
            self.completed.call(*args, **kwargs)

            # if next time we will reach the limit - close
            if (self._numCalls + 1) > maxCalls:
                self.bClosed = True

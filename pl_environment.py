#!/usr/bin/env python
""" generated source for module Environment """
import copy
from pl_evalexception import EvalException

class Environment(object):
    """ generated source for class Environment """

    def __init__(self):
        """ generated source for method __init__ """
        self.map = {}
        self.funcMap = {}

    def put(self, var, val):
        """ generated source for method put """
        self.map[var] = val
        return val

    def get(self, pos, var):
        """ generated source for method get """
        if var in self.map:
            return self.map[var]
        raise EvalException(pos, "undefined variable: " + var)

    def putFunc(self, id, val):
        self.funcMap[id] = val
        return val

    def getFunc(self, pos, id):
        if id in self.funcMap:
            return self.funcMap[id]
        raise EvalException(pos, "undefined function: " + id)

    #deep copy global environment, work in local copy
    def copy(self,env):
        scopeEnv = copy.deepcopy(env)
        for id in self.map:
            scopeEnv.put(id, self.map[id])
        for id in self.funcMap:
            scopeEnv.putFunc(id, self.funcMap[id])
        return scopeEnv

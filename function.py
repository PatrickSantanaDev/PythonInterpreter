#!/usr/bin/env python

class Function(object):

    def __init__(self, args, expr):
        self.args = args
        self.expr = expr

    def call(self, env, expr):
        envCopy = env.copy(env)
        envCopy.put(self.args, expr)
        return self.expr.eval(envCopy)
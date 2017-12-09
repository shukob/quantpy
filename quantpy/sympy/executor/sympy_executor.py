from sympy.physics.quantum.qapply import qapply as sympy_qapply

from quantpy.sympy.executor._quantumexecutor import BaseQuantumExecutor


class SymPyExecutor(BaseQuantumExecutor):
    def execute(self, circuit, **options):
        res = sympy_qapply(circuit, **options)
        return res

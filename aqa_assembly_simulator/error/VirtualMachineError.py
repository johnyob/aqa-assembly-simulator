from aqa_assembly_simulator.error.RuntimeError import RuntimeError


class VirtualMachineError(RuntimeError):

    def __init__(self, token, message):
        super().__init__(token, message)

    def report(self):
        return "[ERROR] Error: AssemblySimulatorVMError, Response: ({0})".format(super().report())
# test_elmo.py
# Calls various elmo circuits to test them
#
# Copyright Michael Walker 2024

from qiskit.circuit import QuantumCircuit
from qiskit.primitives import Sampler
#from qiskit.primitives import StatevectorSampler
import elmo

def test_elmo(nq_qreg) :
  symmetrize = 0
  qreg1 = [qubit for qubit in range(symmetrize+1,symmetrize+1+nq_qreg)]
  qreg2 = [qubit for qubit in range(qreg1[-1]+1,qreg1[-1]+1+nq_qreg)]
  creg0 = qreg2[-1] + 1
  creg1 = [creg0 + qubit for qubit in qreg1]
  creg2 = [creg0 + qubit for qubit in qreg2]
  qreg = [symmetrize] + qreg1 + qreg2
  creg = [creg0] + creg1 + creg2
  qc = elmo.elmo(QuantumCircuit(qreg[-1]+1),qreg1,qreg2,0)
  qc.measure_all(qreg,creg)
  qc.draw()
  #
  session = Sampler()
  #session = StatevectorSampler()
  job = session.run([(qc)])
  print(job.result())


################################################
if __name__ == "__main__" :
  test_elmo(2)


# test_elmo.py
# Calls various elmo circuits to test them
#
# Copyright Michael Walker 2024

from qiskit import QuantumCircuit
#from qiskit.primitives import sampler
from qiskit.primitives import StatevectorSampler
import elmo

def test_elmo(nq_qreg) :
  symmetrize = 0
  qreg1 = [qubit for qubit in range(symmetrize+1,symmetrize+1+nq_qreg)]
  qreg2 = [qubit for qubit in range(qreg1[-1]+1,qreg1[-1]+1+nq_qreg)]
  qc = elmo.elmo(QuantumCircuit(qreg2[-1]+1),qreg1,qreg2,0)
  qc.measure_all()
  qc.draw()
  #
  #session = sampler()
  session = StatevectorSampler()
  job = session.run([(qc)])
  print(job.result()[0])


################################################
if __name__ == "__main__" :
  test_elmo(2)


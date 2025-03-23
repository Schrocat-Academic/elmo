# test_elmo.py
# Calls various elmo circuits to test them
#
# Copyright Michael Walker 2025

from qiskit.circuit import QuantumCircuit
from qiskit.primitives import Sampler
#from qiskit.primitives import StatevectorSampler
import elmo

def test_elmo(nq_val,nq_qft) :
  qval = [qubit for qubit in range(nq_val)]
  qqft = [[qval[-1] + 1 + qindex*nq_qft + qubit for qubit in range(nq_qft)] for qindex in range(nq_val)]
  cval = [qqft[-1][-1] + 1 + qubit for qubit in qval]
  cqft = [qqft[-1][-1] + 1 + qubit for qubit in qqft]
  qreg = qval + qqft
  creg = cval + cqft
  qc = elmo.elmo(QuantumCircuit(qreg[-1]+1),qreg1,qreg2,0)
  qc.measure_all(qreg,creg)
  print(qc.draw())
  #
  #session = QuantumInstance()
  session = Sampler()
  #session = StatevectorSampler()
  job = session.run(qc)
  #job = session.execute(qc)
  #print(job.result().result.metadata[0])
  print(job.result().quasi_dists[0])


################################################
if __name__ == "__main__" :
  test_elmo(2)


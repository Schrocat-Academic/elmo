# elmo.py
# copyright Michael Walker 2024
#
# This circuit create extracts a desired (flagged) component from a given state.
# It works by creating two independent copies of the state and flipping the
# flag qubit as done for a Grover operation except:
# 1) the flip is controlled by a qubit in the |+> state,
# 2) the flipped components have their sign reversed for one copy.
# Note that the flag qubit is absorbed into the state.
# 
# A Hadamard on the controlling |+> qubit then yields the final state
# |0>|unflagged>|flagged> + |1>|flagged>|unflagged>

def elmo(qc,qreg1,qreg2,symmetrize=0) :
  qc.h(symmetrize)
  for qubit in qreg2 :
    qc.x(qubit)
  qc.h(symmetrize)
  qc.mcx(qreg2,symmetrize)
  qc.h(symmetrize)
  for qubit in qreg2 :
    qc.x(qubit)
  # Initialise qregs
  for qubit in qreg1 :
    qc.h(qubit)
  for qubit in qreg2 :
    qc.h(qubit)
  # Flag sought component |11>
  qc.h(symmetrize)
  qc.mcx(qreg2,symmetrize)
  qc.h(symmetrize)
  #
  #qc.x(symmetrize)
  qc.h(symmetrize)
  qc.mcx(qreg1,symmetrize)
  qc.h(symmetrize)
  #qc.x(symmetrize)
  # Take symmetric and antisymmetric components
  qc.h(symmetrize)

  qc.measure_all()
  return qc


**UNDER CONSTRUCTION**  
#Project Elmo#  
born of my need to economise the Grover algorithm 23/11/24

This project requires qiskit to be installed, recommended by 
pip install qiskit  

but best to consult website q-ctrl.com/qiskit/

For an arbtrary state vector whose desirable component(s) we can flag the Grover 
algorithm will rotate said vector until the flagged component(s) dominate(s), 
thus yielding it upon measurement. However, this requires the generator to be 
run backwards and forwards multiple times, driving up the circuit depth, with no
guarantee of a successful measurement. This approach generates two independent 
state vectors and separates each into a superposition of 
`|unflagged> +- |flagged>`


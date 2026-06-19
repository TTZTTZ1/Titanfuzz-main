import torch
from torch.nn import GRUCell

# Initialize the GRUCell
gru_cell = GRUCell(input_size=10, hidden_size=20)

# Input sequence and initial hidden state
input_seq = torch.randn(5, 3, 10)  # 5 time steps, 3 batches, input size 10
initial_hidden_state = torch.randn(3, 20)  # 3 batches, hidden size 20

# Process the sequence
hidden_states = []
for t in range(input_seq.size(0)):
    hidden_state = gru_cell(input_seq[t], initial_hidden_state)
    hidden_states.append(hidden_state)
    initial_hidden_state = hidden_state

# Convert list to tensor
hidden_states = torch.stack(hidden_states, dim=0)
print(hidden_states.shape)  # Should be (5, 3, 20)
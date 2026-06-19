import torch

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Input sequence and initial hidden state
input_sequence = torch.randn(5, 3, 10)  # Sequence length 5, batch size 3, feature dimension 10
initial_hidden_state = torch.randn(3, 20)  # Batch size 3, hidden state dimension 20

# Process each time step
hidden_states = []
for input_step in input_sequence:
    hidden_state = gru_cell(input_step, initial_hidden_state)
    hidden_states.append(hidden_state)
    initial_hidden_state = hidden_state

# Output the final hidden states
print(torch.stack(hidden_states))
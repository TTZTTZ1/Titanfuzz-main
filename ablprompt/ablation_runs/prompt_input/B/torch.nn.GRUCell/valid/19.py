import torch

# Define the GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Initialize hidden state
hidden_state = torch.zeros(1, 20)

# Input sequence
input_sequence = torch.randn(5, 1, 10)

# Process each time step
for input_step in input_sequence:
    hidden_state = gru_cell(input_step, hidden_state)

print(hidden_state)
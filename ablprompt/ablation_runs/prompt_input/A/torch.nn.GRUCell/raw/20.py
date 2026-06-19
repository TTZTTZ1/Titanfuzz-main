import torch
from torch.nn import GRUCell

# Initialize the GRUCell
input_size = 10
hidden_size = 20
gru_cell = GRUCell(input_size, hidden_size)

# Create random input and hidden state
input_data = torch.randn(5, input_size)  # Sequence of 5 inputs
hidden_state = torch.randn(hidden_size)   # Initial hidden state

# Perform a single step through the GRUCell
new_hidden_state = gru_cell(input_data, hidden_state)

print("New Hidden State:", new_hidden_state)
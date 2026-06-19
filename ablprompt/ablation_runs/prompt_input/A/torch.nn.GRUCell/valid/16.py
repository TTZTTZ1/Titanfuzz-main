import torch
import torch.nn as nn

# Define input and hidden size
input_size = 10
hidden_size = 20

# Create an instance of GRUCell
gru_cell = nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden state
input_data = torch.randn(1, input_size)  # Batch size of 1
hidden_state = torch.randn(1, hidden_size)

# Perform a single step through the GRU cell
new_hidden_state = gru_cell(input_data, hidden_state)

print(new_hidden_state)
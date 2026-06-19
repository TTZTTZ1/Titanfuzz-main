import torch
import torch.nn as nn

# Define input size, hidden size, and batch size
input_size = 10
hidden_size = 20
batch_size = 5

# Create a GRUCell instance
gru_cell = nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden state
input_data = torch.randn(batch_size, input_size)
hidden_state = torch.zeros(batch_size, hidden_size)

# Perform a single step of GRU computation
new_hidden_state = gru_cell(input_data, hidden_state)

print(new_hidden_state.shape)  # Should print: torch.Size([5, 20])
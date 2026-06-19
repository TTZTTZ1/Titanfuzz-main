import torch
import torch.nn as nn

# Define input size, hidden size, and number of layers
input_size = 10
hidden_size = 20
num_layers = 1

# Initialize GRU cell
gru_cell = nn.GRUCell(input_size, hidden_size)

# Create random input tensor
input_tensor = torch.randn(1, input_size)

# Initialize hidden state
hidden_state = torch.zeros(1, hidden_size)

# Perform forward pass through GRU cell
output = gru_cell(input_tensor, hidden_state)

print(output)
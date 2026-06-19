import torch
import torch.nn as nn

# Define input size, hidden size, and number of layers for GRUCell
input_size = 10
hidden_size = 20
num_layers = 1

# Initialize the GRUCell
gru_cell = nn.GRUCell(input_size, hidden_size)

# Create a random input tensor and an initial hidden state
input_tensor = torch.randn(1, input_size)
hidden_state = torch.randn(1, hidden_size)

# Perform a forward pass through the GRUCell
new_hidden_state = gru_cell(input_tensor, hidden_state)

print(new_hidden_state)
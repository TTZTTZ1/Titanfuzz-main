import torch
import torch.nn as nn

# Define input size, hidden size, and number of layers
input_size = 10
hidden_size = 20

# Create an instance of GRUCell
gru_cell = nn.GRUCell(input_size, hidden_size)

# Generate random input tensor
input_tensor = torch.randn(1, input_size)  # batch_size=1 for simplicity

# Initialize hidden state
hidden_state = torch.zeros(1, hidden_size)

# Perform a single step through the GRUCell
output = gru_cell(input_tensor, hidden_state)

print("Output:", output)
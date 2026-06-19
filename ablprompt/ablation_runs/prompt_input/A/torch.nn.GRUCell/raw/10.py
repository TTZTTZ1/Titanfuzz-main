import torch
import torch.nn as nn

# Define input size, hidden size, and batch size
input_size = 10
hidden_size = 20
batch_size = 5

# Create an instance of GRUCell
gru_cell = nn.GRUCell(input_size, hidden_size)

# Initialize input and hidden state
input_data = torch.randn(batch_size, input_size)
hidden_state = torch.randn(batch_size, hidden_size)

# Perform a single step of GRUCell computation
output = gru_cell(input_data, hidden_state)

print(output)
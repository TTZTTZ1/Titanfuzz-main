import torch
import torch.nn as nn

# Define the input size, hidden size, and number of layers
input_size = 10
hidden_size = 20
num_layers = 2

# Initialize the GRUCell
gru_cell = nn.GRUCell(input_size, hidden_size)

# Create random input and initial hidden state
batch_size = 5
input_tensor = torch.randn(batch_size, input_size)
hidden_state = torch.randn(batch_size, hidden_size)

# Process multiple time steps
for i in range(3):
    hidden_state = gru_cell(input_tensor, hidden_state)

print(hidden_state)
import torch
from torch.nn import GRU

# Define the model
input_size = 10
hidden_size = 20
num_layers = 2
gru = GRU(input_size, hidden_size, num_layers)

# Prepare input data
batch_size = 3
sequence_length = 5
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass
output, _ = gru(input_data)

print(output.shape)  # Should be (sequence_length, batch_size, hidden_size)
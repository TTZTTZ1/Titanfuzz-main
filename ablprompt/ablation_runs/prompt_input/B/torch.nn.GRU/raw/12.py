import torch
from torch.nn import GRU

# Define the GRU model
input_size = 10
hidden_size = 20
num_layers = 2
gru = GRU(input_size, hidden_size, num_layers)

# Create a random input tensor
batch_size = 3
sequence_length = 5
input_tensor = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the GRU
output, hidden_state = gru(input_tensor)

print("Output:", output)
print("Hidden State:", hidden_state)
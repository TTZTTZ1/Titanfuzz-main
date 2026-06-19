import torch
from torch.nn import GRU

# Define model parameters
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
sequence_length = 5

# Create a random input tensor
input_tensor = torch.randn(sequence_length, batch_size, input_size)

# Initialize the GRU layer
gru_layer = GRU(input_size, hidden_size, num_layers, batch_first=True)

# Forward pass through the GRU layer
output, hidden_state = gru_layer(input_tensor)

print("Output:", output.shape)
print("Hidden State:", hidden_state.shape)
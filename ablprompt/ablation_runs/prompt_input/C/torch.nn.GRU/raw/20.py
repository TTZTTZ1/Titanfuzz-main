import torch
from torch.nn import GRU

# Define the parameters
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
sequence_length = 5

# Create an instance of GRU
gru = GRU(input_size, hidden_size, num_layers, batch_first=True)

# Generate random input data
input_data = torch.randn(sequence_length, batch_size, input_size)

# Initialize hidden state
h0 = torch.zeros(num_layers * 1, batch_size, hidden_size)  # 1 because not bidirectional

# Forward pass through GRU
output, hn = gru(input_data, h0)

print("Output shape:", output.shape)
print("Hidden state shape:", hn.shape)
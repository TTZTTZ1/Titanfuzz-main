import torch
from torch.nn import GRU

# Define the model
input_size = 10
hidden_size = 20
num_layers = 2
gru = GRU(input_size, hidden_size, num_layers)

# Prepare the input data
batch_size = 3
sequence_length = 5
input_data = torch.randn(sequence_length, batch_size, input_size)

# Initialize the hidden state
h0 = torch.zeros(num_layers, batch_size, hidden_size)

# Forward pass through the GRU
output, hn = gru(input_data, h0)

print("Output:", output.shape)
print("Hidden State:", hn.shape)
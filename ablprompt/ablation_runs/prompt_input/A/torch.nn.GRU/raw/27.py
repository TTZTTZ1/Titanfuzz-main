import torch

# Define input parameters
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 32
seq_length = 5

# Create random input tensor
inputs = torch.randn(seq_length, batch_size, input_size)

# Initialize GRU layer
gru = torch.nn.GRU(input_size, hidden_size, num_layers)

# Forward pass through GRU
outputs, _ = gru(inputs)

print(outputs.shape)  # Should print: torch.Size([5, 32, 20])
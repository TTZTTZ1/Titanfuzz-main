import torch

# Define input parameters
input_size = 10
hidden_size = 20
batch_size = 5
num_layers = 2

# Create an instance of GRU
gru = torch.nn.GRU(input_size, hidden_size, num_layers)

# Generate random input data
input_data = torch.randn(seq_len, batch_size, input_size)
h0 = torch.randn(num_layers, batch_size, hidden_size)

# Forward pass through GRU
output, hn = gru(input_data, h0)

print("Output shape:", output.shape)
print("Hidden state shape:", hn.shape)
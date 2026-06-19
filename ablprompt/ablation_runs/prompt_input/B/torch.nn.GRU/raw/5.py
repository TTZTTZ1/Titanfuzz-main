import torch
from torch.nn import GRU

# Define the GRU model
gru = GRU(input_size=10, hidden_size=20, num_layers=2, batch_first=True, bidirectional=True)

# Create random input tensor
input_tensor = torch.randn(5, 3, 10)

# Initialize hidden state
h0 = torch.randn(4, 3, 20)  # 4 = 2*num_layers * bidirectional

# Forward pass through the GRU
output, h_n = gru(input_tensor, h0)

print("Output:", output.shape)
print("Final Hidden State:", h_n.shape)
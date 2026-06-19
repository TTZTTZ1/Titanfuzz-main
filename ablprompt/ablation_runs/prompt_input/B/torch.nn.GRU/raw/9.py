import torch
from torch.nn import GRU

# Define the GRU model
gru_model = GRU(input_size=128, hidden_size=64, num_layers=3, batch_first=True, bidirectional=True)

# Create a random input tensor
input_tensor = torch.randn(10, 32, 128)

# Initialize hidden state
if gru_model.bidirectional:
    h0 = torch.randn(gru_model.num_layers * 2, input_tensor.size(0), gru_model.hidden_size)
else:
    h0 = torch.randn(gru_model.num_layers, input_tensor.size(0), gru_model.hidden_size)

# Forward pass through the GRU
output, h_n = gru_model(input_tensor, h0)

print("Output shape:", output.shape)
print("Final hidden state shape:", h_n.shape)
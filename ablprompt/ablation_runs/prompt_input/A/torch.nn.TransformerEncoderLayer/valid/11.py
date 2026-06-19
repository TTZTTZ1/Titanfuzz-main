import torch
from torch.nn import TransformerEncoderLayer

# Define the model parameters
d_model = 512
nhead = 8
dim_feedforward = 2048
dropout = 0.1

# Create an instance of TransformerEncoderLayer
transformer_encoder_layer = TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout)

# Example input tensor (batch_size, seq_len, d_model)
input_tensor = torch.randn(32, 10, 512)

# Pass the input through the transformer encoder layer
output_tensor = transformer_encoder_layer(input_tensor)

print(output_tensor.shape)  # Should print: torch.Size([32, 10, 512])
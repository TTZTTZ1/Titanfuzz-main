import torch
from torch.nn import TransformerEncoderLayer

# Define a sample input tensor and mask
input_tensor = torch.randn(10, 32, 512)  # (sequence_length, batch_size, embedding_dim)
src_mask = None  # You can define a mask if needed

# Initialize the TransformerEncoderLayer
encoder_layer = TransformerEncoderLayer(d_model=512, nhead=8)

# Pass the input through the encoder layer
output = encoder_layer(input_tensor, src_mask)

print(output.shape)  # Should print: torch.Size([10, 32, 512])
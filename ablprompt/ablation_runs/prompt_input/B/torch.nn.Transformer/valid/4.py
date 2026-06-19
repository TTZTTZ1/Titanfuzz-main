import torch
from torch.nn import Transformer, TransformerEncoderLayer, TransformerDecoderLayer

# Define the model parameters
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'

# Create an instance of the Transformer model
model = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers,
                    num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward,
                    dropout=dropout, activation=activation)

# Dummy data for demonstration
src = torch.rand((10, 32, 512))
tgt = torch.rand((20, 32, 512))

# Generate a square subsequent mask for the decoder
tgt_mask = model.generate_square_subsequent_mask(tgt.size(0)).to(device=tgt.device)

# Forward pass through the model
output = model(src, tgt, tgt_mask=tgt_mask)

print(output.shape)  # Should be (20, 32, 512)
import torch
from torch.nn import Transformer

# Define model parameters
d_model = 256
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1
activation = 'relu'
batch_first = True

# Initialize the Transformer model
transformer = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers,
                          num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward,
                          dropout=dropout, activation=activation, batch_first=batch_first)

# Create dummy input tensors
src = torch.rand((10, 32, d_model))
tgt = torch.rand((20, 32, d_model))

# Generate a square subsequent mask for the decoder
tgt_mask = torch.nn.Transformer.generate_square_subsequent_mask(tgt.size(0), device=tgt.device)

# Forward pass through the transformer
output = transformer(src, tgt, tgt_mask=tgt_mask)

print(output.shape)  # Should be (20, 32, d_model)
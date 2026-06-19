import torch
from torch.nn import Transformer, MultiHeadAttention, Linear, LayerNorm

# Define a simple model using Transformer
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, output_dim):
        super(SimpleTransformerModel, self).__init__()
        self.transformer = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers, num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward)
        self.fc_out = Linear(d_model, output_dim)
        self.norm = LayerNorm(d_model)

    def forward(self, src, tgt):
        # Ensure inputs are in the correct shape
        assert src.dim() == 3 and tgt.dim() == 3, "Inputs must be 3D tensors (seq_len, batch_size, embedding_dim)"
        
        # Pass through transformer
        output = self.transformer(src, tgt)
        
        # Final linear transformation
        output = self.fc_out(output)
        output = self.norm(output)
        
        return output

# Initialize the model
model = SimpleTransformerModel(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, dim_feedforward=2048, output_dim=10)

# Dummy input data
src = torch.rand((10, 32, 512))
tgt = torch.rand((10, 32, 512))

# Forward pass
output = model(src, tgt)
print(output.shape)  # Should print: torch.Size([10, 32, 10])
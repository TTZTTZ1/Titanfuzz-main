import torch
from torch.nn import Transformer, MultiHeadAttention

# Define a custom encoder layer
class CustomEncoderLayer(torch.nn.Module):
    def __init__(self, d_model, nhead):
        super(CustomEncoderLayer, self).__init__()
        self.self_attn = MultiHeadAttention(d_model, nhead)
        self.linear1 = torch.nn.Linear(d_model, 2048)
        self.dropout = torch.nn.Dropout(0.1)
        self.linear2 = torch.nn.Linear(2048, d_model)
        self.norm1 = torch.nn.LayerNorm(d_model)
        self.norm2 = torch.nn.LayerNorm(d_model)

    def forward(self, src, src_mask=None, src_key_padding_mask=None):
        src2 = self.self_attn(src, src, src, attn_mask=src_mask, key_padding_mask=src_key_padding_mask)[0]
        src = src + self.dropout(src2)
        src = self.norm1(src)
        src2 = self.linear2(self.dropout(torch.relu(self.linear1(src))))
        src = src + self.dropout(src2)
        src = self.norm2(src)
        return src

# Create a custom encoder
custom_encoder = torch.nn.Sequential(
    CustomEncoderLayer(512, 8),
    CustomEncoderLayer(512, 8)
)

# Create a custom decoder
custom_decoder = torch.nn.Sequential(
    CustomDecoderLayer(512, 8),
    CustomDecoderLayer(512, 8)
)

# Initialize the Transformer model with custom encoder and decoder
transformer = Transformer(d_model=512, nhead=8, num_encoder_layers=6, num_decoder_layers=6, custom_encoder=custom_encoder, custom_decoder=custom_decoder)

# Generate sample inputs
src = torch.rand((10, 32, 512))
tgt = torch.rand((20, 32, 512))

# Forward pass
output = transformer(src, tgt)
print(output.shape)  # Should be (20, 32, 512)
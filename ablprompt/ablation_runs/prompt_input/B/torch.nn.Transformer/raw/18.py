import torch
from torch.nn import Transformer, LayerNorm, Linear
from torch.nn.functional import gelu

class CustomTransformer(nn.Module):
    def __init__(self, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout):
        super(CustomTransformer, self).__init__()
        self.transformer = Transformer(d_model=d_model, nhead=nhead, num_encoder_layers=num_encoder_layers,
                                       num_decoder_layers=num_decoder_layers, dim_feedforward=dim_feedforward, dropout=dropout)
        self.linear_out = Linear(d_model, d_model)

    def forward(self, src, tgt, src_mask=None, tgt_mask=None, memory_mask=None, src_key_padding_mask=None,
                tgt_key_padding_mask=None, memory_key_padding_mask=None):
        output = self.transformer(src, tgt, src_mask=src_mask, tgt_mask=tgt_mask, memory_mask=memory_mask,
                                  src_key_padding_mask=src_key_padding_mask, tgt_key_padding_mask=tgt_key_padding_mask,
                                  memory_key_padding_mask=memory_key_padding_mask)
        return self.linear_out(output)

# Example usage
d_model = 512
nhead = 8
num_encoder_layers = 6
num_decoder_layers = 6
dim_feedforward = 2048
dropout = 0.1

model = CustomTransformer(d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, dropout)
src = torch.rand((10, 32, 512))
tgt = torch.rand((20, 32, 512))

output = model(src, tgt)
print(output.shape)  # Should be (20, 32, 512)
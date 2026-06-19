```python
import torch
from torch.nn import Transformer, LayerNorm, Linear

# Define a simple model using Transformer
class SimpleTransformerModel(torch.nn.Module):
    def __init__(self, d_model, nhead, num_encoder_layers, num_decoder_layers, dim_feedforward, output_dim):
        super(SimpleTransformerModel, self).__init__()
        self.model_type = 'Transformer'
        self.pos_encoder = PositionalEncoding(d_model, 0.1)
        encoder_layers = nn.TransformerEncoderLayer(d_model, nhead, dim_feedforward, dropout=0.5)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layers, num_encoder_layers)
        decoder_layers = nn.TransformerDecoderLayer(d_model, nhead, dim_feedforward, dropout=0.5)
        self.transformer_decoder = nn.TransformerDecoder(decoder_layers, num_decoder_layers)
        self.encoder = nn.Embedding(1000, d_model)
        self.decoder = nn.Linear(d_model, output_dim)
        self.d_model = d_model
        self.nhead = nhead

    def forward(self, src, tgt, src_mask=None, tgt_mask=None, memory_mask=None,
                src_key_padding_mask=None, tgt_key_padding_mask=None, memory_key_padding_mask=None):
        src = self.encoder(src) * torch.sqrt(torch.tensor(self.d_model, dtype=torch.float32))
        src = self.pos_encoder(src)
        tgt = self.encoder(tgt) * torch.sqrt(torch.tensor(self.d_model, dtype=torch.float32))
        tgt = self.pos_encoder(tgt)
        output = self.transformer_decoder(tgt, src, memory_mask=memory_mask,
                                           tgt_mask=tgt_mask, memory_key_padding_mask=memory_key_padding_mask,
                                           tgt_key_padding_mask=tgt_key_padding_mask)
        output = self.decoder(output)
        return output

class PositionalEncoding(nn.Module):
    def __init__(self, d_model, dropout=0.1, max_len=5000):
        super(PositionalEncoding, self).__init__()
        self.dropout = nn.Dropout(p=dropout)

        pe = torch.zeros(max_len, d_model)
        position = torch.arange(0, max_len, dtype=torch.float).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-torch.log(torch.tensor(10000.0)) / d_model))
        pe[:, 0::2] =
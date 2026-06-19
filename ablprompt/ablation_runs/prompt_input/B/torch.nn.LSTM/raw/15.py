import torch
import torch.nn as nn

# Define an LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False, proj_size=0):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional, proj_size=proj_size)
    
    def forward(self, x, h0=None, c0=None):
        out, _ = self.lstm(x, (h0, c0))
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
bidirectional = True
proj_size = 10

model = LSTMModel(input_size, hidden_size, num_layers, bidirectional, proj_size)

# Dummy input tensor
input_tensor = torch.randn(5, 3, 10)  # (seq_len=5, batch=3, input_size=10)
h0 = torch.randn(num_layers * (2 if bidirectional else 1), 3, proj_size if proj_size > 0 else hidden_size)  # (num_layers*(2 if bidirectional else 1), batch, hidden_size or proj_size)
c0 = torch.randn(num_layers * (2 if bidirectional else 1), 3, proj_size if proj_size > 0 else hidden_size)  # (num_layers*(2 if bidirectional else 1), batch, hidden_size or proj_size)

output = model(input_tensor, h0, c0)
print(output.shape)  # Should print: torch.Size([5, 3, 20])
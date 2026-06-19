import torch
import torch.nn as nn

# Define an LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False, proj_size=0):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, bidirectional=bidirectional, proj_size=proj_size)
    
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

# Create random input tensor
seq_length = 5
batch_size = 3
x = torch.randn(seq_length, batch_size, input_size)

# Initialize hidden and cell states
h0 = torch.randn(num_layers * (2 if bidirectional else 1), batch_size, proj_size if proj_size > 0 else hidden_size)
c0 = torch.randn(num_layers * (2 if bidirectional else 1), batch_size, proj_size if proj_size > 0 else hidden_size)

# Forward pass
output = model(x, h0, c0)
print(output.shape)  # Should print: torch.Size([5, 3, 10])
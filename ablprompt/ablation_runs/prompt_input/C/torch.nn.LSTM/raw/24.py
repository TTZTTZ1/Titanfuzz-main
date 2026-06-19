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
batch_size = 3
sequence_length = 5

model = LSTMModel(input_size, hidden_size, num_layers, bidirectional=True, proj_size=10)

# Create dummy input
x = torch.randn(sequence_length, batch_size, input_size)

# Forward pass
output = model(x)
print(output.shape)  # Should print: torch.Size([5, 3, 40]) for bidirectional with proj_size=10
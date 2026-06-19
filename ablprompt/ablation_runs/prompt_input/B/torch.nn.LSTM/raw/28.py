import torch
import torch.nn as nn

# Define an LSTM model
class LSTMModel(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False, proj_size=0):
        super(LSTMModel, self).__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional, proj_size=proj_size)
    
    def forward(self, x):
        h0 = torch.zeros(num_layers * (2 if bidirectional else 1), x.size(0), hidden_size).to(x.device)
        c0 = torch.zeros(num_layers * (2 if bidirectional else 1), x.size(0), hidden_size).to(x.device)
        out, _ = self.lstm(x, (h0, c0))
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
bidirectional = True
proj_size = 10

model = LSTMModel(input_size, hidden_size, num_layers, bidirectional, proj_size)
input_data = torch.randn(5, 3, input_size)
output = model(input_data)
print(output.shape)  # Should print: torch.Size([5, 3, 10])
import torch
import torch.nn as nn

# Define an LSTM model
class SimpleLSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        
    def forward(self, x):
        # Initialize hidden state and cell state
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))  # out: tensor of shape (batch_size, seq_length, hidden_size)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
seq_length = 5

model = SimpleLSTM(input_size, hidden_size, num_layers)
input_data = torch.randn(batch_size, seq_length, input_size)

output = model(input_data)
print(output.shape)  # Should print torch.Size([3, 5, 20])
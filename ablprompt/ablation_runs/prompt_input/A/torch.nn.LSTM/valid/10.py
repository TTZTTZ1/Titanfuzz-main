import torch
import torch.nn as nn

# Define an LSTM model
class SimpleLSTM(nn.Module):
    def __init__(self, input_size=10, hidden_size=20, num_layers=1):
        super(SimpleLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        
    def forward(self, x):
        # Initialize hidden state and cell state
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # Forward propagate LSTM
        out, _ = self.lstm(x, (h0, c0))
        return out

# Example usage
input_seq = torch.randn(5, 3, 10)  # (sequence length, batch size, input size)
lstm_model = SimpleLSTM()
output = lstm_model(input_seq)
print(output.shape)  # Should print: torch.Size([5, 3, 20])
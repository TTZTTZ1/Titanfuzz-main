import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity='relu', batch_first=True, bidirectional=bidirectional)
    
    def forward(self, x):
        # Initialize hidden state
        h0 = torch.zeros(self.rnn.num_layers * (2 if self.rnn.bidirectional else 1), x.size(0), self.rnn.hidden_size).to(x.device)
        
        # Forward propagate RNN
        out, _ = self.rnn(x, h0)
        return out

# Example usage
if __name__ == "__main__":
    input_size = 10
    hidden_size = 20
    num_layers = 2
    bidirectional = True
    
    model = SimpleRNN(input_size, hidden_size, num_layers, bidirectional)
    input_data = torch.randn(5, 3, input_size)  # Batch size of 3, sequence length of 5, input size of 10
    output = model(input_data)
    print(output.shape)  # Should be (5, 3, 40) for bidirectional RNN
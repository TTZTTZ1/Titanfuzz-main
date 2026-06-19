import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh', bidirectional=False):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, 
                          nonlinearity=nonlinearity, bidirectional=bidirectional)
    
    def forward(self, x):
        # Initialize hidden state
        h0 = torch.zeros(self.rnn.num_layers, x.size(0), self.rnn.hidden_size).to(x.device)
        
        # Forward propagate RNN
        out, _ = self.rnn(x, h0)
        return out

# Example usage
if __name__ == "__main__":
    input_size = 10
    hidden_size = 20
    num_layers = 2
    sequence_length = 5
    batch_size = 3
    
    # Create random input data
    x = torch.randn(sequence_length, batch_size, input_size)
    
    # Create the RNN model
    rnn_model = SimpleRNN(input_size, hidden_size, num_layers)
    
    # Forward pass
    output = rnn_model(x)
    print(output.shape)  # Should be (sequence_length, batch_size, hidden_size*num_directions)
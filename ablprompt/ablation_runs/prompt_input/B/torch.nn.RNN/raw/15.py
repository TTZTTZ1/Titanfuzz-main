import torch
import torch.nn as nn

# Define an RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x):
        # Initialize hidden state
        h0 = torch.zeros(num_layers, x.size(0), hidden_size).to(x.device)
        
        # Forward propagate RNN
        out, _ = self.rnn(x, h0)
        return out

# Example usage
if __name__ == "__main__":
    input_size = 10
    hidden_size = 20
    num_layers = 2
    sequence_length = 3
    batch_size = 5
    
    # Create random input data
    input_data = torch.randn(sequence_length, batch_size, input_size)
    
    # Create model
    model = SimpleRNN(input_size, hidden_size, num_layers)
    
    # Forward pass
    output = model(input_data)
    print(output.shape)  # Expected shape: (sequence_length, batch_size, hidden_size)
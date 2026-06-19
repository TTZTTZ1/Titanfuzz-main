import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers=num_layers, nonlinearity=nonlinearity)
    
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
    sequence_length = 5
    batch_size = 3
    
    # Create random input data
    x = torch.randn(sequence_length, batch_size, input_size)
    
    # Create an instance of the RNN model
    rnn_model = SimpleRNN(input_size, hidden_size)
    
    # Forward pass through the RNN
    output = rnn_model(x)
    
    print(output.shape)  # Should be (sequence_length, batch_size, hidden_size)
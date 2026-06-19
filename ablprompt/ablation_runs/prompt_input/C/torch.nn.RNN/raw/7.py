import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x):
        # Initialize hidden state
        h0 = torch.zeros(self.rnn.num_layers, x.size(0), self.rnn.hidden_size).to(x.device)
        
        # Forward propagate RNN
        out, _ = self.rnn(x, h0)
        return out

# Example usage
if __name__ == "__main__":
    # Input sequence length, batch size, input size
    seq_length = 5
    batch_size = 3
    input_size = 4
    
    # Create random input data
    input_data = torch.randn(seq_length, batch_size, input_size)
    
    # Define model parameters
    hidden_size = 8
    num_layers = 2
    nonlinearity = 'relu'
    
    # Initialize the RNN model
    rnn_model = SimpleRNN(input_size, hidden_size, num_layers, nonlinearity)
    
    # Forward pass
    output = rnn_model(input_data)
    print(output.shape)  # Should be (seq_length, batch_size, hidden_size)
import torch

# Define the RNN model
class SimpleRNN(torch.nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = torch.nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x, hx=None):
        return self.rnn(x, hx)

# Create an instance of the RNN model
input_size = 10
hidden_size = 20
num_layers = 3
rnn_model = SimpleRNN(input_size, hidden_size, num_layers)

# Generate random input data
batch_size = 5
sequence_length = 4
x = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output, h_n = rnn_model(x)

print("Output:", output.shape)
print("Final Hidden State:", h_n.shape)
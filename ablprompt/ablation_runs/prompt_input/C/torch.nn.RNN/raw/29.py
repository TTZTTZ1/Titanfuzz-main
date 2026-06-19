import torch

# Define the RNN model
rnn = torch.nn.RNN(input_size=10, hidden_size=20, num_layers=2, nonlinearity='relu', batch_first=True, bidirectional=True, dropout=0.5)

# Create some random input data
input_data = torch.randn(3, 4, 10)  # Sequence length=3, Batch size=4, Input size=10

# Initialize the hidden state
hidden_state = torch.zeros(4, 4, 20)  # Num layers*directions=4, Batch size=4, Hidden size=20

# Forward pass through the RNN
output, hidden_state = rnn(input_data, hidden_state)

print(output.shape)  # Should be (3, 4, 40)
print(hidden_state.shape)  # Should be (8, 4, 20)
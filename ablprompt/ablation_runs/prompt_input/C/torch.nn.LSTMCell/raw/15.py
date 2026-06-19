import torch

# Define the LSTMCell parameters
input_size = 10
hidden_size = 20
num_layers = 3
batch_size = 5
seq_len = 6

# Initialize the LSTMCell
lstm_cell = torch.nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)

# Create random input and hidden/cell states
input_data = torch.randn(seq_len, batch_size, input_size)
h0 = torch.randn(num_layers, batch_size, hidden_size)
c0 = torch.randn(num_layers, batch_size, hidden_size)

# Forward pass through the LSTMCell
output, (hn, cn) = lstm_cell(input_data, (h0, c0))

print(output.shape)  # Should be (seq_len, batch_size, hidden_size)
print(hn.shape)      # Should be (num_layers, batch_size, hidden_size)
print(cn.shape)      # Should be (num_layers, batch_size, hidden_size)
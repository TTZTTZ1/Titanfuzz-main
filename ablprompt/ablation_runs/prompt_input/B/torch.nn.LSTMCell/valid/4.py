import torch

# Define the dimensions
input_size = 10
hidden_size = 20
batch_size = 5
seq_length = 3

# Create random input and initial states
input_data = torch.randn(seq_length, batch_size, input_size)
h0 = torch.zeros(batch_size, hidden_size)
c0 = torch.zeros(batch_size, hidden_size)

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Process each time step
for i in range(seq_length):
    h0, c0 = lstm_cell(input_data[i], (h0, c0))

print("Final hidden state:", h0)
print("Final cell state:", c0)
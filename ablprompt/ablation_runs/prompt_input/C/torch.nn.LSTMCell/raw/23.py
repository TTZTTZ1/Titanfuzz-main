import torch

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_time_steps = 5

# Create an instance of LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Initialize input and hidden states
input_data = torch.randn(num_time_steps, input_size)
h0 = torch.zeros(1, hidden_size)
c0 = torch.zeros(1, hidden_size)

# Forward pass through the LSTMCell
for i in range(num_time_steps):
    h0, c0 = lstm_cell(input_data[i], (h0, c0))

print("Final hidden state:", h0)
print("Final cell state:", c0)
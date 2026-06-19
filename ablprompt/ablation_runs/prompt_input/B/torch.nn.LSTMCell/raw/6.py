import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial states
input_data = torch.randn(5, input_size)  # 5 timesteps, each with input size 10
h0 = torch.zeros(5, hidden_size)        # Initial hidden state
c0 = torch.zeros(5, hidden_size)        # Initial cell state

# Process input through LSTMCell
for i in range(input_data.size(0)):
    h0, c0 = lstm_cell(input_data[i], (h0, c0))

print("Final hidden state:", h0)
print("Final cell state:", c0)
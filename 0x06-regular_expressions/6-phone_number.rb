#!/usr/bin/env ruby
# Function to find all occurrences of strings consisting of 1 to 10 digits
def find_digits(input)
  input.scan(/^\d{1,10}$/)
end

# Extract the first argument from the command-line arguments
input_string = ARGV[0]

# Call the function to find occurrences and join them
puts find_digits(input_string).join

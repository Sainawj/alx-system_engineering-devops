#!/usr/bin/env ruby
# Function to find all occurrences of specific patterns in the input string
def find_patterns(input)
  input.scan(/(?<=from|to|flags):(\+?\w+|[-?[0-1]:?]+)/)
end

# Extract the first argument from the command-line arguments
input_string = ARGV[0]

# Call the function to find occurrences and join them
puts find_patterns(input_string).join(',')

#!/usr/bin/env ruby

sequence = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
puts ARGV[0].scan(sequence).join(",")

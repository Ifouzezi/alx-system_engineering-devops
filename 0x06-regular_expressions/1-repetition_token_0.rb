#!/usr/bin/env ruby

sequence = /hbt{2,5}n/
puts ARGV[0].scan(sequence).join

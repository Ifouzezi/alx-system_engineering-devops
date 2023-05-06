#!/usr/bin/env ruby

sequence = /^\d{10,10}$/
puts ARGV[0].scan(sequence).join

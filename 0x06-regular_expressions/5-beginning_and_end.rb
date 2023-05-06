#!/usr/bin/env ruby

sequence = /^h.n$/
puts ARGV[0].scan(sequence).join

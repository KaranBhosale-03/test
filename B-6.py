#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:09:23 2023

@author: karanbhosale
"""
#B-6
import random
num_spins = 10000
red_slots = 18
black_slots = 18
green_slots = 2
wins = 0
for _ in range(num_spins):
    spin = random.randint(1, 38)

    if spin <= red_slots:
        wins += 1
win_probability = wins / num_spins
print("Probability of winning on any given spin:", win_probability)

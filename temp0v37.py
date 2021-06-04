#!/usr/local/bin/python
# Program test0.py for tensorflow check
print ("Test program to check tensorflow test0.py ")

import numpy as nm
import pandas as pd
import scipy as sc
import matplotlib.pyplot as plt


print ("imported numpy(nm), pandas(pd), scipy(sc) ")
import tensorflow as tf
print ("imported tensorflow(tf)")

c = tf.constant("Hello World!!")
with tf.Session() as sess:
       print (sess.run(c))

# Create a graph
g = tf.Graph()

# Establish Graph as the default graph
with g.as_default():
    # Assemble a graph consisting of the following 3 operands
    #  * Two tf.constant operation to create the operands
    #  * One tf.add operation to add the two operands
    x = tf.constant(8, name="x_const")
    y = tf.constant(5, name="y_const")
    my_sum = tf.add(x, y, name="x_y_sum")

    # Now create s session
    # The session will run the default graph
    with tf.Session() as sess:
        print (my_sum.eval())

print (" end of pgm test0.py for imports ")
print (" added extra line to enhance s/w characteristics -- Starwars")
print (" added another line for Luke Skywalker ")
print (" added another line for Darth Vader, even though he no longer exists in Nov 2020")


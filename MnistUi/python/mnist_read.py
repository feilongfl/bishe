
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import os

import tensorflow as tf
import numpy as np
from PIL import Image

# Create the model
x = tf.placeholder(tf.float32, [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.matmul(x, W) + b

# Define loss and optimizer
y_ = tf.placeholder(tf.float32, [None, 10])

# The raw formulation of cross-entropy,
#
#   tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(tf.nn.softmax(y)),
#                                 reduction_indices=[1]))
#
# can be numerically unstable.
#
# So here we use tf.nn.softmax_cross_entropy_with_logits on the raw
# outputs of 'y', and then average across the batch.
cross_entropy = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_, logits=y))
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()
# Train
#for _ in range(1000):
#batch_xs, batch_ys = mnist.train.next_batch(100)
#sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

#load
saver = tf.train.Saver()
model_path = "./python/model.ckpt"
saver.restore(sess, model_path)
#print("restore")

ans=tf.argmax(y, 1)
#print("answer");
arr=[]
img = Image.open('./data/data.min.png').convert('L')
for i in range(28):
    for j in range(28):
        # mnist 里的颜色是0代表白色（背景），1.0代表黑色
        pixel = 1.0 - float(img.getpixel((j, i)))/255.0
        arr.append(pixel)

num = sess.run(ans, feed_dict = {x:np.array(arr).reshape((1, 784))});
print(num[0])

"""
# Import data
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)
# Test trained model
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))



print(sess.run(accuracy, feed_dict={x: mnist.test.images,
                                    y_: mnist.test.labels}))

#write log
writer = tf.summary.FileWriter("log", tf.get_default_graph())
writer.close()
"""

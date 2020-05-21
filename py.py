import tensorflow.compat.v1 as tf
import os

tf.disable_v2_behavior()
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

graph = tf.Graph()
with graph.as_default():
    x = tf.constant(5, name="x")
    y = tf.constant(1, name="y")
    sum = tf.add(x,y, name="x_y")

    with tf.Session() as Session:
        print("hasil : ",sum.eval())

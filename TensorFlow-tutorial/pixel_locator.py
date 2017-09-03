# Freddy @Terminal 1, Capital Airport, Beijing
# Sep 2, 2017
import tensorflow as tf
import numpy as np
from os import sys
import time
import cv2


def pixel_locator():
    '''
    f: focal distance, 
    p: position of the camera, 
    v: direction of the camera(from center of camera to focal point)
    x: point cloud
    '''
    x = tf.placeholder(tf.float32,[None,3])
    p = tf.placeholder(tf.float32,[None,3])
    v = tf.placeholder(tf.float32,[None,3])
    f = tf.placeholder(tf.float32,[None,1])
    divider = tf.reduce_sum( (p - x) * v , axis=0, keep_dims=True) + 1 
    result = f * v - f * f * f * (p + f * v - x) / divider

    return result, x, p, v,f


def timeit(func, *args, **kwargs):
    s = time.time()
    func(*args, **kwargs)
    e = time.time()
    print("USE <\033[1;32m%.2f\033[0m> s" % (e - s))

def data_loader(address):
    print("load data...")
    original_data = np.loadtxt(address)
    print("load complete")
    print("------data stats------")
    print("max x: %f max y: %f max z: %f" % (max(original_data[:,0]),max(original_data[:,1]), max(original_data[:,2])))
    print("min x: %f min y: %f min z: %f" % (min(original_data[:,0]),min(original_data[:,1]), min(original_data[:,2])))
    return original_data


def parameter_setting(original_data):
    photo_center = np.array([max(original_data[:,0])*1.2,max(original_data[:,1])*1.2, max(original_data[:,2])*1.3])
    focal_dir = np.array( [0 , 0 , max(original_data[:,2])*1.5 ] )
    focal_distance = (max(original_data[:,2]) - min(original_data[:,2]))*0.3
    return photo_center, focal_dir, focal_distance



def generate_photo(data, a, b, v, o):
    '''
    data:
    a: length
    b: width
    v: direction of the camera(from center of camera to focal point)
    o: positive direction of the photo
    '''
    #data = data.eval
    #v = v.eval
    #o = o.eval
    #photo = np.zeros([a, b, 3])
    photo = tf.zeros([a, b, 3])
    #xs = np.sum(data[:, :3] * o, axis=1)
    xs = tf.reduce_sum(data[:, :3] * o, axis=1)
    #ys = np.sum(data[:, :3] * np.cross(o, v), axis=1)
    ys = tf.reduce_sum(data[:, :3] * tf.cross(o, v), axis=1)
    #ys = (b - 1) * (ys - ys.min()) / (ys.max() - ys.min())
    #xs = (a - 1) * (xs - xs.min()) / (xs.max() - xs.min())

    print("xs.shape:", xs.shape)
    for i in range(xs.shape[0]):
        photo[xs[i], ys[i], :] = data[i, 3:6]
        # print(photo[int(x), int(y), :])
    return photo

#def str2vec(s):

def main():
    original_data = data_loader(sys.argv[1])
    data,x,p,v,f = pixel_locator()

    photo_center, focal_dir, focal_distance = parameter_setting(original_data)
    
    init = tf.global_variables_initializer()
    
    with tf.Session() as sess:
        sess.run(init)
        point_num = len(original_data)
        photo_center = np.transpose(np.reshape(np.repeat(photo_center,point_num),(3,point_num)))
        focal_dir = np.transpose(np.reshape(np.repeat(focal_dir,point_num),(3,point_num)))
        focal_distance = np.transpose(np.reshape(np.repeat(focal_distance,point_num),(1,point_num)))
        
        print("photo_center.shape:", photo_center.shape)
        print("focal_dir.shape: ",focal_dir.shape)
        print("focal_distance.shape: ",focal_distance.shape)
        
        print("to run...")
        
        data = sess.run(data,feed_dict={
            x: original_data[:,:3] ,
            p: photo_center ,
            v: focal_dir,
            f: focal_distance }) # any data returned by sess.run is numpy.array
        print("max x: %f max y: %f max z: %f" % (max(original_data[:,0]),max(original_data[:,1]), max(original_data[:,2])))
        print(max(data[:,0]), max(data[:,1]),max(data[:,2]))
        #print(data)
        original_data[:,:3] = data


        #print(data.shape)
        #np.savetxt(sys.argv[2], original_data, fmt = "%.3f %.3f %.3f %i %i %i %i")
        o = tf.constant([1,0,0],tf.float32)
        photo = generate_photo(original_data, 400,400,v,o)
        print(photo.shape)
        print(photo)


if __name__ == "__main__":
    #timeit(main,*args)
    main()

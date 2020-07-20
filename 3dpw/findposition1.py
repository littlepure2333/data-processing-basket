# encoding: utf-8

import pickle
import numpy as np
import os
import json
import script

def findposition1(file25, file1, file2):
    # file1 = ("downtown_sitOnStairs_00.pkl")
    x = pickle.load(open(file1))
    poses2d = x['poses2d']
    #print(poses2d)
    x1 = np.array(poses2d)
    print(x1.shape)
    x1 = x1.transpose(0, 1, 3, 2)
    #print(x1.shape)

    # file25 = ("./25b/downtown_sitOnStairs_00/")
    filename = os.listdir(file25)

    #print(len(filename))
    x_25_0 = np.zeros([x1.shape[0],x1.shape[1],3,25])
    #print(x_25_0.shape)
    #x_25_1 = np.zeros([2,x.shape[1],3,25])

    count = 0
    for e,i in enumerate(filename):
        #print(i)
        num = int(i.split('_')[1])
        #print(num)
        i = os.path.join(file25,i)
        y = json.load(open(i))
        arr25_18 = []
        for j in range(len(y['people'])):
            y25 = y['people'][j]["pose_keypoints_2d"]
            #print(y25[0:23])
            #arr25 = np.array(y25)
            arr25_18.append(y25[0:24] + y25[27:57])
            #print(arr25_18)
            #arr25 = np.array(arr25_18[j])
            #print(arr25_18)
        arr25_18 = np.array(arr25_18)
        #print(arr25_18.shape)
        #print(arr25_18.shape)
        #arr18 = x[2][i][3][18]
        for numperson in range(0,x1.shape[0]):
        
            arr18_0 = x1[numperson][num].flatten()

            arr18_0_9 = np.tile(arr18_0,(len(y['people']),1))
            #print(arr25_18.shape)
            #print(arr18_0_9.shape)
            diff0 = np.abs(arr25_18 - arr18_0_9)
            #print(diff0[6])
            diff0 = diff0.sum(1)
            #diff0.min()
            #print(diff0)
            #print(arr18.shape)
            id0 = np.argmin(diff0)
            #print(id0)
            arr25_0 = y['people'][id0]["pose_keypoints_2d"]
            arr25_0 = np.array(arr25_0)
            #print(arr25_0.shape)
            indexperson = np.array([0,1,2,48,49,50,45,46,47,54,55,56,51,52,53,15,16,17,6,7,8,18,19,20,9,10,11,21,22,23,12,13,14,36,37,38,27,28,29,39,40,41,30,31,32,42,43,44,33,34,35,3,4,5,0,0,0,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74])
            arr25_0 = arr25_0[indexperson]

            arr25_0[54] = 0
            arr25_0[55] = 0
            arr25_0[56] = 0

            arr25_0 = arr25_0.reshape(25,3)
            arr25_0 = arr25_0.transpose(1,0)
            #print(arr25_0)


            x_25_0[numperson][num]  = arr25_0
            #x_25_0 = list(x_25_0)
            #print(x_25_0)
            #print(x_25_0.shape)
            #print("3333")

        count = e + 1
    if count != x1.shape[1]:
        print(count)
        print(x1.shape[1])
        # print(e)
        

    '''
        arr18_1 = x1[1][num].flatten()
        arr18_1_9 = np.tile(arr18_1,(len(y['people']),1))
        diff1 = np.abs(arr25_18 - arr18_1_9)
        #print(diff0[6])
        diff1 = diff1.sum(1)
        #diff0.min()
        #print(diff1)
        #print(arr18.shape)
        id1 = np.argmin(diff1)
        #print(id1)
        arr25_1 = y['people'][id1]["pose_keypoints_2d"]
        arr25_1 = np.array(arr25_1)
        arr25_1 = arr25_1.reshape(25,3)
        arr25_1 = arr25_1.transpose(1,0)
        
        x_25_0[1][num]  = arr25_1

        #c
        #print(x_25_1[1][num])
        #print(x_25_0.shape)
    '''

    print(x_25_0.shape)
    x_25_0 = list(x_25_0)
    # file2 = ("1downtown_sitOnStairs_00.pkl")
    file181 = open(file2,'wb')   
    #x1 = pickle.load(file181)
    #poses2d = x1['poses2d']

    #print(len(x_25_0))
    # print(type(x))
    x['poses2d'] = x_25_0
    pickle.dump(x,file181)
    file181.close()
    #x_25_1 = list(x_25_1)
'''
    file3 = ("1downtown_sitOnStairs_00.pkl")
    x2 = pickle.load(open(file3)) 
    poses2d1 = x['poses2d']
    # print(x.keys())
    # print(x2.keys())
    x2 = np.array(poses2d1)
    #print(x2)
    print(x2.shape)
'''



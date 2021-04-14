# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 10:48:41 2021

@author: subhash
"""
import numpy as np
import laspy as lp
import pptk


def preparedata():
    input_path="C:\\"
    dataname="2020_Drone_M"
    point_cloud=lp.file.File(input_path+dataname+".las", mode="r")
    print(point_cloud)
    points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z) 
    ).transpose()
    print(points)
    print(type(points))
    print(points.size)
    colors = np.vstack((point_cloud.red, point_cloud.green,
    point_cloud.blue)).transpose()
    return point_cloud,points,colors


def pptkviz(points,colors):
    v = pptk.viewer(points)
    v.attributes(colors/65535)
    v.set(point_size=0.001,bg_color= [0,0,0,0],show_axis=0,
    show_grid=0)
    return v

def cameraSelector(v):
    camera=[]
    camera.append(v.get('eye'))
    camera.append(v.get('phi'))
    camera.append(v.get('theta'))
    camera.append(v.get('r'))
    return np.concatenate(camera).tolist()

def computePCFeatures(selection, points, colors, knn=6, radius=np.inf):
    normals=pptk.estimate_normals(points[selection],knn,radius)
    idx_ground=np.where(points[...,2]>np.min(points[...,2]+0.3))
    idx_normals=np.where(abs(normals[...,2])<0.9)
    idx_wronglyfiltered=np.setdiff1d(idx_ground, idx_normals)
    common_filtering=np.append(idx_normals, idx_wronglyfiltered)
    return pptk.viewer(points[common_filtering],colors[common_filtering]/65535)



#Declare all your functions here
if __name__ == "__main__":
    
    point_cloud,points,colors=preparedata()
    viewer1=pptkviz(points,colors)
    
    
    # to segement data points with selection(extracting and adding features, attributes)
    
    # selection = viewer1.get('selected')
    # print(selection)
    # if selection.any():
    #     computePCFeatures(selection, points, colors)
    
    # to visualize by selecting camera angles 
    
    cam1=cameraSelector(viewer1)
    #Change your viewpoint then -->
    cam2=cameraSelector(viewer1)
    #Change your viewpoint then -->
    cam3=cameraSelector(viewer1)
    #Change your viewpoint then -->
    cam4=cameraSelector(viewer1)

    poses = []
    poses.append(cam1)
    poses.append(cam2)
    poses.append(cam3)
    poses.append(cam4)
    viewer1.play(poses, 2 * np.arange(4), repeat=True, interp='linear')

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 09:06:40 2021

@author: subhash
"""
import numpy as np
import matplotlib.pyplot as plt
import laspy as lp

input_path = "C:\\"
dataname = "2020_Drone_M"
point_cloud=lp.file.File(input_path+dataname+".las", mode="r")

print(type(point_cloud))

print(point_cloud)

points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()


# # pip install pptk

# import pptk

# v = pptk.viewer(points)

# v.attributes(colors/65535)


# v.color_map('cool')
# v.set(point_size=0.001,bg_color=[0,0,0,0],show_axis=0,show_grid=0)


import open3d as o3d
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
print(pcd.points)
print(type(pcd.points))
print(np.asarray(pcd.points).size)
pcd.colors = o3d.utility.Vector3dVector(colors/65535)
# # pcd.normals = o3d.utility.Vector3dVector(normals) no normals in data set .las?
o3d.visualization.draw_geometries([pcd])

voxel_grid = o3d.geometry.VoxelGrid
create_from_point_cloud(pcd,voxel_size=0.40)
o3d.visualization.draw_geometries([voxel_grid])

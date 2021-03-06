import numpy as np
import open3d as o3d

def get_camera_parameters(extrinsic_mat=None, intrinsic_mat=[1280, 720, 631.5, 631.2, 639.5, 359.5]):
    param = o3d.camera.PinholeCameraParameters()
    
    if extrinsic_mat == None:
        param.extrinsic = np.eye(4, dtype=np.float64)
    else:
        param.extrinsic = extrinsic_mat

    # param.intrinsic = o3d.camera.PinholeCameraIntrinsic()

    param.intrinsic.set_intrinsics(intrinsic_mat[0], intrinsic_mat[1], intrinsic_mat[2], \
                                   intrinsic_mat[3], intrinsic_mat[4], intrinsic_mat[5])

    return param

def get_type_camera_parameters(extrinsic_mat=None, camera=''):
    param = o3d.camera.PinholeCameraParameters()
    
    if extrinsic_mat == None:
        param.extrinsic = np.eye(4, dtype=np.float64)
    else:
        param.extrinsic = extrinsic_mat

    # param.intrinsic = o3d.camera.PinholeCameraIntrinsic()

    if camera == 'kinect':
        param.intrinsic.set_intrinsics(1280, 720, 631.5, 631.2, 639.5, 359.5)
    elif camera == 'realsense':
        param.intrinsic.set_intrinsics(1280, 720, 927.17, 927.37, 639.5, 359.5)
    else:
        print("Unknow camera type")
        exit(0)

    return param
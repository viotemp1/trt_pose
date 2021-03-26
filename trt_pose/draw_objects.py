import cv2
<<<<<<< HEAD
import numpy as np
=======
>>>>>>> a89b422e0d72c4d537d7d4f39d03589f7ac236c0


class DrawObjects(object):
    
    def __init__(self, topology):
        self.topology = topology
<<<<<<< HEAD
#         self.output = {"image_shape":(), "circles": np.empty([0,2], np.int32), "lines": np.empty([0,4], np.int32)}
        
    def __call__(self, image, object_counts, objects, normalized_peaks):
        topology = self.topology
        output = {"image_shape":(), "circles": np.empty([0,2], np.uint16), "lines": np.empty([0,4], np.uint16)}
        output["image_shape"] = image.shape
=======
        
    def __call__(self, image, object_counts, objects, normalized_peaks):
        topology = self.topology
>>>>>>> a89b422e0d72c4d537d7d4f39d03589f7ac236c0
        height = image.shape[0]
        width = image.shape[1]
        
        K = topology.shape[0]
        count = int(object_counts[0])
        K = topology.shape[0]
        for i in range(count):
            color = (0, 255, 0)
            obj = objects[0][i]
            C = obj.shape[0]
            for j in range(C):
                k = int(obj[j])
                if k >= 0:
                    peak = normalized_peaks[0][j][k]
                    x = round(float(peak[1]) * width)
                    y = round(float(peak[0]) * height)
                    cv2.circle(image, (x, y), 3, color, 2)
<<<<<<< HEAD
                    output["circles"] = np.concatenate((output["circles"], [[x, y]]), axis=0)
=======
>>>>>>> a89b422e0d72c4d537d7d4f39d03589f7ac236c0

            for k in range(K):
                c_a = topology[k][2]
                c_b = topology[k][3]
                if obj[c_a] >= 0 and obj[c_b] >= 0:
                    peak0 = normalized_peaks[0][c_a][obj[c_a]]
                    peak1 = normalized_peaks[0][c_b][obj[c_b]]
                    x0 = round(float(peak0[1]) * width)
                    y0 = round(float(peak0[0]) * height)
                    x1 = round(float(peak1[1]) * width)
                    y1 = round(float(peak1[0]) * height)
<<<<<<< HEAD
                    cv2.line(image, (x0, y0), (x1, y1), color, 2)
                    output["lines"] = np.concatenate((output["lines"], [[x0, y0, x1, y1]]), axis=0)
        if len(output["circles"]) == 0 or len(output["lines"]):
            output = {}
        return output
=======
                    cv2.line(image, (x0, y0), (x1, y1), color, 2)
>>>>>>> a89b422e0d72c4d537d7d4f39d03589f7ac236c0

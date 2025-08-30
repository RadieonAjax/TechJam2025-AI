import cv2
import zxingcpp
import numpy as np

def blur_codes(image_path, output_path):
    img = cv2.imread(image_path)

    results = zxingcpp.read_barcodes(img)
    print(results)

    pt_array = []

    for barcode in results:
        pts = np.array([
            [barcode.position.top_left.x, barcode.position.top_left.y],
            [barcode.position.top_right.x, barcode.position.top_right.y],
            [barcode.position.bottom_right.x, barcode.position.bottom_right.y],
            [barcode.position.bottom_left.x, barcode.position.bottom_left.y]
        ], dtype=np.int32)

        pt_array.append(pts)

    if pt_array:
        all_pts = np.stack(pt_array)
    else:
        all_pts = np.empty((0, 4, 2), dtype=np.int32)
    return all_pts

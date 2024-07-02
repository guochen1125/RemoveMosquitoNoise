import numpy as np
import cv2
from scipy.ndimage import generic_filter


def padding(block, pad_w):
    padded_matrix = np.pad(block, ((pad_w, pad_w), (pad_w, pad_w)), mode="constant")

    padded_matrix[pad_w:-pad_w, :pad_w] = block[:, :pad_w]
    padded_matrix[pad_w:-pad_w, -pad_w:] = block[:, -pad_w:]
    padded_matrix[:pad_w, :] = padded_matrix[pad_w : 2 * pad_w, :]
    padded_matrix[-pad_w:, :] = padded_matrix[-2 * pad_w : -pad_w, :]

    return padded_matrix


def epsilon(ori, pad_w):
    def filter_func(window):
        center = window[len(window) // 2]
        eps = np.std(window)  # / np.mean(window)
        mask = (window >= center - eps) & (window <= center + eps)
        return np.mean(window[mask])

    padded_matrix = padding(ori, pad_w)
    res = generic_filter(
        padded_matrix, filter_func, size=(2 * pad_w + 1, 2 * pad_w + 1)
    )
    res = np.clip(res, 0, 255).astype(np.uint8)
    return res[pad_w:-pad_w, pad_w:-pad_w]


if __name__ == "__main__":
    image = cv2.imread("./ori/3.png")
    src = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)[:1080,:1920]
    denoised_src = np.zeros_like(src).astype(np.uint8)
    for ch in range(3):
        denoised_src[:, :, ch] = epsilon(src[:, :, ch], 3)
    res = cv2.cvtColor(denoised_src, cv2.COLOR_YCrCb2BGR)
    cv2.imwrite("./res_std/3_3.png", res)

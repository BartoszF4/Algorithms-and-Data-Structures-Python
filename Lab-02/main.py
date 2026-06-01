import time
from utils import load_image_rgb, load_image_grayscale, save_image_grayscale
from thresholding import single_thresholding, double_thresholding
from histogram_equalization import equalize_histogram
from mean_filter import naive_mean_filter, sat_mean_filter


def main():
    yoda_rgb, _, _ = load_image_rgb('yoda.jpeg')

    yoda_single = single_thresholding(yoda_rgb, 40)
    save_image_grayscale(yoda_single, 'yoda_single.jpeg')
    print("Single threshold done.")

    yoda_double = double_thresholding(yoda_rgb, 40, 100 )
    save_image_grayscale(yoda_double, 'yoda_double.jpeg')
    print("Double threshold done.")

    yoda_gray, _, _ = load_image_grayscale('yoda.jpeg')
    yoda_eq = equalize_histogram(yoda_gray)
    save_image_grayscale(yoda_eq, 'yoda_eq.jpeg')
    print("Equalization done.")

    road_gray, _, _ = load_image_grayscale('road.jpg')
    start_time = time.time()
    road_naive = naive_mean_filter(road_gray, 71)
    naive_time = time.time() - start_time
    save_image_grayscale(road_naive, 'road_naive.jpg')
    print("Naive approach done.")
    print(f"Naive approach time: {naive_time:.2f} seconds.")

    start_time = time.time()
    road_sat = sat_mean_filter(road_gray, 71)
    sat_time = time.time() - start_time
    save_image_grayscale(road_sat, 'road_sat.jpg')
    print("SAT approach done.")
    print(f"SAT approach time: {sat_time:.2f} seconds.")


if __name__ == "__main__":
    main()
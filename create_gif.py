import imageio.v3 as iio

def main():

    filenames = ['kiryu1.jpg', 'kiryu2.jpg', 'kiryu3.jpg', 'kiryu4.jpg', 'kiryu5.jpg']
    images = []

    for filename in filenames:
        images.append(iio.imread(filename))
    
    iio.imwrite('kiryu.gif', images, duration=150, loop = 0)

if __name__ == "__main__":
    main()
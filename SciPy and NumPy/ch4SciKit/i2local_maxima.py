import numpy as np
import matplotlib.pyplot as mpl 
import scipy.ndimage as ndimage 
import skimage.morphology as morph
import skimage
print('skimage.__version__=',skimage.__version__)

# 这个方法已经不存在于 skimage.morphology， 我找回来啦从：http://pydoc.net/Python/scikits-image/0.6.1/skimage.morphology.watershed/
def is_local_maximum(image, labels=None, footprint=None):
    """
    Return a boolean array of points that are local maxima
 
    Parameters
    ----------
    image: ndarray (2-D, 3-D, ...)
        intensity image
        
    labels: ndarray, optional 
        find maxima only within labels. Zero is reserved for background.
    
    footprint: ndarray of bools, optional
        binary mask indicating the neighborhood to be examined
        `footprint` must be a matrix with odd dimensions, the center is taken 
        to be the point in question.

    Returns
    -------
    result: ndarray of bools
        mask that is True for pixels that are local maxima of `image`

    Examples
    --------
    >>> image = np.zeros((4, 4))
    >>> image[1, 2] = 2
    >>> image[3, 3] = 1
    >>> image
    array([[ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  2.,  0.],
           [ 0.,  0.,  0.,  0.],
           [ 0.,  0.,  0.,  1.]])
    >>> is_local_maximum(image)
    array([[ True, False, False, False],
           [ True, False,  True, False],
           [ True, False, False, False],
           [ True,  True, False,  True]], dtype='bool')
    >>> image = np.arange(16).reshape((4, 4))
    >>> labels = np.array([[1, 2], [3, 4]])
    >>> labels = np.repeat(np.repeat(labels, 2, axis=0), 2, axis=1)
    >>> labels
    array([[1, 1, 2, 2],
           [1, 1, 2, 2],
           [3, 3, 4, 4],
           [3, 3, 4, 4]])
    >>> image
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15]])
    >>> is_local_maximum(image, labels=labels)
    array([[False, False, False, False],
           [False,  True, False,  True],
           [False, False, False, False],
           [False,  True, False,  True]], dtype='bool')
    """
    if labels is None:
        labels = np.ones(image.shape, dtype=np.uint8)
    if footprint is None:
        footprint = np.ones([3] * image.ndim, dtype=np.uint8)
    assert((np.all(footprint.shape) & 1) == 1)
    footprint = (footprint != 0)
    footprint_extent = (np.array(footprint.shape)-1) // 2
    if np.all(footprint_extent == 0):
        return labels > 0
    result = (labels > 0).copy()
    #
    # Create a labels matrix with zeros at the borders that might be
    # hit by the footprint.
    #
    big_labels = np.zeros(np.array(labels.shape) + footprint_extent*2,
                          labels.dtype)
    big_labels[[slice(fe,-fe) for fe in footprint_extent]] = labels
    #
    # Find the relative indexes of each footprint element
    #
    image_strides = np.array(image.strides) // image.dtype.itemsize
    big_strides = np.array(big_labels.strides) // big_labels.dtype.itemsize
    result_strides = np.array(result.strides) // result.dtype.itemsize
    footprint_offsets = np.mgrid[[slice(-fe,fe+1) for fe in footprint_extent]]
    
    fp_image_offsets = np.sum(image_strides[:, np.newaxis] *
                              footprint_offsets[:, footprint], 0)
    fp_big_offsets = np.sum(big_strides[:, np.newaxis] *
                            footprint_offsets[:, footprint], 0)
    #
    # Get the index of each labeled pixel in the image and big_labels arrays
    #
    indexes = np.mgrid[[slice(0,x) for x in labels.shape]][:, labels > 0]
    image_indexes = np.sum(image_strides[:, np.newaxis] * indexes, 0)
    big_indexes = np.sum(big_strides[:, np.newaxis] * 
                         (indexes + footprint_extent[:, np.newaxis]), 0)
    result_indexes = np.sum(result_strides[:, np.newaxis] * indexes, 0)
    #
    # Now operate on the raveled images
    #
    big_labels_raveled = big_labels.ravel()
    image_raveled = image.ravel()
    result_raveled = result.ravel()
    #
    # A hit is a hit if the label at the offset matches the label at the pixel
    # and if the intensity at the pixel is greater or equal to the intensity
    # at the offset.
    #
    for fp_image_offset, fp_big_offset in zip(fp_image_offsets, fp_big_offsets):
        same_label = (big_labels_raveled[big_indexes + fp_big_offset] ==
                      big_labels_raveled[big_indexes])
        less_than = (image_raveled[image_indexes[same_label]] <
                     image_raveled[image_indexes[same_label]+ fp_image_offset])
        result_raveled[result_indexes[same_label][less_than]] = False
        
    return result

# Generating data points with a non-uniform background
x = np.random.uniform(low=0, high=200, size=20).astype(int) 
y = np.random.uniform(low=0, high=400, size=20).astype(int)

# Creating image with non-uniform background 
func = lambda x, y: np.cos(x)+ np.sin(y) 
grid_x, grid_y = np.mgrid[0:12:200j, 0:24:400j] 
bkg = func(grid_x, grid_y)
bkg = bkg / np.max(bkg)

# Creating points
clean = np.zeros((200,400))
clean[(x,y)] += 5
clean = ndimage.gaussian_filter(clean, 3) 
clean = clean / np.max(clean)

# Combining both the non-uniform background 
# and points
fimg = bkg + clean
fimg = fimg / np.max(fimg)
# Calculating local maxima
# lm1 = morph.peak_local_max(fimg) 

# 下面这个方法已经过期放弃啦
# lm1 = morph.is_local_maximum(fimg)
lm1 = is_local_maximum(fimg)

x1, y1 = np.where(lm1.T == True)

# Creating figure to show local maximum detection 
# rate success
fig = mpl.figure(figsize=(8, 4))
ax = fig.add_subplot(111)
ax.imshow(fimg)
ax.scatter(x1, y1, s=100, facecolor='none', edgecolor='#009999') 
ax.set_xlim(0,400)
ax.set_ylim(0,200)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
fig.savefig('scikit_image_f02.pdf', bbox_inches='tight')

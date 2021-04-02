import torch
import lpips
from IPython import embed


def avatar_similarity(s_img, t_img):


    ## Example usage with images
    ex_ref = lpips.im2tensor(
        lpips.load_image("../data/processed_douban/" + str(s_img) + ".jpg")
    )
    ex_p0 = lpips.im2tensor(
        lpips.load_image("../data/img_weibo/" + str(t_img) + ".jpg")
    )

    if use_gpu:
        ex_ref = ex_ref.cuda()
        ex_p0 = ex_p0.cuda()

    ex_d0 = loss_fn.forward(ex_ref, ex_p0)

    if not spatial:
        print("Distances: (%.3f)" % (ex_d0))
    else:
        print("%s %s Distances: (%.3f)" % (s_img, t_img, ex_d0.mean()))
        # 为写报告画图部分
        # The mean distance is approximately the same as the non-spatial distance
        # import pylab

        # pylab.imshow(ex_d0[0, 0, ...].data.cpu().numpy())
        # pylab.show()


if __name__ == "__main__":
    use_gpu = False  # Whether to use GPU
    spatial = True  # Return a spatial map of perceptual distance.

    # Linearly calibrated models (LPIPS)
    loss_fn = lpips.LPIPS(
        net="alex", spatial=spatial
    )  # Can also set net = 'squeeze' or 'vgg'
    # loss_fn = lpips.LPIPS(net='alex', spatial=spatial, lpips=False) # Can also set net = 'squeeze' or 'vgg'

    if use_gpu:
        loss_fn.cuda()

    ## Example usage with dummy tensors
    dummy_im0 = torch.zeros(1, 3, 64, 64)  # image should be RGB, normalized to [-1,1]
    dummy_im1 = torch.zeros(1, 3, 64, 64)
    if use_gpu:
        dummy_im0 = dummy_im0.cuda()
        dummy_im1 = dummy_im1.cuda()
    dist = loss_fn.forward(dummy_im0, dummy_im1)
    for i in range(1,4):
        for j in range(1,4):
            avatar_similarity(i, j)


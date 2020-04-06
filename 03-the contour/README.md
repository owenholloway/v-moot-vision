## The contour, or how to select an object!

So we've got a mask thats good ... now what?

Well lets use some scout skills! You know those maps we know so well, they have contour lines to find where the gradient changes. We are going to a contour line in the same way but it will just be a step either high (1) or low (0) these are the white or black pixels in the mask. So by feeding this mask into OpenCV we can get the outline of objects that match our filter.

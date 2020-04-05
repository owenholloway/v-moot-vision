## A HSV (Hue Saturation Value) filter

So we now have a lot of pixels at our disposal ... but what about the ones we don't care about. Like blue, lets say we don't like blue. Well, we can filter all blue pixels out, or rather we can make a mask that allows all other pixels through!

Okay .... so HSV you say, whats that? Well, I'm glad you asked. We capture video is RGB (red green blue) which is a colour space. Its good for capturing video but its pretty rubbish for working with on computer vision, so we translate it into Hue Saturation Value. Cool? Good, if you want to know more the [wikipedia entry](https://en.wikipedia.org/wiki/HSL_and_HSV) is pretty good!

```
python3 ./range_detector.py --filter HSV --webcam
```

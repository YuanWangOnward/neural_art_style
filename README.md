# Introduction
<div style="text-align: justify; text-indent: 30px;">
<p>
It's a course project I advised.
Two brilliant and passionated master students at NYU,
Megan Hardy and Sumanto Pal,
start their adventure of image processing and deep learning.
Different objects of a painting typically have distinctively different
styles i.e. textures and color compositions while previous neural
painting works abstract a global style from a painting
and apply it globally onto a photo.
In this project, we separate objects of interest in both painting
and real content photo and apply an art style only to the
corresponding objects. For example, abstract style from a flower
in a painting and apply it onto a flower in a real content photo.
It creates unique aesthetic experiences.
</p>
</div>

# Object segmentation
<div style="text-align: justify; text-indent: 30px;">
<p>
As the first challenge, we use Grabcut to segment objects of interest.
Grabcut is a segmentation technique which requires minimal level of
human intervene while is able to achieve highly details-preserving
results.
</p>
</div>

<center>
<img width="332" height="240"  src="assets/images/grabcut_1.png?raw=true" >
<img width="332" height="240"  src="assets/images/grabcut_2.png?raw=true" >
</center>
<div style="text-align: justify; text-align:center;" >
<p>Fig. 1 Grabcut example. One can simply place a bounding box
around the object of interest and may need to roughly
indicate object with white marker and non-object with black
marker. Then the object can be segmented nicely.
</p></div>

# Painting with multiple styles
<div style="text-align: justify; text-indent: 30px;">
<p>
After some intermediary and post processing, we are able to
abstract styles from objects in paintings and apply them onto
corresponding objects in real content photos.
</p>
</div>

<center>
<img width="276" height="153"  src="assets/images/result_1_1.png?raw=true" >
<img width="233" height="153"  src="assets/images/result_1_2.png?raw=true" >
<img width="276" height="153"  src="assets/images/result_1_3.png?raw=true" >
</center>
<div style="text-align: justify; text-align:center;" >
<p>Fig. 2 Flower style on flower.
</p></div>

<br>
<center>
<img width="270" height="297"  src="assets/images/result_2_1.png?raw=true" >
<img width="270" height="297"  src="assets/images/result_2_2.png?raw=true" >
<img width="270" height="297"  src="assets/images/result_2_3.png?raw=true" >
</center>
<div style="text-align: justify; text-align:center;" >
<p>Fig. 3 Jordon in the space (background styled only).
</p></div>


<br>
<center>
<img width="340" height="225"  src="assets/images/result_3_1.png?raw=true" >
<img width="340" height="225"  src="assets/images/result_3_4.png?raw=true" >
<img width="178" height="272"  src="assets/images/result_3_2.png?raw=true" >
<img width="348" height="272"  src="assets/images/result_3_3.png?raw=true" >
</center>
<div style="text-align: justify; text-align:center;" >
<p>Fig. 3 Separated style for foreground and background.
</p></div>

# Publication
This work as been accepted by ACMMM2017.

# References:
- [A Neural Algorithm of Artistic Style](http://arxiv.org/abs/1508.06576)
- [https://github.com/jcjohnson/neural-style](https://github.com/jcjohnson/neural-style)
- [https://github.com/ckmarkoh/neuralart_tensorflow](https://github.com/ckmarkoh/neuralart_tensorflow)
- [https://github.com/log0/neural-style-painting](https://github.com/log0/neural-style-painting)

#### <a href="https://yuanwangonward.github.io/">Back to Yuan's homepage</a>

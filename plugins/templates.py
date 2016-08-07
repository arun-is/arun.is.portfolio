from cactus.template_tags import register

"""
Used in lightbox.html template
Will append '@2x' to a path to a png or jpg image

"""

@register.filter(is_safe=True)
def responsive_image(value):
	temp = value.replace(".png", "@2x.png")
	temp = temp.replace(".jpg", "@2x.jpg")
	return temp
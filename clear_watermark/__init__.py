"""It uses OOP to insert one image as a watermark on another.
"""

__author__ = "carlosmperilla"
__copyright__ = "Copyright 2022 Carlos M. Perilla"
__credits__ = "Carlos M. Perilla"

__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "carlosmperilla"
__email__ = "carlosperillaprogramacion@gmail.com"
__status__ = "Developing"

from PIL import Image, ImageEnhance

from typing import NewType, Tuple

#This represents a limited percentage between 0 and 100.
LimitPercent = NewType('LimitPercent', int)

class ImgWithWatermark:
	"""
		This class models an image with a watermark, starting from two images:
			The first the base and the second the image to be modified and pasted as a watermark to the first.
	"""


	__msg_percentnotvalid = "It is not a valid percentage, please use an integer number between 0 and 100."
	class PercentNotValid(Exception):
		"""The month is not valid. It is not by default, 
        a list of compatible months has not been imported 
        """
		pass


	def __init__(self, 
				base_img_filename:str, 
				watermark_filename:str, 
				pos:Tuple[LimitPercent]=(25, 75), 
				opacity:LimitPercent=40,
				n_percentage:LimitPercent=50,
				gray_mode:bool=False, 
				final_color_model:str="RGB"
				) -> None:
		
		#Graphic variable to not repeat line break.
		self.__i_linebreak : bool = False
		#We load the images
		self.__load_imgs(base_img_filename, watermark_filename)
		#We edit the watermark.
		self.watermark_edition(gray_mode=gray_mode, opacity=opacity, n_percentage=n_percentage)
		#We position and display the watermark.
		self.watermark_position_and_display(pos)
		#We convert the final image to the chosen color model.
		self.set_color_model(final_color_model)


	def __valid_percent(self, value:LimitPercent) -> None:
		"""
			We validate if it is a value is a percentage between 0 and 100.
		"""
		valid_type = type(value) == int
		if valid_type:
			valid_range = (value <= 100) and (value >= 0)
			if valid_range:
				return None
		raise self.PercentNotValid(self.__msg_percentnotvalid)


	def __load_imgs(self, base_img_filename:str, watermark_filename:str):
		self.base_img = Image.open(base_img_filename)
		self.watermark = Image.open(watermark_filename)


	def __gray(self, gray_mode:bool) -> None:
		"""
			Turn the watermark into a slightly brighter grayscale. 
			If the gray mode is activated.
		"""
		if gray_mode:
			#We increased the brightness a little
			self.watermark = ImageEnhance.Brightness(self.watermark).enhance(1.7)
			#Convert to black and white
			self.watermark = ImageEnhance.Color(self.watermark).enhance(0)


	def __add_percent_opacity(self, opacity:LimitPercent) -> None:
		"""
			Adds opacity to the watermark, with 0 being full transparency and 100 being full opacity.
		"""

		self.__valid_percent(opacity)

		#We translate the opacity value into an integer between 0 and 255
		n_opacity = int(255 * opacity/100)

		#We make a copy to avoid modifying the transparent values of the image 
		# when changing the opacity through the alpha channel.
		#credit: https://github.com/python-pillow/Pillow/issues/4687#issuecomment-643567573
		watermark_aux = self.watermark.copy()
		watermark_aux.putalpha(n_opacity)
		self.watermark.paste(watermark_aux, self.watermark)


	def __percent_resize(self, n_percentage:LimitPercent) -> None:
		"""
			Resizes the image to a percentage less than or equal to its original value.
		"""
		self.__valid_percent(n_percentage)

		#We translate the percentage to a portion of the original image.
		n_ratio = 100//n_percentage
		new_size = self.watermark.width//n_ratio, self.watermark.height//n_ratio
		
		#We resize the image.
		self.watermark = self.watermark.resize(new_size)

	def __center_watermark(self) -> None:
		"""
			Allows the positioning to be from the center of the watermark and not from its upper left corner.
		"""
		center_watermark = self.watermark.width//2, self.watermark.height//2
		self.position[0] -= center_watermark[0]
		self.position[1] -= center_watermark[1]

	def __get_percent_position(self, pos_x:LimitPercent, pos_y:LimitPercent) -> None:
		"""
			From percentages (x, y) locates the watermark within the base image.
				(pos_x=50, pos_y=50) would be the center of the image for example.
		"""

		self.__valid_percent(pos_x)
		self.__valid_percent(pos_y)

		#We get the value in pixels of the position.
		pos_x_ = int((pos_x/100)*self.base_img.width)
		pos_y_ = int((pos_y/100)*self.base_img.height)
		self.position = [pos_x_, pos_y_]

		#We center the watermark at the position point.
		self.__center_watermark()

	def __paste_watermark(self) -> None:
		"""
			We paste the watermark on the base image.
		"""
		self.base_img.paste(self.watermark, self.position, mask = self.watermark)

	def __initial_linebreak(self) -> None:
		"""
			Print a line break before any message.
				If it was already printed, it doesn't do it again.
		"""
		if not self.__i_linebreak:
			print()
			self.__i_linebreak = True

	def __close(self) -> None:
		"""
			We close the open image files.
		"""
		self.__initial_linebreak()
		print("\tImage file closed.")
		self.watermark.close()
		self.base_img.close()

	def watermark_edition(self, gray_mode:bool, opacity:LimitPercent, n_percentage:LimitPercent) -> None:
		"""
			We edit the image to make it a presentable watermark.
		"""
		#If the gray scale is enabled, we apply it.
		self.__gray(gray_mode)
		#We modify the opacity of the watermark.
		self.__add_percent_opacity(opacity)
		#We modify the size of the watermark.
		self.__percent_resize(n_percentage)

	def watermark_position_and_display(self, pos:Tuple[LimitPercent]) -> None:
		"""
			We position the image and display it on the base image.
		"""
		#We position the watermark.
		self.__get_percent_position(*pos)
		#We paste the watermark on the base image.
		self.__paste_watermark()

	def set_color_model(self, final_color_model:str) -> None:
		"""
			We convert the final image into the color mode needed to be saved or showed.
		"""
		self.base_img = self.base_img.convert(final_color_model)

	def show(self, close=True) -> None:
		"""
			We show the final image with its watermark.
		"""
		self.base_img.show()
		if close:
			self.__close()

	def save(self, dest, close=True):
		"""
			We save the final image with its watermark.
		"""
		self.__initial_linebreak()
		try:
			self.base_img.save(dest)
			print(f"\tImage file saved to --> {dest}")
			if close:
				self.__close()
		except ValueError as e:
			print(f"\tThe image could not be saved by '{e}'")

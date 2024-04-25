import heapq
import os
class HuffmanCoding:
	def __init__(self, path):
		self.path = path
		self.heap = []
		self.codes = {}
		self.reverse_mapping = {}

	class HeapNode:
		def __init__(self, char, freq):
			self.char = char
			self.freq = freq
			self.left = None
			self.right = None

		# defining comparators less_than and equals
		def __lt__(self, other):
			return self.freq < other.freq

		def __eq__(self, other):
			if(other == None):
				return False
			if(not isinstance(other, HuffmanCoding.HeapNode)):
				return False
			return self.freq == other.freq

	# functions for compression:

	#A frequency dictionary is used for counting the characters in the txt file
	def make_frequency_dict(self, text):
		frequency = {}
		for character in text:
			#If the character is not in the dictionary, then it adds 
			#the character as key and the times it appears as the content
			if not character in frequency:
				frequency[character] = 0
				
			#Otherwise, it just adds up the counter
			frequency[character] += 1

		#Finally it returns the dictionary for displaying later
		return frequency

	#Make_heap creates a data structure known as a minHeap for representing the Huffman tree
	def make_heap(self, frequency):
		for key in frequency:
			node = self.HeapNode(key, frequency[key])
			heapq.heappush(self.heap, node)

	#Merge_nodes creates the tree as it is known
	def merge_nodes(self):
		while(len(self.heap)>1):
			node1 = heapq.heappop(self.heap)
			node2 = heapq.heappop(self.heap)

			merged = self.HeapNode(None, node1.freq + node2.freq)
			merged.left = node1
			merged.right = node2

			heapq.heappush(self.heap, merged)

	#This function declares the values to give the characters in the tree
	def make_codes_helper(self, root, current_code):
		if(root == None):
			return

		if(root.char != None):
			self.codes[root.char] = current_code
			self.reverse_mapping[current_code] = root.char
			return

		self.make_codes_helper(root.left, current_code + "0")
		self.make_codes_helper(root.right, current_code + "1")


	#This function assigns wether the character is assigned a 0 or a 1 in the tree (left or right)
	def make_codes(self):
		root = heapq.heappop(self.heap)
		current_code = ""
		self.make_codes_helper(root, current_code)


	#As the name implies, the function gets the encoded text based on the values
	#the previous function assigned to the characters
	def get_encoded_text(self, text):
		encoded_text = ""
		for character in text:
			encoded_text += self.codes[character]
		return encoded_text

	#Here is where the encoding gets grouped in bytes (8 bit groups)
	def pad_encoded_text(self, encoded_text):
		extra_padding = 8 - len(encoded_text) % 8
		for i in range(extra_padding):
			encoded_text += "0"

		padded_info = "{0:08b}".format(extra_padding)
		encoded_text = padded_info + encoded_text
		return encoded_text

	#Here the byte array that is "written" in the .bin file is created
	def get_byte_array(self, padded_encoded_text):

		#Validation for the padding to exist
		if(len(padded_encoded_text) % 8 != 0):
			print("Encoded text not padded properly")
			exit(0)

		b = bytearray()
		#Grouping bytes
		for i in range(0, len(padded_encoded_text), 8):
			byte = padded_encoded_text[i:i+8]
			b.append(int(byte, 2))
		return b

	#The name is not very clear to be honest, it doesn't really compress at all
	#Just calls all the functions that actually do compress the file
	def compress(self):
		#The path and extension for the file is established
		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + ".bin"

		#Selected file is open as read+ mode and the file we will output (.bin) is opened as write bits
		with open(self.path, 'r+') as file, open(output_path, 'wb') as output:
			text = file.read()
			text = text.rstrip()

			#Calling for the frequency dict to be made based on the txt
			frequency = self.make_frequency_dict(text)
			#Then this dict is used as input for the tree
			self.make_heap(frequency)
			#Finally, text is encoded via these functions
			self.merge_nodes()
			self.make_codes()
			encoded_text = self.get_encoded_text(text)
			padded_encoded_text = self.pad_encoded_text(encoded_text)

			#Byte array is generated and written in the .bin file
			b = self.get_byte_array(padded_encoded_text)
			output.write(bytes(b))

		#Console log for looking if the compression was succesful
		print("Compressed succesfully")
		#Path for compressed file is returned
		return output_path


	""" functions for decompression: """

	#Based on the padding made before, text can be unpadded
	def remove_padding(self, padded_encoded_text):
		padded_info = padded_encoded_text[:8]
		extra_padding = int(padded_info, 2)

		padded_encoded_text = padded_encoded_text[8:]
		encoded_text = padded_encoded_text[:-1*extra_padding]

		return encoded_text

	#Then the text is decoded using a reverse mapping of the characters
	def decode_text(self, encoded_text):
		current_code = ""
		decoded_text = ""

		for bit in encoded_text:
			current_code += bit
			if(current_code in self.reverse_mapping):
				character = self.reverse_mapping[current_code]
				decoded_text += character
				current_code = ""
		#And decoded text is returned
		return decoded_text

	#Again, this function isn't that clear, same as the opposite function.
	def decompress(self, input_path):
		#This time "_decompressed.txt" is added as a way to show that another txt is created
		#not just returning the file the user selected previously
		filename, file_extension = os.path.splitext(self.path)
		output_path = filename + "_decompressed" + ".txt"

		#This is just the opposite thing the code did before
		#Open the .bin as read bytes mdoe, and open a new txt file as writing mode
		with open(input_path, 'rb') as file, open(output_path, 'w') as output:
			bit_string = ""
			#Interpreting bytes and rewritting the text
			byte = file.read(1)
			while(len(byte) > 0):
				byte = ord(byte)
				bits = bin(byte)[2:].rjust(8, '0')
				bit_string += bits
				byte = file.read(1)

			encoded_text = self.remove_padding(bit_string)

			decompressed_text = self.decode_text(encoded_text)

			output.write(decompressed_text)

		print("Decompressed succesfully")
		#Path for decompressed file is returned
		return output_path

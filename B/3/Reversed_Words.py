class Reversed_Words:
	def __init__(self,some_line):
		self.sentence=some_line;
		self.vowel_count=0;
		vowels=set(['a','A','e','E','i','I','O','o','u','U']);
		for letter in some_line:
			if letter in vowels:
				self.vowel_count=self.vowel_count+1;
		self.rev=' '.join(reversed(some_line.split(' ')));

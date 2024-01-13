from pathlib import Path
from emoji import emojize, is_emoji
from unicodedata import lookup

def main():
	files = Path("sounds").glob("*.wav")
	emoji_characters = []
	unicode_characters = []
	falied_characters = []
	for filepath in files:
		emoji = emojize(f":{filepath.stem}:", language='alias')
		if is_emoji(emoji):
			emoji_characters.append(emoji)
		else:
			character = filepath.stem
			try:
				character = lookup(character)
				unicode_characters.append(character)
			except:
				falied_characters.append(character)
	print(emoji_characters)
	print(unicode_characters)
	print(falied_characters)

if __name__ == "__main__":
	main()
from pathlib import Path
from emoji import emojize, is_emoji
from unicodedata import lookup

emoji_sounds: dict
SOUNDS_DIR = (Path("__file__").parent/"sounds").absolute()

def _load_emoji_sounds(sound_dir: Path, return_unicode_separately:bool=False, return_failed_characters:bool=False) -> dict | tuple:
	files = sound_dir.glob("*.wav")
	emoji_sound_mapping = {}
	unicode_sound_mapping = {}
	falied_characters = []
	for filepath in files:
		emoji = emojize(f":{filepath.stem}:", language='alias')
		if is_emoji(emoji):
			emoji_sound_mapping[emoji] = filepath
		else:
			character = filepath.stem
			try:
				character = lookup(character)
				unicode_sound_mapping[character] = filepath
			except:
				falied_characters.append(character)

	returns = (emoji_sound_mapping,)
	if return_unicode_separately:
		returns += (unicode_sound_mapping,)
	else:
		emoji_sound_mapping.update(unicode_sound_mapping)
	if return_failed_characters:
		returns += (falied_characters,)
	return emoji_sound_mapping

emoji_sounds = _load_emoji_sounds(SOUNDS_DIR)
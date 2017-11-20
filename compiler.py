#!/bin/env python3
import markdown
import pathlib
import argparse

MD_CONVERTER = markdown.Markdown()
ROOT_PATH = None


def boxit(markdown_text):
	return '<section class="box">{}</section>'.format(MD_CONVERTER.convert(markdown_text))


def tagify(tag_name):
	return '<!--##{}##-->'.format(tag_name)


def main(argv):
	assets = ROOT_PATH / 'assets'
	markdown_assets = assets / 'stories'

	with (ROOT_PATH / argv.input[0]).open() as file:
		index_content = file.read()

	for file in markdown_assets.iterdir():
		filename = file.name
		tag = tagify(filename)
		pretext, tag, posttext = index_content.partition(tag)
		if not (pretext == "" or tag == "" or posttext == ""):
			with file.open() as md_file:
				index_content = "{}{}{}".format(pretext, boxit(md_file.read()), posttext)

	print(index_content)


def argparser():
	parser = argparse.ArgumentParser()
	parser.add_argument("input", nargs=1, type=str, help="Input files")
	return parser.parse_args()

if __name__ == '__main__':
	ROOT_PATH = pathlib.Path(__file__).parent.absolute()
	main(argparser())

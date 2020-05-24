#!/bin/bash

change() {
#	local IFS=+;
	$(sed -i "s/text_to_change/$*/g" download_speech_file.py)
}

get_back() {
#	local IFS=+;
	$(sed -i "s/$*/text_to_change/g" download_speech_file.py)
}

change $*
python download_speech_file.py
sleep .5
get_back $*

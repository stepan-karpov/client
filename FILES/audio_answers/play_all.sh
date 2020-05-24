for entry in *; do
	#$(omxplayer $entry)
	changed=$(echo "$entry" | sed -e "s/ /\\\ /g; s/,/\\\,/g")
	echo $(omxplayer $changed)
done

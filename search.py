c=input("Enter a Statement :")
if "python" in a.lower():
	index_value=c.index("python")
	count_value=c.count("python")
	print("python-"+srt(index_value))
	print("occurence-"+srt(count_value))
else:
	print("No python in A")
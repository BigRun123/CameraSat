import requests, glob

#shutil.make_archive("Pictures", "zip", "Pictures")
f = open("Links.txt", "a")
f.truncate(0)

while True:
	pictures = glob.glob("Pictures/*")
	upload = pictures[-1]

	try:
		response = requests.post("https://file.io/", files={"file": open(upload, "rb")})
		res = response.json()

		success = res["success"]

		if not success:
			response = requests.post("https://file.io/", files={"file": open(upload, "rb")})
			res = response.json()
			success = res["success"]
			print("not")

		if success:
			link = res["link"]
			f.write(link + "\n")
			f.flush()

	except:
		continue

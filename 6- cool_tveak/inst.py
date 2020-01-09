import instaloader


def main():
	L = instaloader.Instaloader()
	profile = instaloader.Profile.from_username(L.context, 'esaitgaleeva')
	print(profile.biography)


if __name__=='__main__':
	main()
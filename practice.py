class Movie:
    '''Storeing data about movies from movie objects'''
    def __init__(self, name: str, year: int, director: str, stars: list) -> None:
        # checking the attribute
        assert 2022 > year > 1930, "Invalid year"
        assert len(name) >= 1, "Name of the movie must not be empty"
        #initializing 
        self.name = name
        self.year = year
        self.director = director
        self.stars = stars


        		with open(PassManager.file, 'r') as f:
			lines = f.readlines()
			print(lines)
			if profile in lines:
				option = input(f"{profile} already exist, what do you want to do? (delete/replace) : ")

				if option == 'delete':
					PassManager.delete()
				elif option == 'replace':
					pass
				else:
					print("wrong input, options are 'delete' and 'replace'/n exiting")

			else:
				PassManager.add()
        
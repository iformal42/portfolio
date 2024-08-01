class Detail:
    def __init__(self, title: str, name: str, points: list, tech: dict, url: str, video: str):
        self.title = title
        self.name = name
        self.points = points
        self.tech = tech
        self.url = url
        self.video = video


class Projects:
    def __init__(self):
        self.location = {
            1: Detail("Platformer Game", "Find Home Game", list_of_points['1'], techs['1'], urls['1'], videos['1']),
            2: Detail("Automation", "Data entry bot", list_of_points['2'], techs['2'], urls['2'], videos['2']),
            3: Detail("Blog Website", "Daily Blog", list_of_points['3'], techs['3'], urls['3'], videos['3']),
            4: Detail("Typing Test App", "Type Faster", list_of_points['4'], techs['4'], urls['4'], videos['4'])
        }


list_of_points = {
    '1': ["It is a game consist of 2 unique levels with different themes one 'Home Village' and another is 'Dark Magic "
          "Village",
          "Main character can move freely left,right and jump as well as double jump by clicking keys like 'A',"
          "'D' and 'Space-once ,'Space-twice' respectively ",
          "Player's score determine by quantity of fruits has been collected and number of enemies defeated",
          "Enemies can be defeated by jumping on their head"],
    '2': ["This bot scrap interested data from website and fill in excell shit",
          "To scrap the data used beautifulsoup (a library)",
          "Add the scraped to google form using selenium that is linked to the excel sheet"],
    '3': ["A blog website with user friendly design."
          "User can register and login through their email."
          "Only admin can edit, post and delete blogs."
          "Only registered user can add comments on blogs."],
    '4': ["It is Typing test app build using Python",
          "User have to click start button to start the test.",
          "User have to write the words and press enter for matching",
          "Wrong word highlighted with red and correct with green",
          "User get 1 minutes for test",
          "After 1 minutes it will redirect to feedback page with score and restart button"]
}

techs = {'1': {"Programming Langauge": "Python",
               "library": "pygame"},
         '2': {"Programming Langauge": "Python",
               "library": "Selenium, Beautifulsoup"},
         '3': {"Programming Langauge": "Python, Javascript",
               "Front-end": "HTML, CSS",
               "Frame-Work": "Flask, Bootstrap"},
         '4': {"Programming Langauge": "Python",
               "library": "Tkinter"}
         }

urls = {'1': "https://github.com/iformal42/academic-project.git",
        '2': "https://github.com/iformal42/data-entry-job-bot.git",
        '3': "https://github.com/iformal42/My-Blog.git",
        '4': "https://github.com/iformal42/Typing-Test-app.git"}

videos = {'1': 'v1.mp4', '2': 'v2.mp4', '3': 'v3.mp4', '4': 'v4.mp4'}

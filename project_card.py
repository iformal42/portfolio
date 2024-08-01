class Detail:
    def __init__(self, title, content, img):
        self.title = title
        self.content = content
        self.img = img


class Card:
    def __init__(self):
        self.detail = {1: Detail(titles[1], description[1], images[1]),
                       2: Detail(titles[2], description[2], images[2]),
                       3: Detail(titles[3], description[3], images[3]),
                       4: Detail(titles[4], description[4], images[4])}


titles = {1: 'Animated Game',
          2: 'Automation',
          3: 'Blog website',
          4: 'Typing Master'}
description = {1: 'An amazing single player animated game.Reminds you your childhood',
               2: 'Automated data entry job.Complete your work within few finger clicks ',
               3: 'A Blog website where you can show case your knowledge and build your network',
               4: 'A software which would test your typing skills and speed.'}

images = {1: 'img1.png', 2: 'img2.png', 3: 'img3.png', 4: 'img4.png'}
